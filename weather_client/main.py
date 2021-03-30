
def main():
	# print the header
	print_the_header()

	# get zipcode from user
	code = input('What zipcode do you want the weather for (97201)? ')

	# find state and city
	state, city = get_state_and_city(code)

	# get html from web
	get_html_from_web(state, city, code)

	# parse the html
	# display the forecast


def print_the_header():
	print('-------------------------------')
	print('        WEATHER APP')
	print('-------------------------------')
	print()


def get_state_and_city(zicode):
	return "MA", "BRIMFIELD"


def get_html_from_web(state, city, zipcode):
	url = 'http://www.wunderground.com//weather/us/{}/{}/{}'.format(state, city, zipcode)
	print(url)


if __name__ == '__main__':
	main()
