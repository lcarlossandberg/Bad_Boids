import yaml
from StringIO import StringIO


data={"count": 5, "attraction": 0.01, "alert": 100, "formation": 10000, "strength": 0.125, "save": False, "name": 'none'}


with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=True)
