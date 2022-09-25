import sys
import requests

sys.path.append('./src/Q1')

from Q1_lab03 import *

def test_get_github_api_endpoints():
	assert get_github_api_endpoints() == {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
	assert type(get_github_api_endpoints()) == dict


def test_get_github_profile_info():
	assert get_github_profile_info("torvalds")["location"] == "Portland, OR"
	assert get_github_profile_info("torvalds")["login"] == "torvalds"
	assert get_github_profile_info("torvalds")["name"] == "Linus Torvalds"
	assert get_github_profile_info("torvalds")["type"] == "User"
	assert get_github_profile_info("torvalds")["url"] == "https://api.github.com/users/torvalds"
	assert type(get_github_profile_info("torvalds")) == dict

	assert get_github_profile_info("BjarneStroustrup")["location"] == "NY, NY, USA"
	assert get_github_profile_info("BjarneStroustrup")["login"] == "BjarneStroustrup"
	assert get_github_profile_info("BjarneStroustrup")["name"] == "Bjarne Stroustrup"
	assert get_github_profile_info("BjarneStroustrup")["type"] == "User"
	assert get_github_profile_info("BjarneStroustrup")["url"] == "https://api.github.com/users/BjarneStroustrup"
	assert type(get_github_profile_info("BjarneStroustrup")) == dict

	assert get_github_profile_info("gvanrossum")["location"] == "San Francisco Bay Area"
	assert get_github_profile_info("gvanrossum")["login"] == "gvanrossum"
	assert get_github_profile_info("gvanrossum")["name"] == "Guido van Rossum"
	assert get_github_profile_info("gvanrossum")["type"] == "User"
	assert get_github_profile_info("gvanrossum")["url"] == "https://api.github.com/users/gvanrossum"
	assert type(get_github_profile_info("gvanrossum")) == dict


	assert get_github_profile_info("username")["message"] == "Not Found"
	assert get_github_profile_info("username")["documentation_url"] == "https://docs.github.com/rest/reference/users#get-a-user"


def test_get_github_max_ratelimit():
	assert get_github_max_ratelimit() == 60
	assert type(get_github_max_ratelimit()) == int


def test_get_headers_with_session():
	assert "X-OAuth-Scopes" in get_headers_with_session().keys()
	assert get_headers_with_session()["X-RateLimit-Limit"]== '5000'
	assert type(get_headers_with_session()) == dict


def test_create_repo():
	if requests.get(f"https://api.github.com/repos/{get_github_username()}/test").status_code == 200:
		assert create_repo({'name':'test', 'description':'some test repo'}).status_code == 422
	else:
		assert create_repo({'name':'test', 'description':'some test repo'}).status_code == 201
