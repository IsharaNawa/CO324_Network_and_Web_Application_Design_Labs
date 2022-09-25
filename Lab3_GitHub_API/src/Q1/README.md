# Q1

## Q1.a
GitHub API provides many end points. Observe the available end points of GitHub API by getting the response by calling https://api.github.com. Return the response in JSON format.
```python
def get_github_api_endpoints() -> Dict:
	"""Return the JSON output of available end points"""
	pass #TODO
```

## Q1.b
Get your GitHub profile information from the endpoint (replace username with your’s) https://api.github.com/users/{username}.
```python
def get_github_profile_info(username:str) -> Dict:
	"""Return the JSON output of github profile info"""
	pass #TODO
```

## Q1.c
Servers have limited resources to serve all their clients. Hence, companies use different quota mechanisms for the proper distribution of their servers’ computational capabilities. Further, they enforce certain policies. E.g. Monetization. You can read more about how quota mechanisms are implemented in HTTP using the reference given below.
* [HTTP rate limiting](https://tools.ietf.org/id/draft-polli-ratelimit-headers-00.html#rfc.section.1.1)

In terms of this lab, you can refer to GitHub quota mechanisms using the following reference.
* [GitHub rate limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)

Implement the given function to return the maximum number of allowed unauthenticated requests to the GitHub API per hour.
```python
def get_github_max_ratelimit() -> int:
	"""Return max unauthenticated requests to GitHub API per hour"""
	pass #TODO
```

## Q1.d
Read the reference given related to HTTP sessions.
* [HTTP Sessions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Session)
* [Sessions in requests](https://docs.python-requests.org/en/master/user/advanced/)

GitHub API adds custom headers to the response. Any headers beginning with X- are custom headers, and are not included in the HTTP spec. 
1. First, run the given function `get_headers_without_session()`. 
2. Complete the `get_headers_with_session()` function to return the HTTP headers when a request is made with a session object.
```python
def get_headers_with_session() -> Dict:
	"""Returns the HTTP headers when a session is used"""
```

Observe the differences between the two headers returned.


## Q1.e
Use a session you created to create a repository owned by you by making a POST request to https://api.github.com/user/repos. Include the following request body, to create a repo named "test." (**Hint:** use the json keyword argument when calling the method requests.post)
`{'name':'test', 'description':'some test repo'}`

1. First, complete the `get_github_username()`.
```python
def get_github_username() -> str:
    """Returns the GitHub username"""
    return "YOUR_GITHUB_USERNAME"
```

2. Complete the given function to create a repo. Return the HTTP response.
```python
def create_repo(repo_data:Dict):
	"""
		1. Create a session
		2. Make a POST request to the given GitHub API endpoint to create a repo
		3. Return the HTTP response
	"""
	pass #TODO
```


