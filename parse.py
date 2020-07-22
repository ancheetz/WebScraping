import json

with open('/Users/aczarnecki/Documents/bcr/Git/PYTHON/WebScraping/ec2.json') as f:
    data = json.load(f)

print(data)
print(type(data))

with open('data.csv', 'w') as csvfile:
    for key in data.keys():
        csvfile.write("%s, %s/n" % (key, data[key]))

        

