import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/tavg/1/10/1850-2025/data.json'

# with open(json_data_source, encoding='UTF-8') as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies["description"])

for year, value in anomalies["data"].items():
    year, value = int(year), value["anomaly"]
    print(f"{year} ...{value:6.2f}")
print("*" * 80)

# print(anomalies["citation"])
