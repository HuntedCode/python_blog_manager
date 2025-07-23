import requests

def fetch_posts(limit=5):
    """Fetches posts using limit param to limit responses. Note: Extra client-side filtering done to simulate multiple users."""

    payload = {"_limit": limit * 10}
    try:
        req = requests.get("https://jsonplaceholder.typicode.com/posts", params=payload)
        # req = requests.get("https://httpbin.org/status/404", params=payload)
    except requests.exceptions.RequestException():
        print("Request failed. Please make sure you are connected to the internet and try again later.")
   
    if req.status_code == requests.codes.ok:
        posts = []
        seen = set()
        for item in req.json():
            uid = item['userId']
            if uid not in seen:
                posts.append(item)
                seen.add(uid)
                if len(posts) >= limit:
                    break
        return posts
    else:
        print(f"Request error! Please try again later. Error code: {req.status_code}")
        return []