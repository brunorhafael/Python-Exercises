#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import requests

def main():
    print('Hello, World.')
    response = requests.get("http://www.google.com")
    print (response.text)

if __name__ == '__main__': main()
