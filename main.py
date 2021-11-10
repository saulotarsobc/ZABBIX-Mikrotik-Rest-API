import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3

urllib3.disable_warnings();

response = requests.get('http://10.0.0.243/rest/interface', auth=HTTPBasicAuth('admin', 'admin'), verify=False);

print(json.dumps(response.json(), indent=4));