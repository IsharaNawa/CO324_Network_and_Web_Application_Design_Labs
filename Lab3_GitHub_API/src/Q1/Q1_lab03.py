import requests
import json
from typing import Dict

def get_github_api_endpoints() -> Dict:
	"""Return the JSON output of available end points"""
	response = requests.get('https://api.github.com')
	myDict = response.json()
	return myDict


def get_github_profile_info(username:str) -> Dict:
	"""Return the JSON output of github profile info"""
	github_user_url = " https://api.github.com/users/"+username
	response = requests.get(github_user_url)
	myDict = response.json()
	return myDict


def get_github_max_ratelimit() -> int:
	"""Return max unauthenticated requests to GitHub API per hour"""
	response = requests.get('https://api.github.com')
	maxRate = response.headers['X-RateLimit-Limit']
	return  int(maxRate)

def get_headers_without_session() -> Dict:
	"""Returns the HTTP headers when a session is not used"""
	with requests.get("https://api.github.com") as response:
		return dict(response.headers)


def get_headers_with_session() -> Dict:
	"""Returns the HTTP headers when a session is used"""
	with requests.Session() as session:
		session.headers['Authorization'] = 'token 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'
		responseOfSession = session.get("https://api.github.com")
		return dict(responseOfSession.headers)


def get_github_username() -> str:
    """Returns the GitHub username"""
    return "IsharaNawarathna"

    
def create_repo(repo_data:Dict):
	"""
		1. Create a session
		2. Make a POST request to the given GitHub API endpoint to create a repo
		3. Return the HTTP response
	"""
	with requests.Session() as session:
		token = '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'
		session.auth = (get_github_username(),token)
		repoURL = "https://api.github.com/user/repos"
		login = session.post(repoURL, data=json.dumps(repo_data))
		return login

if __name__ == '__main__':
	#Q1.a
	print(json.dumps(get_github_api_endpoints(), indent=4, sort_keys=True))
	# Add code to test locally


	#Q1.b
	print(json.dumps(get_github_profile_info("IsharaNawarathna"), indent=4, sort_keys=True)) # Change username
	# Add code to test locally

	#Q1.c
	# Add code to test locally


	#print("Part d")
	#Q1.d
	print(json.dumps(get_headers_without_session(), indent=4, sort_keys=True))

	print(json.dumps(get_headers_with_session(), indent=4, sort_keys=True))
	# Add code to test locally

	#Q1.e
	repo_creation_response = create_repo({'name':'test', 'description':'some test repo'})
	# Add code to test locally
	print(repo_creation_response)
	




