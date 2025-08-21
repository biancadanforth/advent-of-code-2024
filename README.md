# Advent of Code 2024

Python solutions to Advent of Code 2024 (https://adventofcode.com/2024) challenges using TDD (Test Driven Development).

## To clone the repo locally
```
git clone <repo_url>
cd <repo_name>
```

## To set up a dev environment

1. Install and activate a virtual environment
```
python -m venv venv
source venv/bin/activate
```
You will need to run the second command each time you open or restart your terminal.
2. Install python packages into the virtual environment
```
pip install -r requirements.in
```

## To run checks and tests
Make sure your [virtual env is activated](#to-set-up-a-dev-environment).

### Running all tests
```
ruff check
pytest
```

### Running test(s) in a single directory
Make sure your [virtual env is activated](#to-set-up-a-dev-environment).
```
pytest [test file or directory]
```
For example, to run the test from `day01`, you could do:
```
pytest day01
```

## To run one of the exercises
Make sure your [virtual env is activated](#to-set-up-a-dev-environment).
```
python path/to/exercise/file
```
For example, to run the exercise from `day01`, you could do:
```
cd day01
python day01.js
```