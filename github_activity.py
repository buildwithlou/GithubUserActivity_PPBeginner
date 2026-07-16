import sys
import urllib.error
import urllib.request


def main():
    # 1. Check if the username argument was provided
    # Hint: Check if the length of sys.argv is less than 2
    print("What Python received:", sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    # 2. Extract the username from sys.argv
    username = sys.argv[1].strip()

    if not username:
        print("Error: Username cannot be blank.")
        sys.exit(1)

    # 3. For now, just print a success message to verify it works
    # print(f"Debug: Successfully captured username: {username}")

    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(
        url, headers={"User-Agent": "MyPythonGithubActivityApp"}
    )

    with urllib.request.urlopen(req) as response:
        raw_json_string = response.read().decode("utf-8")

    print("Successfully connected! Here is a preview of what Github sent:")
    print(raw_json_string[:300])

    try:
        with urllib.request.urlopen(req) as response:
            raw_data = response.read().decode("utf-8")
            print("Debug: Successfully fetched data from Github!")
            print(raw_data[:200])

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: The user '{username}' was not found on Github.")
        else:
            print(f"Error: Github API returned HTTP status {e.code}")
        sys.exit(1)

    except urllib.errir.URLError:
        print("Error: Failed to connect to the internet or Github servers.")
        sys.exit(1)

    try:
        # Attempt to reach Github
        with urllib.request.urlopen(req) as response:
            raw_json_String = response.read().decode("utf-8")
            print(f"Successfully fetched activity for {username}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: The user '{username}' was not found on GitHub.")
        elif e.code == 403:
            print("Error: Access forbidden. You might be rate-limited by Github.")
        else:
            print(f"Error: Github API returned status code {e.code}")
        sys.exit(1)

    except urllib.error.URLError:
        # just in case the internet is down or the URL is unreacheable
        print(
            "Error: Failed to connect to Github. Please check your internet connection."
        )
        sys.exist(1)


if __name__ == "__main__":
    main()
