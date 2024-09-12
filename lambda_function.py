import json
from requests import get

def lambda_handler(event,context):
    ip = get('https://api.ipify.org').text
    print('My public ip is: {}'.format(ip))
    print('Version 1')
    print('Version 2')
    return 'My Public IP is:' + ip
