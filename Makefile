test: bin/python metaL.py metaL.ini
	./$^

.PHONY: doc
doc: docs/index.html
docs/index.html: doxy.gen README.md doc/* metaL.py Makefile
	rm -rf docs ; doxygen doxy.gen 1>/dev/null