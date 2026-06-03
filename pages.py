# pages.py

import requests
from config import BASE_URL, PAGE_ID, ACCESS_TOKEN, REQUEST_TIMEOUT


def get_page_info():
    """
    Get Facebook Page Information
    """

    url = f"{BASE_URL}/{PAGE_ID}"

    params = {
        "fields": "id,name,category,fan_count,followers_count",
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

        print("\n===== PAGE INFO =====")
        print(f"Name      : {data.get('name')}")
        print(f"ID        : {data.get('id')}")
        print(f"Category  : {data.get('category')}")
        print(f"Followers : {data.get('followers_count', 'N/A')}")
        print(f"Fans      : {data.get('fan_count', 'N/A')}")
        print("=====================\n")

    except Exception as e:
        print(f"Request Failed: {e}")


def test_connection():
    """
    Test Access Token
    """

    url = f"{BASE_URL}/{PAGE_ID}"

    params = {
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code == 200:
            print("✓ Connected Successfully")
        else:
            print("✗ Connection Failed")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_connection()
    get_page_info()
