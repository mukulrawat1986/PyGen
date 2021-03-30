import requests


def main():
	# print the header
	print_the_header()

	# get zipcode from user
	code = input('What zipcode do you want the weather for (97201)? ')

	# find state and city
	state, city = get_state_and_city(code)

	# get html from web
	html = get_html_from_web(state, city, code)

	# parse the html
	# display the forecast


def print_the_header():
	print('-------------------------------')
	print('        WEATHER APP')
	print('-------------------------------')
	print()


def get_state_and_city(zipcode):
	url = 'http://ziptasticapi.com/{}'.format(zipcode)
	# set a known browser user agent
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	return response.json()['state'], response.json()['city']


def get_html_from_web(state, city, zipcode):
	url = 'http://www.wunderground.com//weather/us/{}/{}/{}'.format(state, city, zipcode)
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	return response.text


if __name__ == '__main__':
	main()
