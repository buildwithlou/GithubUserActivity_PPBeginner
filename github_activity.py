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
    print(f"Debug: Successfully captured username: {username}")

    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(
        url, headers={"User-Agent": "MyPythonGithubActivityApp"}
    )

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


if __name__ == "__main__":
    main()
