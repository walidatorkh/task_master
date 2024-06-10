import requests


def post_request(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    return response


def put_request(url, headers, payload):
    response = requests.put(url, headers=headers, json=payload)
    return response


def get_request(url, headers):
    response = requests.get(url, headers=headers)
    return response
