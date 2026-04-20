from fastapi import FastAPI
from datetime import datetime, timezone
import uvicorn


app = FastAPI()

@app.get("/")
async def healthy() -> dict:
    return {"start": datetime.now(tz=timezone.utc)}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=4000)