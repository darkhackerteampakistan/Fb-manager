# comments.py

import requests
from config import BASE_URL, ACCESS_TOKEN, REQUEST_TIMEOUT


def get_comments(post_id, limit=20):
    """
    Get comments from a page post
    """

    url = f"{BASE_URL}/{post_id}/comments"

    params = {
        "fields": "id,message,from,created_time",
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

        comments = data.get("data", [])

        if not comments:
            print("No comments found.")
            return

        print("\n===== COMMENTS =====")

        for i, comment in enumerate(comments, start=1):

            user = comment.get("from", {})
            username = user.get("name", "Unknown")

            print(f"\n[{i}]")
            print("Comment ID :", comment.get("id"))
            print("User       :", username)
            print("Time       :", comment.get("created_time"))
            print("Message    :", comment.get("message"))

    except Exception as e:
        print("Error:", e)


def reply_comment(comment_id, message):
    """
    Reply to a comment as Page
    """

    url = f"{BASE_URL}/{comment_id}/comments"

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

        print("\n✓ Reply Sent Successfully")
        print("Reply ID:", data.get("id"))

    except Exception as e:
        print("Error:", e)


def delete_comment(comment_id):
    """
    Delete a comment (if permitted)
    """

    url = f"{BASE_URL}/{comment_id}"

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
            print("✓ Comment Deleted")
        else:
            print("Delete Failed")
            print(data)

    except Exception as e:
        print("Error:", e)
