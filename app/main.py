from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Returns Hello World

    Returns:
        _type_: Dict
    """
    return {"message": "Hello Worl"}
