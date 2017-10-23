import json

from models import BrandDecoder

"""
This search gives us the index of the desired element, but it's a mess. Fix and optimize it so that
it's both sane and maintainable.
"""

def parse_brands(filename):
    """Parses in a list of brands from a json file"""
    with open(filename, 'r') as infile:
        return json.loads(infile.read(), cls=BrandDecoder)

def find_brand_by_name(brands, name):
    """
    Returns the index of the first brand in a list of brands whose name
    matches name
    """
    return next(i for i, brands in enumerate(brands) if brand.name == name)
        
def print_brand_position(brands, name, when):
    """Finds and prints the index of a brand in the list of brands by name"""
    index = find_brand_by_name(brands, name)
    print("{0} was at index {1} {2} sorting".format(name, index, when))

brands = parse_brands('brands.json')

print_brand_position(brands, name='2 Sisters', when='before')

brands.sort(key=lambda brand: brand.uuid)

print_brand_position(brands, name='2 Sisters', when='after')

"""
Finally, implement and return a list of all individual books, sorted by `release_date`.
"""

books = [book for brand in brands for book in brand.books]
books.sort(key=lambda book: book.release_date)

for book in books:
    print("{0} was released {1}".format(book.title, book.release_date))
