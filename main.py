from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def root():
    """
    Root route welcoming to the app.
    """
    return {'message': 'Welcome to FastFood Fast.'}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
