clean:
	rm -rf __*

test:
	./pywrf.py wrf -t make_namelist
