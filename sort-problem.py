import json

"""
This search gives us the index of the desired element, but it's a mess. Fix and optimize it so that
it's both sane and maintainable.
"""

def parse_brands(filename):
    """Parses in a list of brands from a json file"""
    with open(filename, 'r') as infile:
        return json.loads(infile.read())

def find_brand_by_name(brands, name):
    """
    Loops through a list of brands to find the index of the brand
    who's name matches the name parameter
    """
    for index, brand in enumerate(brands):
        if brand['name'] == name:
            return index
        
def print_brand_position(brands, name, when):
    """Finds and prints the index of a brand in the list of brands by name """
    index = find_brand_by_name(brands, name)
    print("{0} was at index {1} {2} sorting".format(name, index, when))

                
brands = parse_brands('brands.json')

print_brand_position(brands, name='2 Sisters', when='before')

brands.sort(key=lambda brand: brand['uuid'])

print_brand_position(brands, name='2 Sisters', when='after')

"""
Finally, implement and return a list of all individual books, sorted by `release_date`.
"""
