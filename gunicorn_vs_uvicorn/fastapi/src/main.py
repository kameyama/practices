from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """
    AWS ECSのhealthcheck用のendpint
    """
    return {"status": "OK"}


# select path from an environment variable
import os
import importlib
model=os.environ.get("MODEL")
print(model)
path=f"src.routers.{model}"
module=importlib.import_module(path)
app.include_router(getattr(module, "router"))


# # natural import
# from src.routers import wait
# app.include_router(wait.router)

