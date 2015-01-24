from urllib.request import urlopen
import re


def counter(word, url):
	"""
	Returns the length of a list filled with a specified word
	"""
	regex = re.compile(word)
	response = urlopen(url)
	string = response.read().decode('utf-8')
	found_words = regex.findall(string)

	return len(found_words)


# Sample usage
print(counter('google', 'http://www.google.com'))