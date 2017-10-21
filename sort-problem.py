import json

"""
This search gives us the index of the desired element, but it's a mess. Fix and optimize it so that
it's both sane and maintainable.
"""


brands_string = """[{"is_featured": false, "name": "2 Sisters", "badge_image_url": "https://d1p1su8170li4z.cloudfront.net/brand_covers/561/web.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "sort_key": "2 sisters", "series": [{"large_image": "https://d1p1su8170li4z.cloudfront.net/series_covers/697/web%402x.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "name": "2 Sisters", "sort_key": "2 sisters", "etag": "6a97f7a17e88a22cc43f49f5aba77536", "volumes": [{"name": "2 Sisters: A Super-Spy Graphic Novel", "sort_key": "2 sisters_0001", "number": 1, "cover_image": "https://d35n03719o0h6x.cloudfront.net/e8ae5c755acd4b98bd65f9dd521b1f22/public/cover_image", "etag": "6a97f7a17e88a22cc43f49f5aba77536", "books": [{"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/e8ae5c755acd4b98bd65f9dd521b1f22/preview/book.tar", "page_count": 304, "is_new": false, "db_id": 6021, "series_uuid": "ab8d76014f8049c39447a185fb667932", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/e8ae5c755acd4b98bd65f9dd521b1f22", "book_uuid": "e8ae5c755acd4b98bd65f9dd521b1f22", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "25-045", "title": "2 Sisters: A Super-Spy Graphic Novel", "is_rtl": false, "etag": "6a97f7a17e88a22cc43f49f5aba77536", "is_geo_restricted": false, "next_in_series": null, "blacklist_countries": true, "sort_key": "2 sisters_0001_0001", "price": 14.99, "digital_jobnum": "28-319", "brand_uuid": "2e5db1e21ada4f9bb2d7b85332451c97", "volume_uuid": "c5450a7544354c98bac461e913c94e6c", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "2 sisters super spy graphic novel 2 sisters 2 sisters super spy graphic novel matt kindt matt kindt marie enger matt kindt", "release_date": "2015-09-30 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/e8ae5c755acd4b98bd65f9dd521b1f22/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/e8ae5c755acd4b98bd65f9dd521b1f22/2-sisters-a-super-spy-graphic-novel-hc"}], "series_uuid": "ab8d76014f8049c39447a185fb667932", "uuid": "c5450a7544354c98bac461e913c94e6c"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/e8ae5c755acd4b98bd65f9dd521b1f22/public/cover_image", "brand_uuid": "2e5db1e21ada4f9bb2d7b85332451c97", "uuid": "ab8d76014f8049c39447a185fb667932"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/e8ae5c755acd4b98bd65f9dd521b1f22/public/cover_image", "etag": "6a97f7a17e88a22cc43f49f5aba77536", "featured_image_url": null, "uuid": "2e5db1e21ada4f9bb2d7b85332451c97"}, {"is_featured": false, "name": "3 Story", "badge_image_url": "https://d1p1su8170li4z.cloudfront.net/brand_covers/9/web.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "sort_key": "3 story", "series": [{"large_image": "https://d1p1su8170li4z.cloudfront.net/series_covers/221/web%402x.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "name": "3 Story", "sort_key": "3 story", "etag": "9a18a37aeca74e6315d5bcfef1e3fabd", "volumes": [{"name": "3 Story", "sort_key": "3 story_0001", "number": 1, "cover_image": "https://d35n03719o0h6x.cloudfront.net/9b567d857c0d440b82071dc1b169b365/public/cover_image", "etag": "9a18a37aeca74e6315d5bcfef1e3fabd", "books": [{"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/4d7e20c8117b44dea6c926ae1cd23053/preview/book.tar", "page_count": 189, "is_new": false, "db_id": 1608, "series_uuid": "cf2c9d6c09f9495793d15e6998ab4053", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/4d7e20c8117b44dea6c926ae1cd23053", "book_uuid": "4d7e20c8117b44dea6c926ae1cd23053", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "15-593", "title": "3 Story: The Secret History of the Giant Man", "is_rtl": false, "etag": "c8eddec6e348c2146ce099b7ce1b8430", "is_geo_restricted": false, "next_in_series": "9b567d857c0d440b82071dc1b169b365", "blacklist_countries": true, "sort_key": "3 story_0001_0007", "price": 9.99, "digital_jobnum": "21-260", "brand_uuid": "288122ef4fab411692dbd14c39370056", "volume_uuid": "6c8e0bef3cfd4949a490e94c2c5dd82f", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "3 story secret history giant man 3 story 3 story matt kindt", "release_date": "2012-04-04 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/4d7e20c8117b44dea6c926ae1cd23053/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/4d7e20c8117b44dea6c926ae1cd23053/3-story-the-secret-history-of-the-giant-man-hc"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/9b567d857c0d440b82071dc1b169b365/preview/book.tar", "page_count": 35, "is_new": false, "db_id": 1854, "series_uuid": "cf2c9d6c09f9495793d15e6998ab4053", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/9b567d857c0d440b82071dc1b169b365", "book_uuid": "9b567d857c0d440b82071dc1b169b365", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "19-517", "title": "3 Story: Secret Files of the Giant Man One-Shot", "is_rtl": false, "etag": "9a18a37aeca74e6315d5bcfef1e3fabd", "is_geo_restricted": false, "next_in_series": null, "blacklist_countries": true, "sort_key": "3 story_0001_0008", "price": 1.99, "digital_jobnum": "21-412", "brand_uuid": "288122ef4fab411692dbd14c39370056", "volume_uuid": "6c8e0bef3cfd4949a490e94c2c5dd82f", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "3 story secret files giant man one shot 3 story 3 story matt kindt", "release_date": "2012-04-18 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/9b567d857c0d440b82071dc1b169b365/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/9b567d857c0d440b82071dc1b169b365/3-story-secret-files-of-the-giant-man"}], "series_uuid": "cf2c9d6c09f9495793d15e6998ab4053", "uuid": "6c8e0bef3cfd4949a490e94c2c5dd82f"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/9b567d857c0d440b82071dc1b169b365/public/cover_image", "brand_uuid": "288122ef4fab411692dbd14c39370056", "uuid": "cf2c9d6c09f9495793d15e6998ab4053"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/9b567d857c0d440b82071dc1b169b365/public/cover_image", "etag": "9a18a37aeca74e6315d5bcfef1e3fabd", "featured_image_url": null, "uuid": "288122ef4fab411692dbd14c39370056"}, {"is_featured": false, "name": "300", "badge_image_url": "https://d1p1su8170li4z.cloudfront.net/brand_covers/8/web.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "sort_key": "300", "series": [{"large_image": "https://d1p1su8170li4z.cloudfront.net/series_covers/236/web%402x.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "name": "300", "sort_key": "300", "etag": "2398ce4c128c32e4015c856f4665a243", "volumes": [{"name": "Volume 1", "sort_key": "300_0001", "number": 1, "cover_image": "https://d35n03719o0h6x.cloudfront.net/ab233cfd86d14b6fb237ef3ef3d8669e/public/cover_image", "etag": "2398ce4c128c32e4015c856f4665a243", "books": [{"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/ab233cfd86d14b6fb237ef3ef3d8669e/preview/book.tar", "page_count": 89, "is_new": false, "db_id": 1855, "series_uuid": "0c3e230318944016a722dfad81c4121b", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/ab233cfd86d14b6fb237ef3ef3d8669e", "book_uuid": "ab233cfd86d14b6fb237ef3ef3d8669e", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "48-339", "title": "300", "is_rtl": false, "etag": "2398ce4c128c32e4015c856f4665a243", "is_geo_restricted": false, "book_uuid_google": "ab233cfd86d14b6fb237ef3ef3d8669g", "next_in_series": null, "blacklist_countries": true, "sort_key": "300_0001_0001", "price": 13.99, "digital_jobnum": "21-712", "brand_uuid": "190bd25802f54732a8907adb591d3094", "volume_uuid": "566cf952192d47c581580303344de550", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "300 300 volume 1 frank miller frank miller lynn varley", "release_date": "2012-05-16 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/ab233cfd86d14b6fb237ef3ef3d8669e/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/ab233cfd86d14b6fb237ef3ef3d8669e/300-hc"}], "series_uuid": "0c3e230318944016a722dfad81c4121b", "uuid": "566cf952192d47c581580303344de550"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/ab233cfd86d14b6fb237ef3ef3d8669e/public/cover_image", "brand_uuid": "190bd25802f54732a8907adb591d3094", "uuid": "0c3e230318944016a722dfad81c4121b"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/ab233cfd86d14b6fb237ef3ef3d8669e/public/cover_image", "etag": "2398ce4c128c32e4015c856f4665a243", "featured_image_url": null, "uuid": "190bd25802f54732a8907adb591d3094"}, {"is_featured": false, "name": "365 Samurai", "badge_image_url": "https://d1p1su8170li4z.cloudfront.net/brand_covers/220/web.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "sort_key": "365 samurai", "series": [{"large_image": "https://d1p1su8170li4z.cloudfront.net/series_covers/337/web%402x.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "name": "365 Samurai and a Few Bowls of Rice", "sort_key": "365 samurai and a few bowls of rice", "etag": "4f828b03eff219f9d68fcdfeeefcc7f6", "volumes": [{"name": "365 Samurai and a Few Bowls of Rice", "sort_key": "365 samurai and a few bowls of rice_0001", "number": 1, "cover_image": "https://d35n03719o0h6x.cloudfront.net/54127750b7ab4af1b3696710c518896d/public/cover_image", "etag": "4f828b03eff219f9d68fcdfeeefcc7f6", "books": [{"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/54127750b7ab4af1b3696710c518896d/preview/book.tar", "page_count": 393, "is_new": false, "db_id": 2677, "series_uuid": "28ee1d3ed8d54db28eba2af322ee19fc", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/54127750b7ab4af1b3696710c518896d", "book_uuid": "54127750b7ab4af1b3696710c518896d", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "16-386", "title": "365 Samurai and a Few Bowls of Rice", "is_rtl": false, "etag": "4f828b03eff219f9d68fcdfeeefcc7f6", "is_geo_restricted": false, "next_in_series": null, "blacklist_countries": true, "sort_key": "365 samurai and a few bowls of rice_0001_0001", "price": 9.99, "digital_jobnum": "23-192", "brand_uuid": "72fc5e41062a45bcbe6585b1eff5449c", "volume_uuid": "78b6f417ee5143688f3b34f7dbfe450b", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "365 samurai few bowls rice 365 samurai few bowls rice 365 samurai few bowls rice j p kalonji j p kalonji", "release_date": "2013-01-16 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/54127750b7ab4af1b3696710c518896d/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/54127750b7ab4af1b3696710c518896d/365-samurai-and-a-few-bowls-of-rice"}], "series_uuid": "28ee1d3ed8d54db28eba2af322ee19fc", "uuid": "78b6f417ee5143688f3b34f7dbfe450b"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/54127750b7ab4af1b3696710c518896d/public/cover_image", "brand_uuid": "72fc5e41062a45bcbe6585b1eff5449c", "uuid": "28ee1d3ed8d54db28eba2af322ee19fc"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/54127750b7ab4af1b3696710c518896d/public/cover_image", "etag": "4f828b03eff219f9d68fcdfeeefcc7f6", "featured_image_url": null, "uuid": "72fc5e41062a45bcbe6585b1eff5449c"}, {"is_featured": false, "name": "47 Ronin", "badge_image_url": "https://d1p1su8170li4z.cloudfront.net/brand_covers/206/web.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "sort_key": "47 ronin", "series": [{"large_image": "https://d1p1su8170li4z.cloudfront.net/series_covers/322/web%402x.jpg?git=0abd982408fb42b1bb7456cca53449b9f6c79505", "name": "47 Ronin", "sort_key": "47 ronin", "etag": "f2dfda516d8d32766deaf1a3a6111571", "volumes": [{"name": "Volume 1", "sort_key": "47 ronin_0001", "number": 1, "cover_image": "https://d35n03719o0h6x.cloudfront.net/031dd15a233d43afaaa9d53e59868e89/public/cover_image", "etag": "f2dfda516d8d32766deaf1a3a6111571", "books": [{"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/4ff94a949b6541bb87881cb615e531d8/preview/book.tar", "page_count": 0, "is_new": false, "db_id": 3663, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/4ff94a949b6541bb87881cb615e531d8", "book_uuid": "4ff94a949b6541bb87881cb615e531d8", "country_restrictions": [], "is_approved": true, "legacy_jobnum": null, "title": "47 Ronin #1-#5 Bundle", "is_rtl": false, "etag": "d6242172d1656b02379d2f704e1f45e7", "is_geo_restricted": false, "next_in_series": "2457c85061084d2bab5295dcb916dce1", "blacklist_countries": true, "sort_key": "47 ronin_0001_0000", "price": 8.99, "digital_jobnum": null, "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 1 5 bundle 47 ronin volume 1 lovern kindzierski stan sakai stan sakai mike richardson kazuo koike", "release_date": "2013-07-31 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "", "more_info_url": "https://digital.darkhorse.com/books/4ff94a949b6541bb87881cb615e531d8/47-ronin-1-5-bundle"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/2457c85061084d2bab5295dcb916dce1/preview/book.tar", "page_count": 29, "is_new": false, "db_id": 2415, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/2457c85061084d2bab5295dcb916dce1", "book_uuid": "2457c85061084d2bab5295dcb916dce1", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "15-949", "title": "47 Ronin #1", "is_rtl": false, "etag": "2323ba4cf82f1a773ab04fdda4533d28", "is_geo_restricted": false, "next_in_series": "c09ea34d1fe447cd9b7927505d2e6e03", "blacklist_countries": true, "sort_key": "47 ronin_0001_0001", "price": 1.99, "digital_jobnum": "22-206", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 1 47 ronin volume 1 mike richardson stan sakai lovern kindzierski stan sakai", "release_date": "2012-11-07 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/2457c85061084d2bab5295dcb916dce1/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/2457c85061084d2bab5295dcb916dce1/47-ronin-1"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/c09ea34d1fe447cd9b7927505d2e6e03/preview/book.tar", "page_count": 28, "is_new": false, "db_id": 2580, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/c09ea34d1fe447cd9b7927505d2e6e03", "book_uuid": "c09ea34d1fe447cd9b7927505d2e6e03", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "21-371", "title": "47 Ronin #2", "is_rtl": false, "etag": "8d993adb49ad0963455ee6e1507f51b9", "is_geo_restricted": false, "next_in_series": "4d08f49442474a54b16a5c9774d6484c", "blacklist_countries": true, "sort_key": "47 ronin_0001_0002", "price": 1.99, "digital_jobnum": "22-207", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 2 47 ronin volume 1 mike richardson stan sakai stan sakai kazuo koike", "release_date": "2013-01-02 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/c09ea34d1fe447cd9b7927505d2e6e03/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/c09ea34d1fe447cd9b7927505d2e6e03/47-ronin-2"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/4d08f49442474a54b16a5c9774d6484c/preview/book.tar", "page_count": 30, "is_new": false, "db_id": 2806, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/4d08f49442474a54b16a5c9774d6484c", "book_uuid": "4d08f49442474a54b16a5c9774d6484c", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "21-372", "title": "47 Ronin #3", "is_rtl": false, "etag": "c7a9fbceb0c8a122797ce506577a3e91", "is_geo_restricted": false, "next_in_series": "207d14cb40444c9dbf196d9c3bd3fca5", "blacklist_countries": true, "sort_key": "47 ronin_0001_0003", "price": 1.99, "digital_jobnum": "22-208", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 3 47 ronin volume 1 mike richardson stan sakai stan sakai", "release_date": "2013-03-06 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/4d08f49442474a54b16a5c9774d6484c/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/4d08f49442474a54b16a5c9774d6484c/47-ronin-3-of-5"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/207d14cb40444c9dbf196d9c3bd3fca5/preview/book.tar", "page_count": 30, "is_new": false, "db_id": 2802, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/207d14cb40444c9dbf196d9c3bd3fca5", "book_uuid": "207d14cb40444c9dbf196d9c3bd3fca5", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "21-373", "title": "47 Ronin #4", "is_rtl": false, "etag": "ecad6bbfe9901060095c88521e4cd245", "is_geo_restricted": false, "next_in_series": "031dd15a233d43afaaa9d53e59868e89", "blacklist_countries": true, "sort_key": "47 ronin_0001_0004", "price": 1.99, "digital_jobnum": "22-209", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 4 47 ronin volume 1 mike richardson stan sakai lovern kindzierski stan sakai", "release_date": "2013-05-01 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/207d14cb40444c9dbf196d9c3bd3fca5/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/207d14cb40444c9dbf196d9c3bd3fca5/47-ronin-4"}, {"book_preview_archive": "https://drhq3xefn6rcs.cloudfront.net/031dd15a233d43afaaa9d53e59868e89/preview/book.tar", "page_count": 38, "is_new": false, "db_id": 3396, "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "site_ids": [1], "read_url": "https://digital.darkhorse.com/read/031dd15a233d43afaaa9d53e59868e89", "book_uuid": "031dd15a233d43afaaa9d53e59868e89", "country_restrictions": [], "is_approved": true, "legacy_jobnum": "21-374", "title": "47 Ronin #5", "is_rtl": false, "etag": "f2dfda516d8d32766deaf1a3a6111571", "is_geo_restricted": false, "next_in_series": null, "blacklist_countries": true, "sort_key": "47 ronin_0001_0005", "price": 1.99, "digital_jobnum": "22-210", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "volume_uuid": "8518a0866ead46f189ed383c95d25dbc", "publisher": {"name": "Dark Horse Comics", "uuid": "62af2c3eb1764b7a951903087ef404ca"}, "search_text": "47 ronin 5 47 ronin volume 1 mike richardson stan sakai lovern kindzierski stan sakai", "release_date": "2013-07-03 00:00:00", "exclusions": [], "coming_soon": false, "cover_image": "https://d35n03719o0h6x.cloudfront.net/031dd15a233d43afaaa9d53e59868e89/public/cover_image", "more_info_url": "https://digital.darkhorse.com/books/031dd15a233d43afaaa9d53e59868e89/47-ronin-5"}], "series_uuid": "ff07513ecd0d4016a3b7a0ae995e4c06", "uuid": "8518a0866ead46f189ed383c95d25dbc"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/031dd15a233d43afaaa9d53e59868e89/public/cover_image", "brand_uuid": "6577d7928c5947faa5886c471f6f5c78", "uuid": "ff07513ecd0d4016a3b7a0ae995e4c06"}], "cover_image": "https://d35n03719o0h6x.cloudfront.net/031dd15a233d43afaaa9d53e59868e89/public/cover_image", "etag": "f2dfda516d8d32766deaf1a3a6111571", "featured_image_url": null, "uuid": "6577d7928c5947faa5886c471f6f5c78"}] """

parsed_brands = json.loads(brands_string)

count = 0

for index, unsorted_brand in enumerate(parsed_brands):
    if unsorted_brand['name'] == '2 Sisters':
        print("2 Sisters was at index {} before sorting".format(index))
        break

while count < len(parsed_brands):
    for index, brand in enumerate(parsed_brands):
        if index < len(parsed_brands) - 1:
            if parsed_brands[index]['uuid'] > parsed_brands[index+1]['uuid']:
                temp = parsed_brands[index+1]
                parsed_brands[index+1] = parsed_brands[index]
                parsed_brands[index] = temp

        count += 1

for index, sorted_brand in enumerate(parsed_brands):
    if sorted_brand['name'] == '2 Sisters':
        print("2 Sisters was at index {} after sorting".format(index))
        break

"""
Finally, implement and return a list of all individual books, sorted by `release_date`.
"""
