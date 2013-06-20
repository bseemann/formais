all:
	python my_main_window.py 
interface:
	pyuic4 interface.ui -o interface.py
clean:
	rm *.pyc
