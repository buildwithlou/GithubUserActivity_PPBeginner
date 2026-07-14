import sys


def main():
    # Checking if the username argument was provided
    # By checking the length of sys.argv is less than 2
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    print(f"Debug: Successfully captured username: {username}")


if __name__ == "__main__":
    main()
