from app.config.settings import API_HOST, API_PORT
from fastapi import FastAPI
from datetime import datetime, timezone
import uvicorn


app = FastAPI()

@app.get("/")
async def healthy() -> dict:
    return {"start": datetime.now(tz=timezone.utc)}

if __name__ == '__main__':
    uvicorn.run(app, host=API_HOST, port=API_PORT)