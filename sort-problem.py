import json

"""
This search gives us the index of the desired element, but it's a mess. Fix and optimize it so that
it's both sane and maintainable.
"""

def parse_brands(filename):
    with open(filename, 'r') as infile:
        return json.loads(infile.read())


parsed_brands = parse_brands('brands.json')

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
