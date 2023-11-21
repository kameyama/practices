from fastapi import APIRouter, BackgroundTasks
import time
import asyncio
import os

router = APIRouter()


t=float(os.environ.get("WAITING_TIME"))

@router.get('/async')
async def wait():
    start = time.time()
    await asyncio.sleep(t)
    elapsed_time =  time.time() - start
    print(f"wait: {elapsed_time}")
    return {"wait": f"{elapsed_time}"}

@router.get('/sync')
def wait():
    start = time.time()    
    time.sleep(t)
    elapsed_time =  time.time() - start
    print(f"wait: {elapsed_time}")    
    return {"wait": f"{elapsed_time}"}

def print_wait_time(count: int):
    time.sleep(count)
    print(f"Wait {count} second & print!")


@router.get("/{count}")
async def asgi_task(count: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_wait_time, count)
    return {"status": "See the console log for wait time."}
 
