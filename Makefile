
all: build-dot build-python

build-dot:
	make -C dot

build-python:
	make -C python
