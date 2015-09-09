all: DESCRIPTION.rst


DESCRIPTION.rst: README.md
	pandoc -f markdown -t rst -o $@ $<


upload: all
	python setup.py clean bdist bdist_wheel sdist upload
