input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline() # skips the headings
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # countries[code.casefold()] = country_dict

# print(countries)
for country, value in countries.items():
    if len(value["capital"]) == 0:
        print(f"{country} has no capital")

    if len(value["country_code"]) == 0:
        print(f"{country} has no country code")

    if len(value["cc3"]) == 0:
        print(f"{country} has no 3 digit country code")

    if len(value["dialing_code"]) == 0:
        print(f"{country} has no dialing code")

    if len(value["timezone"]) == 0:
        print(f"{country} has no timezone")

    if len(value["currency"]) == 0:
        print(f"{country} has no currency")

while True:
    country = input("Please enter the name for a country (type quit to exit): ")
    country_key = country.casefold()
    if country_key in countries:
        print(f"The capital of the {country} is {countries[country_key]['capital']}")
    elif country_key == 'quit':
        break
    else:
        print(f"Could not find the capital of {country}")
