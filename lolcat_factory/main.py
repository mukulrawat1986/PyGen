import os


def main():
	# print the header
	print_header()

	# get or create output folder
	get_or_create_output_folder()

	# download cats
	# display cats
	print('Hello from main')


def print_header():
	print('--------------------------------------')
	print('          CAT FACTORY')
	print('--------------------------------------')


def get_or_create_output_folder():
	base_folder = os.path.dirname(__file__)
	folder = 'cat_pictures'
	full_path = os.path.join(base_folder, folder)

	if not os.path.exists(full_path) or not os.path.isdir(full_path):
		print('Creating new directory at {}'.format(full_path))
		os.mkdir(full_path)


if __name__ == '__main__':
	main()
