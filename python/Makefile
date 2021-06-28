
all: build

build:
	@for file in plots/*.py ; do \
		echo Processing "$$file"; \
		pipenv run python $$file ; \
	done
