import requests

def fetch_posts(limit=5):
    """Fetches posts using limit param to limit responses."""

    posts = []
    payload = {"_limit": limit}
    req = requests.get("https://jsonplaceholder.typicode.com/posts", params=payload)
    # req = requests.get("https://httpbin.org/status/404", params=payload)
   
    if req.status_code == requests.codes.ok:
        for item in req.json():
            posts.append(item)
        return posts
    else:
        print(f"Request error! Please try again later. Error code: {req.status_code}")
        return []