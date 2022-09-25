# Q2

## Q2.a
Complete the given `get_github_superstars(orgnanization)` function.
```python
def get_github_superstars(organization: str) -> List[Tuple]:
    '''Sirasa superstar for Computer engineers. :)
        1. Get a list of members in the Github organization
        2. For each member, find the repo they own with the most stars.
        3. Add the repo name and the number of stars it has to a list.
        4. Return the list sorted in descending order of stars.
    '''
```

## Q2.b
Complete the given `watch_winning_repo(repo_name)` function to watch the winning repository.
```python
def watch_winning_repo(repo_name: str):
    """Returns the HTTP response after watching the winning repo"""
    pass #TODO
```

## Q2.c
There are two major versions of the GitHub API. They are REST API and GraphQL API. Read more about them in the official documentation.

* v3: [REST API](https://docs.github.com/en/rest)
* v4: [GraphQL API](https://docs.github.com/en/graphql)

We have used REST API up to now for all the questions. This question is intended to explore about GraphQL API of GitHub.

1. First, complete the `get_github_username()`.
```python
def get_github_username() -> str:
    """Returns the GitHub username"""
    return "YOUR_GITHUB_USERNAME"
```

2. Complete the given function `def make_graphql_query()` to make a GraphQL query to the GitHub API.
```python
def make_graphql_query():
    """Returns the HTTP response after a simple GraphQL query to GitHub API"""
```

