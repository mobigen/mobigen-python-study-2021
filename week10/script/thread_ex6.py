import requests
from time import time
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'
def fetch(session, url):
   with session.get(url) as response:
       print(response.json()['uuid'])

if __name__ == "__main__":
    start = time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 50, [URL] * 50)
            executor.shutdown(wait=True) 
    print(time()-start)