import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="qpost",
	version="0.0.1a2",
	author="medjed",
	author_email="imoshugi01@gmail.com",
	description="A basic qpost API wrapper",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/medjedqt/qpost",
	packages=setuptools.find_packages(),
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
	],
	python_requires=">=3.6"
)
