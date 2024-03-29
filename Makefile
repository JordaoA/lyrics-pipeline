VENV?=venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

help:
	@echo "Hello Make?!"

venv:$(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

run:
	$(PYTHON) pipeline.py

clean:
	@rm -rf $(VENV)