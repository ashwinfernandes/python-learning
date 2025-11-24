import json

json_data_source = 'temperature_anomaly.json'

with open(json_data_source, encoding='UTF-8') as data:
    anomalies = json.load(data)

print(anomalies["description"])

for year, value in anomalies["data"].items():
    year, value = int(year), value["anomaly"]
    print(f"{year} ...{value:6.2f}")
print("*" * 80)

print(anomalies["citation"])
