# posts.py

import requests
from config import BASE_URL, PAGE_ID, ACCESS_TOKEN, REQUEST_TIMEOUT


def list_posts(limit=10):
    """
    Get latest page posts
    """

    url = f"{BASE_URL}/{PAGE_ID}/posts"

    params = {
        "fields": "id,message,created_time",
        "limit": limit,
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        data = response.json()

        if "error" in data:
            print("\n[ERROR]")
            print(data["error"]["message"])
            return

        posts = data.get("data", [])

        if not posts:
            print("No posts found.")
            return

        print("\n===== POSTS =====")

        for i, post in enumerate(posts, start=1):
            print(f"\n[{i}]")
            print("ID:", post.get("id"))
            print("Time:", post.get("created_time"))
            print("Message:", post.get("message", "(No Text)"))

    except Exception as e:
        print("Error:", e)


def create_post(message):
    """
    Create new page post
    """

    url = f"{BASE_URL}/{PAGE_ID}/feed"

    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.post(
            url,
            data=payload,
            timeout=REQUEST_TIMEOUT
        )

        data = response.json()

        if "error" in data:
            print("\n[ERROR]")
            print(data["error"]["message"])
            return

        print("\n✓ Post Published Successfully")
        print("Post ID:", data.get("id"))

    except Exception as e:
        print("Error:", e)


def delete_post(post_id):
    """
    Delete page post
    """

    url = f"{BASE_URL}/{post_id}"

    params = {
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.delete(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        data = response.json()

        if data.get("success"):
            print("✓ Post Deleted Successfully")
        else:
            print("Delete Failed")
            print(data)

    except Exception as e:
        print("Error:", e)
