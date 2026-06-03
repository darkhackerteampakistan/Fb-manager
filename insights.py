# insights.py

import requests
from config import BASE_URL, PAGE_ID, ACCESS_TOKEN, REQUEST_TIMEOUT


def get_page_insights():
    """
    Get basic page insights
    """

    metrics = [
        "page_impressions",
        "page_reach_total",
        "page_post_engagements"
    ]

    url = f"{BASE_URL}/{PAGE_ID}/insights"

    params = {
        "metric": ",".join(metrics),
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

        print("\n===== PAGE INSIGHTS =====")

        for item in data.get("data", []):

            name = item.get("name")

            values = item.get("values", [])

            latest_value = "N/A"

            if values:
                latest_value = values[0].get("value")

            print(f"{name}: {latest_value}")

        print("=========================\n")

    except Exception as e:
        print("Error:", e)


def get_followers():
    """
    Get page followers count
    """

    url = f"{BASE_URL}/{PAGE_ID}"

    params = {
        "fields": "followers_count",
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
            print(data["error"]["message"])
            return

        print("\nFollowers:", data.get("followers_count", "N/A"))

    except Exception as e:
        print("Error:", e)


def get_page_summary():
    """
    Combined overview
    """

    print("\n===== PAGE SUMMARY =====")

    get_followers()

    print("\nLoading Insights...\n")

    get_page_insights()
