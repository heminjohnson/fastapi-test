from typing import Optional

import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Hemin"}


@app.get("/ticker/{ticker}")
def read_item(ticker: str, q: Optional[str] = None):
    return {"ticker": ticker, "q": q, "data": "hemin"}


@app.get("/reddit/trend")
async def reddit_trend():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://tradestie.com/api/v1/apps/reddit")
        return response.json()
