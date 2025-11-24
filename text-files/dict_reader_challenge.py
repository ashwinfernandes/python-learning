import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        country = row['country']
        countries[country.casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)

while True:
    country = input("Please enter the name for a country (type quit to exit): ")
    country_key = country.casefold()
    if country_key in countries:
        print(f"The capital of the {country} is {countries[country_key]['capital']}")
    elif country_key.casefold() == 'quit':
        break
    else:
        print(f"Could not find the capital of {country}")
