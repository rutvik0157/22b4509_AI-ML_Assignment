install:
	python3 -m venv venv
	. ./venv/bin/activate && pip install -r requirements.txt && make run

run:
	. ./venv/bin/activate && python main.py --subject=ancient_history
