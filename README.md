# Project Snow White

This project contains problems to be solved

## Problems

Here is the current list of problems:

- [Problem 1](project_snow_white/problems/p0001/description.md)
- [Problem 2](project_snow_white/problems/p0002/description.md)

## Solutions

Suggested solutions are written in Python in this repository.

### Requirements

- `git`, this repository must be cloned and commands are to be run from the root directory
- `make`, see <https://www.gnu.org/software/make/>, managed with `Makefile` file
- `pipenv`, see <https://github.com/pypa/pipenv>, managed with `Pipfile` and `Pipfile.lock` files
- `python 3.9`, see <https://www.python.org/>, to be used in a virtual environment with `pipenv`

### Setup

Install dependencies with

```
make install
```

Activate the `pipenv` shell environment:

```
make activate
```

Run a solution with `make run.[problem package].[problem module]`, for example:

```
make run.p0001.solution
```

### Development tools

The codebase is checked for code formatting with `black` (<https://github.com/python/black>) and
`isort` (<https://pypi.org/project/isort/>). `mypy` for static typing (<http://mypy-lang.org/>).
And `flake8` for various errors and warnings (<https://pypi.org/project/flake8/>).

_It is strongly recommended to have all of these tools configured within the editor or IDE._

Manual executions of those tools can be done with `make`:

```
# checks:
make flake
make mypy
make black-check
make isort-check

# run all above checks:
make checks

# apply black formatting on the codebase:
make black

# apply isort formatting on the codebase:
make isort
```

### Test

Run all tests with:

```
make test
```

Or specific tests with something like:

```
# test a whole file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file

# test a specific test class within a file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file.TestClassName

# test a specific test class method within a file:
make test TARGET=tests.test_directory_1.test_directory_2.test_file.TestClassName.test_method_name
```

For convenience, a file path may also be used (as "/" characters are replaced with "." characters):

```
# test a whole file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file

# test a whole file with ".py" extention also ok as ".py" is removed within the make logic:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.py

# test a specific test class within a file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.TestClassName

# test a specific test class method within a file:
make test TARGET=tests/test_directory_1/test_directory_2/test_file.TestClassName.test_method_name
```

### Dependencies

Install all dependencies (`pip` packages including development packages) with:

```
make install
```

If new packages are to be added, install them with:

```
make install PACKAGE=new_package_name
```

Or new development packages with:

```
make install DEV_PACKAGE=new_dev_package_name
```

Always commit `Pipfile` and `Pipfile.lock` changes.

Update packages with:

```
make update
```

Or update a single package with:

```
make update PACKAGE=some_package_name
```
