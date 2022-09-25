import requests
import json
from typing import List, Tuple, Dict

def get_github_superstars(organization: str) -> List[Tuple]:
	'''Sirasa superstar for Computer engineers. :)
		1. Get a list of members in the Github organization
		2. For each member, find the repo they own with the most stars.
		3. Add the repo name and the number of stars it has to a list.
		4. Return the list sorted in descending order of stars.
	'''

	output = []

	with requests.Session() as session:
		#getting the session
		token = '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'
		session.headers['Authorization'] = 'token '+token

		memberURL = "https://api.github.com/orgs/"+organization+"/members"
		response = session.get(memberURL)

		#getting the number of member pages
		links = response.headers['Link']
		links = links.rsplit(',')
		element = links[1]
		x = element.find("page=")
		number = element[x+5:]
		element = number.rsplit(';')
		element = element[0].replace('>','')
		lastPage = int(element)

		members = []

		#getting the member list
		for i in range (1,lastPage+1):
			memberURL = "https://api.github.com/orgs/" + organization + "/members?page="+str(i)
			response = session.get(memberURL)
			members.extend(response.json())

		tuple = ()

		#getting the list to be output
		for i in members:
			rePo=i['repos_url']
			repos= session.get(rePo).json()
			max = 0
			fullname = ''
			for j in repos:
				stars = j["stargazers_count"]
				if max<stars:
					max=stars
					fullname=j['full_name']
			if max != 0:
				output.append((fullname,max))

			output.sort(key = lambda x: x[1],reverse=True)

	session.close()

	return output

def watch_winning_repo(repo_name: str):
	"""Returns the HTTP response after watching the winning repo"""

	with requests.Session() as session:
		token = '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'
		session.headers['Authorization'] = 'token ' + token
		url = 'https://api.github.com/repos/'+repo_name+'/subscription'
		response = session.put(url)

	session.close()

	return response

def get_github_username() -> str:
	"""Returns the GitHub username"""
	return "IsharaNawarathna"


def make_graphql_query():
	"""Returns the HTTP response after a simple GraphQL query to GitHub API"""
	with requests.Session() as session:
		session.headers["Authorization"] = 'token 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'
		query_url = 'https://api.github.com/graphql'
		query_data = "{ \"query\": \"query { viewer { login }}\" } "
		query_data = json.loads(query_data)
		request = session.post(query_url, json=query_data)
		return request


if __name__ == "__main__":
	#Q2.a
	#top_cepdn_repos = get_github_superstars("cepdnaclk")
	#print(top_cepdn_repos)

	#Q2.b
	repo_watch_response = watch_winning_repo('uaudith/Virustotal-telegram')
	print(repo_watch_response.json()['url'])
	# Add code to test locally

	#Q2.c
	#graphql_response = make_graphql_query()
	#print(graphql_response.json())
	# Add code to test locally
