
all:
	PYTHONPATH=`python gen_path.py` coverage run --branch -m pytest ./
	PYTHONPATH=`python gen_path.py` coverage report
	PYTHONPATH=`python gen_path.py` coverage html

