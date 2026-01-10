from fastapi import FastAPI, Query
import httpx

app = FastAPI()

async def get_roblox_stats(game_id: str):
    url = f"https://games.roblox.com/v1/games?universeIds={game_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            likes = data["data"][0].get("favoritesCount", 0)
            visits = data["data"][0].get("visits", 0)
            return {"likes": likes, "visits": visits}
        return {"likes": 0, "visits": 0}

@app.get("/roblox")
async def roblox_stats(game_id: str = Query(..., description="ID du jeu Roblox")):
    """
    Exemples :
    /roblox?game_id=1234567890
    """
    stats = await get_roblox_stats(game_id)
    return stats
