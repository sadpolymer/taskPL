import json
from sys import argv

script, tests, values = argv
values = open(values)
tests = open(tests)


values_json = json.load(values)
tests_json = json.load(tests)

def recurse(data):
    for i in data:
        if i== "value":
            for j in values_json["values"]:
                if j["id"] == data["id"]:
                    data[i] = j["value"]
        elif i == "values":
            for k in range(0,len(data[i])):
                data[i][k] = recurse(data[i][k])
    return data

report_json = recurse(tests_json)


with open("report.json", "w") as outfile:
    json.dump(report_json, outfile, indent=2)
