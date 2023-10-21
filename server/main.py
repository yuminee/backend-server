from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/limits")
async def get_limits():
    return {"message": "Hello Limits"}


@app.get("/limits/{limit_id}")
async def get_limits(limit_id: int):
    return {"message": f"Hello Limits {limit_id}"}