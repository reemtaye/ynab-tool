#!/usr/bin/env python3
import json
import requests
import sys

def usage():
    print('\nMissing an argument.  Usage:\n')
    print('$ request.py <token> e.g.')
    sys.exit()

def auth_header(token):
    request_header = {
        "Authorization": "Bearer "+ f"{token}"}
    return request_header

def submit_request(url, header, body=None):
    response = requests.get(url, headers=header, json=body)
    print(response.text)
    return response

if __name__ == "__main__":
    try:
        # request.py <token>
        token = sys.argv[1]

    except IndexError:
        usage()

budgets_url = 'https://api.youneedabudget.com/v1/budgets'
submit_request(budgets_url,auth_header(token))