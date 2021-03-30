
def main():
	# print the header
	print_the_header()

	# get zipcode from user
	code = input('What zipcode do you want the weather for (97201)? ')

	# get html from web
	print(code)

	# parse the html
	# display the forecast


def print_the_header():
	print('-------------------------------')
	print('        WEATHER APP')
	print('-------------------------------')
	print()


if __name__ == '__main__':
	main()
