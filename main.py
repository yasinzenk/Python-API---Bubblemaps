from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from services import get_token_info, get_batch_token_info
from models import TokenInfoRequest, TokenInfoResponse

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/token-info/{chain}/{address}", response_model=TokenInfoResponse)
async def token_info(chain: str, address: str):
    return await get_token_info(chain, address)


@app.post("/token-info/batch", response_model=list[TokenInfoResponse])
async def token_info_batch(request: TokenInfoRequest):
    return await get_batch_token_info(request.chain, request.addresses)

