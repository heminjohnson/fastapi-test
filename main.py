from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Hemin"}

@app.get("/ticker/{ticker}")
def read_item(ticker: int, q: Optional[str] = None):
    return {"ticker": ticker, "q": q, "data": "hemin"}
