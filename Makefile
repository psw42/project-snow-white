.PHONY: activate install update run \
		flake flake8 mypy mypy-context black black-check isort isort-check check checks

.DEFAULT_GOAL := activate

SHELL := /bin/bash

PIPENV_RUN = PYTHONPATH=${PYTHONPATH}:${PWD} pipenv run

ROOT_PYTHON_PACKAGES = project_snow_white


list:
	# Listing of available make targets
	@(grep -oe '^[[:lower:][:digit:]_\-\ ]\{1,\}:' Makefile | tr -d ':' | uniq)

activate:
	pipenv shell

install: # examples: make install DEV_PACKAGE=mypy ; make install PACKAGE=requests ; make install
ifneq ($(DEV_PACKAGE),)
	$(PIPENV_RUN) pipenv install -d $(DEV_PACKAGE) $(ARGS)
else
ifneq ($(PACKAGE),)
	$(PIPENV_RUN) pipenv install $(PACKAGE) $(ARGS)
else
	$(PIPENV_RUN) pipenv install -d $(ARGS)
endif
endif

update:
	$(PIPENV_RUN) pipenv update $(PACKAGE) $(ARGS)

run.%:
	$(PIPENV_RUN) python -m project_snow_white.problems.$(*)

flake flake8:
	$(PIPENV_RUN) flake8 $(ROOT_PYTHON_PACKAGES) $(ARGS)

mypy:
	$(PIPENV_RUN) mypy $(ROOT_PYTHON_PACKAGES) $(ARGS)

mypy-context: # show error context not used as default as it can be a bit verbose with many errors
	make mypy ARGS="--show-error-context $(ARGS)"

black:
	$(PIPENV_RUN) black $(ROOT_PYTHON_PACKAGES) $(ARGS)

black-check:
	make black ARGS="--check $(ARGS)"

isort:
	$(PIPENV_RUN) isort $(ROOT_PYTHON_PACKAGES) $(ARGS)

isort-check:
	make isort ARGS="--check-only $(ARGS)"

check checks:
	@(echo "FLAKE8..." && make flake > /dev/null 2>&1 && echo "          OK")
	@(echo "MYPY..." && make mypy > /dev/null 2>&1 && echo "          OK")
	@(echo "BLACK..." && make black-check > /dev/null 2>&1 && echo "          OK")
	@(echo "ISORT..." && make isort-check > /dev/null 2>&1 && echo "          OK")
