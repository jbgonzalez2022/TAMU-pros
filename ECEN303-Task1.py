import json

data = {}
data['students'].append({
    'name': 'Full Name',
    'GitHubID': 'GitHub ID',
    'NetID': 'TAMU NetID'
})


with open('identity.txt', 'w') as outfile:
    json.dump(data, outfile)
