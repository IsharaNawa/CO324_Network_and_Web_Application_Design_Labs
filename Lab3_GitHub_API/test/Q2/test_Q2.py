import sys

sys.path.append('./src/Q2')

from Q2_lab03 import *

def test_get_github_superstars():
	assert get_github_superstars("cepdnaclk")[0] == ('uaudith/Virustotal-telegram', 22)
	assert get_github_superstars("cepdnaclk")[1] == ('AmilaIndika789/FlowChartGenerator', 8)
	assert get_github_superstars("cepdnaclk")[2] == ('gihanjayatilaka/eng.pdn.ac.lk-unofficial-interim-transcript-template', 5)
	assert get_github_superstars("cepdnaclk")[5] == ('damayanthiHerath/comet', 3)


def test_watch_winning_repo():
	assert watch_winning_repo('uaudith/Virustotal-telegram').status_code == 200
	assert watch_winning_repo('uaudith/Virustotal-telegram').json()['subscribed'] == True
	assert watch_winning_repo('uaudith/Virustotal-telegram').json()['url'] == 'https://api.github.com/repos/uaudith/Virustotal-telegram/subscription'

	assert watch_winning_repo('AmilaIndika789/FlowChartGenerator').status_code == 200
	assert watch_winning_repo('AmilaIndika789/FlowChartGenerator').json()['subscribed'] == True
	assert watch_winning_repo('AmilaIndika789/FlowChartGenerator').json()['url'] == 'https://api.github.com/repos/AmilaIndika789/FlowChartGenerator/subscription'

	assert watch_winning_repo('damayanthiHerath/comet').status_code == 200
	assert watch_winning_repo('damayanthiHerath/comet').json()['subscribed'] == True
	assert watch_winning_repo('damayanthiHerath/comet').json()['url'] == 'https://api.github.com/repos/damayanthiHerath/comet/subscription'
	

def test_make_graphql_query():
	assert make_graphql_query().json()["data"]["viewer"]["login"] == get_github_username()
	assert make_graphql_query().status_code == 200