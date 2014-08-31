clean:
	rm -rf __*

test:
	./pywrf.py wrf -t make_namelist -s 2012102518 -r 6
