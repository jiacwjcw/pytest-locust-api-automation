# Introduction
For further information on pytest, take a look at https://docs.pytest.org/en/stable/


# Project Setup

This project is build with `python 3.8.5`

It is recommended to use a python virtual environment to run python projects. You can set it up by following this: https://github.com/pyenv/pyenv-virtualenv

Once your python environment is setup, you need to install the required packages by running

```
pip install -r requirements.txt
```

## Functional Tests

To run functional tests run

```
pytest
```

This runs all of the test files configured in `pytest.ini`

The run also generates result artifacts under the `results` directory. These results can be viewed as an HTML page by running

```
allure serve results/
```
