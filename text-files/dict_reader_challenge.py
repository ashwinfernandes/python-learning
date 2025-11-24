import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    reader = csv.DictReader(country_file, delimiter="|")
    for row in reader:
        country = row['Country']
        countries[country.casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)

while True:
    country = input("Please enter the name for a country (type quit to exit): ")
    country_key = country.casefold()
    if country_key in countries:
        print(f"The capital of the {country} is {countries[country_key]['Capital']}")
    elif country_key == 'quit':
        break
    else:
        print(f"Could not find the capital of {country}")
