import httpx as requests
from asyncio import run, gather

from functools import wraps
import time


def stop_watch(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        elapsed_time =  time.time() - start
        print(f"{func.__name__} is {elapsed_time} sec")
        return result
    return wrapper

n=10
        
urls1 = ["http://fastapi-uvicorn:8000/sync"] * n
urls2 = ["http://fastapi-uvicorn:8000/async"] * n
urls3 = ["http://fastapi-gunicorn:8000/sync"] * n
urls4 = ["http://fastapi-gunicorn:8000/async"] * n
urls5 = ["http://flask:8000/wait"] * n

@stop_watch
def req(url):
    return requests.get(url).json()["wait"]

def sync_func(urls):
    res=sorted([float(req(u)) for u in urls])

def main(urls):
    start = time.time()
    sync_func(urls)
    elapsed_time =  time.time() - start
    print(f"tolal time: {elapsed_time} sec.")

# print("sync")
# main(urls1)
# main(urls2)
# main(urls3)
# main(urls4)

async def async_request(client,url):
    start = time.time()
    r = await client.get(url)
    j = r.json()
    elapsed_time =  time.time() - start
    #return float(j["wait"])
    return elapsed_time

async def async_func(urls):
    async with requests.AsyncClient(timeout=requests.Timeout(50.0, read=100.0)) as client:
        tasks = [async_request(client,u) for u in urls]
        res=await gather(*tasks, return_exceptions=True)
        print(sorted(res))


def main2(urls):
    print(urls[0])
    start = time.time()
    run(async_func(urls))
    elapsed_time =  time.time() - start
    print(f"total time: {elapsed_time} sec.")
    print("")

print("")
print("async")
main2(urls1)
main2(urls2)
main2(urls3)
main2(urls4)
main2(urls5)
