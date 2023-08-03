import requests

res = requests.post(
    "http://127.0.0.1:8000",
    json={
        "query": "Metas latest products and news"
    }
).json()

print(res)