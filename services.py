import httpx
from models import TokenInfoResponse, PoolData

# Base URL for querying Dexscreener token pools
DEXSCREENER_URL = "https://api.dexscreener.com/token-pairs/v1"


async def get_token_info(chain: str, address: str) -> TokenInfoResponse:
    """
    Fetches pool data for a given token on a given chain.
    Returns the largest pool, total liquidity, and number of pools.
    """
    url = f"{DEXSCREENER_URL}/{chain}/{address}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    # If request failed or token not found, return empty result
    if response.status_code != 200:
        return TokenInfoResponse(
            chain=chain,
            token_address=address,
            largest_pool=None,
            total_liquidity_usd=0.0,
            number_of_pools=0
        )

    pools = response.json()

    if not pools:
        return TokenInfoResponse(
            chain=chain,
            token_address=address,
            largest_pool=None,
            total_liquidity_usd=0.0,
            number_of_pools=0
        )

    # Identify the pool with the highest liquidity
    largest = max(pools, key=lambda p: p.get("liquidity", {}).get("usd", 0))

    # Calculate the total liquidity across all pools
    total_liquidity = sum(p.get("liquidity", {}).get("usd", 0) for p in pools)

    # Format the largest pool into a structured model
    largest_pool = PoolData(
        dex_id=largest.get("dexId"),
        pair_address=largest.get("pairAddress"),
        base_token=largest.get("baseToken"),
        quote_token=largest.get("quoteToken"),
        liquidity_usd=largest.get("liquidity", {}).get("usd", 0),
        volume_usd=largest.get("volume", {}).get("h24", 0)
    )

    return TokenInfoResponse(
        chain=chain,
        token_address=address,
        largest_pool=largest_pool,
        total_liquidity_usd=total_liquidity,
        number_of_pools=len(pools)
    )


async def get_batch_token_info(chain: str, addresses: list[str]) -> list[TokenInfoResponse]:
    """
    Processes a list of token addresses and returns a list of TokenInfoResponse objects.
    """
    results = []
    for addr in addresses:
        info = await get_token_info(chain, addr)
        results.append(info)
    return results
