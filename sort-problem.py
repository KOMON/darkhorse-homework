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


parsed_brands = parse_brands('brands.json')

print_brand_position(parsed_brands, name='2 Sisters', when='before')

count = 0
while count < len(parsed_brands):
    for index, brand in enumerate(parsed_brands):
        if index < len(parsed_brands) - 1:
            if parsed_brands[index]['uuid'] > parsed_brands[index+1]['uuid']:
                temp = parsed_brands[index+1]
                parsed_brands[index+1] = parsed_brands[index]
                parsed_brands[index] = temp

        count += 1

print_brand_position(parsed_brands, name='2 Sisters', when='after')

"""
Finally, implement and return a list of all individual books, sorted by `release_date`.
"""
