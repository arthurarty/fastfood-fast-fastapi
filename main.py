from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    """
    Root route welcoming to the app.
    """
    return {'message': 'Welcome to FastFood Fast.'}
