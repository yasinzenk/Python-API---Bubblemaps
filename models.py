from pydantic import BaseModel
from typing import List, Optional

class PoolData(BaseModel):
    dex_id: str
    pair_address: str
    base_token: dict
    quote_token: dict
    liquidity_usd: float
    volume_usd: float

class TokenInfoResponse(BaseModel):
    chain: str
    token_address: str
    largest_pool: Optional[PoolData]
    total_liquidity_usd: float
    number_of_pools: int

class TokenInfoRequest(BaseModel):
    chain: str
    addresses: List[str]