# 📡 Python API – Bubblemaps Technical Test

This project is a FastAPI-based REST API developed as part of a backend/cloud technical test for **Bubblemaps**.  
It provides real-time access to liquidity pool data for a given token on a supported chain, using the [Dexscreener public API](https://docs.dexscreener.com/api/reference).

---

## ✅ Features

- `GET /token-info/{chain}/{address}`  
  → Returns the largest pool by liquidity, the total liquidity across all pools, and the number of pools for a given token.

- `POST /token-info/batch`  
  → Accepts a list of token addresses for the same chain and returns the same data for each.

- Swagger documentation available at `/docs`.

---

## ⚙️ Stack

| Tool       | Role                          |
|------------|-------------------------------|
| Python     | Backend logic                 |
| FastAPI    | Web framework                 |
| httpx      | Async external API calls      |
| Pydantic   | Request/response validation   |
| GCP Cloud Run | Deployment (serverless)   |

---

## 🚀 API Deployment

The API is deployed and publicly accessible here:  
**🔗 [`https://bubblemaps-api-xxxxx.a.run.app/docs`](https://bubblemaps-api-xxxxx.a.run.app/docs)**

---

## 🧠 Implementation Notes

- Designed with modularity and clean separation: routing, services, models.
- Token info is fetched live from Dexscreener (`/token-pairs/v1/{chain}/{tokenAddress}`).
- The “largest pool” is computed by comparing `liquidity.usd` values.
- No persistent storage is used — live computation only.
- API is chain-agnostic (supports `solana`, ready to extend to `ethereum`, etc).
- Basic rate limiting handled by respecting Dexscreener quotas (300 req/min).

---

## ▶️ Run Locally

1. Clone the repo
2. Install dependencies
   
```bash
pip install -r requirements.txt
```

3. Install dependencies

```bash
uvicorn main:app --reload
```
## 📬 Submission

This project was completed as part of the Bubblemaps backend/cloud technical test.
If any additional clarification is needed, feel free to reach out.
