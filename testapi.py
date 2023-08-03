import requests

res = requests.post(
    "https://researchagent.onrender.com",
    json={
        "query": "Metas latest products and news"
    }
).json()

print(res)