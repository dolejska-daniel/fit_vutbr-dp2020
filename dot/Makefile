
all: build

build:
	@for file in *.dot ; do \
		echo Processing "$$file"; \
		dot -Tpdf "$$file" -o"../build/$${file%.dot}.pdf" ; \
	done
