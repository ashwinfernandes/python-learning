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

# print(countries)
country = input("Please enter the name for a country: ")
if country.casefold() in countries:
    print(f"The capital of the {country} is {countries[country.casefold()]['capital']}")
else:
    print(f"Could not find the capital of {country}")
