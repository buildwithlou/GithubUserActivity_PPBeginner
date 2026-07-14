# Github User Activity by Lourdes Pampa
Github user activity Python Project Beginner is a project that will fetch a recent activity of a Github user.

Following the instructions of the Github User Activity Project Roadmap
>>https://roadmap.sh/projects/github-user-activity

This tool is built specifically to practice core backend and DevOps automation patterns, focusing on robust data serialization and clean system execution.

## System Architecture & CLI Usage

The application accepts commands and arguments dynamically via terminal inputs.

```bash
# Provide the GitHub username as an argument when running the CLI.
github-activity <username>

# Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user's activity:
https://api.github.com/users/<username>/events
Example: https://api.github.com/users/kamranahmedse/events

#Display the fetched activity in the terminal.
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...


