import requests

res = requests.post(
    "https://searchagent.onrender.com",
    json={
        "query": "Metas latest products and news"
    }
).json()

print(res)