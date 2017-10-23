import json

class Brand:    
    def __init__(self, **kwargs):
        defaults = {
            'is_featured': False,
            'name': '',
            'badge_image_url': '',
            'sort_key': '',
            'series': [],
            'cover_image': '',
            'etag': '',
            'uuid': ''
        }
        for prop, default in defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def volumes(self):
        return [volume for series in self.series for volume in series.volumes]

    @property
    def books(self):
        return [book for series in self.series for book in series.books]
    
    @staticmethod
    def decode(json_map):
        return Brand(**json_map)

class Series:
    def __init__(self, **kwargs):
        defaults = {
            'large_image': '',
            'name': '',
            'etag': '',
            'volumes': [],
            'cover_image': '',
            'brand_uuid': '',
            'uuid': ''
        } 
        for prop, default in defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def books(self):
        return [book for volume in self.volumes for book in volume.books]
            
    @staticmethod
    def decode(json_map):
        return Series(**json_map)

class Volume:
    def __init__(self, **kwargs):
        defaults = {
            'name': '',
            'sort_key': '',
            'number': 1,
            'cover_image': '',
            'etag': '',
            'books': [],
            'series_uuid': '',
            'uuid': ''
        }
        for prop, default in defaults.items():
            setattr(self, prop, kwargs.get(prop, default))    

    @staticmethod
    def decode(json_map):
        return Volume(**json_map)

class Book:
    def __init__(self, **kwargs):
        defaults = {
            'book_preview_archive': '',
            'page_count': 0,
            'is_new': False,
            'db_id': 0,
            'series_uuid': '',
            'site_ids': [],
            'read_url': '',
            'book_uuid': '',
            'country_restrictions': [],
            'is_approved': False,
            'legacy_jobnum': '',
            'title': '',
            'is_rtl': False,
            'etag': '',
            'is_geo_restricted': False,
            'next_in_series': None,
            'blacklist_countries': True,
            'sort_key': '',
            'price': 0.0,
            'digital_jobnum': '',
            'brand_uuid': '',
            'volume_uuid': '',
            'publisher': None,
            'search_text': '',
            'release_date': '',
            'exclusions': [],
            'coming_soon': False,
            'cover_image': '',
            'more_info_url': ''
        }
        for prop, default in defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

    @staticmethod
    def decode(json_map):
        return Book(**json_map)


class BrandDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook,
                                  *args, **kwargs)

    def object_hook(self, obj):
        if 'series' in obj:
            return Brand.decode(obj)
        elif 'volumes' in obj:
            return Series.decode(obj)
        elif 'books' in obj:
            return Volume.decode(obj)
        elif 'book_uuid' in obj:
            return Book.decode(obj)
        else:
            return obj
