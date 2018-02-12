

"""
The world's most awesome hello world module
"""

import sys

def hello(name='World'):
	"""
	Return a greeting for the given name
	"""

	return 'Hello, {}'.format(name)

def main():
	"""
	Reads input from args paased into the script and prints the output to stdout
	"""

	args = sys.argv[1:]
	name = ' '.join(args).strip()
	if name:
		print(hello(name))
	else: 
		print(hello())

if __name__ == '__main__':
	main()