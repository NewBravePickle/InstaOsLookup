import urllib.request
import urllib.parse
import sys

INSTAGRAM_API = "https://i.instagram.com/api/v1/"
USER_AGENT = "Instagram 219.0.0.12.117 Android"
IG_APP_ID = "136619743395469"

def lookup_user(query):
    url = INSTAGRAM_API + "users/lookup/"
    headers = {
        "User-Agent": USER_AGENT,
        "X-IG-App-ID": IG_APP_ID,
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = urllib.parse.urlencode({"q": query}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <query>")
        sys.exit(1)

    lookup_user(sys.argv[1])
