# 웹 페이지를 다운받는 프로그램 

import requests
from time import time

URL = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

if __name__ == "__main__":
    start = time()
    with requests.Session() as session:
        for _ in range(50):
            fetch(session, URL)
    # end = time()
    print(time()-start)