import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

json_str = json.dumps(data)

print json_str