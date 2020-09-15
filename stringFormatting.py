Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ['Ishaku', 'Ralph', 'Musa', 'Casper']
>>> ages = [30, 32, 33, 32]
>>> for index in range(5):
	'{:<10s} is {:>10d} years old'.format(names[index], ages[index]
					      