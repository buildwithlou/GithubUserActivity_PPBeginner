import sys


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


if __name__ == "__main__":
    main()
