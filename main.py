import asyncio

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


async def token_stream():
    for token in ["Hello", ", ", "world", "!"]:
        yield token
        await asyncio.sleep(0.1)


@app.get("/stream")
async def stream():
    return StreamingResponse(token_stream(), media_type="text/plain")
