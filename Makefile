all:
	pyuic4 interface.ui -o interface.py
	python my_main_window.py 
clean:
	rm *.pyc
