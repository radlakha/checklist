# FILEPATH: /workspaces/checklist/Makefile

# Variables
VENV_NAME?=.venv
PYTHON_VERSION?=3
PYTHON_INTERPRETER=$(VENV_NAME)/bin/python$(PYTHON_VERSION)

# Targets
install:
	# Create virtual environment
	python$(PYTHON_VERSION) -m venv $(VENV_NAME)
	# Upgrade pip
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	# Install dependencies
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	@echo "\033[0;32m"
	@echo ">>> Don't forget to activate the virtual environment! Run 'source $(VENV_NAME)/bin/activate'"
	@echo ">>> To deactivate, run 'deactivate'"
	@echo ">>> To add to your bash profile, run 'echo \"source $(VENV_NAME)/bin/activate\" >> ~/.bash_profile'"
	@echo "\033[0m"

format:
	# Format code
	$(PYTHON_INTERPRETER) -m black .

lint:
	# Lint code
	$(PYTHON_INTERPRETER) -m flake8 .

test:
	# Run tests
	$(PYTHON_INTERPRETER) -m pytest

deploy:
	# Deploy to wherever

run:
	# Run the Python script
	$(PYTHON_INTERPRETER) script.py

clean:
	# Remove virtual environment
	# rm -rf $(VENV_NAME)

add:
	# Add a new expected file to the checklist
	$(PYTHON_INTERPRETER) add_to_checklist.py $(file_name)
