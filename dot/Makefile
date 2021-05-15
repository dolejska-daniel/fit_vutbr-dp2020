
all: build

build:
	@mkdir -p ../build/dot
	@for file in *.dot ; do \
		echo Processing "$$file"; \
		dot -Tpdf "$$file" -o"../build/$${file%.dot}.pdf" ; \
	done

clean:
	rm -f ../build/dot/*.pdf
