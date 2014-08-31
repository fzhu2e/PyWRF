clean:
	rm -rf __*

test:
	#./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818
	./pywrf.py wps -t make_namelist -s 2012102518 -e 2012102818 -r 72
	#./pywrf.py wps -t make_namelist -s 2012102518 -r 72
	#./pywrf.py wrf -t make_namelist -s 2012102518 -r 6
