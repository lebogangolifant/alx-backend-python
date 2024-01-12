# 0x00. Python - Variable Annotations

This directory contains Python projects focused on variable annotations and type hints. Each task explores various aspects of Python's variable annotation features, including type annotations, duck typing, and using tools like `mypy` for code validation.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-add.py](0x00-python_variable_annotations/0-add.py)** - Implement a type-annotated function to add two floats.
- **Task 1: [1-concat.py](0x00-python_variable_annotations/1-concat.py)** - Implement a type-annotated function to concatenate two strings.
- **Task 2: [2-floor.py](0x00-python_variable_annotations/2-floor.py)** - Implement a type-annotated function to return the floor of a float.
- **Task 3: [3-to_str.py](0x00-python_variable_annotations/3-to_str.py)** - Implement a type-annotated function to return the string representation of a float.
- **Task 4: [4-define_variables.py](0x00-python_variable_annotations/4-define_variables.py)** - Define and annotate variables with specified values.
- **Task 5: [5-sum_list.py](0x00-python_variable_annotations/5-sum_list.py)** - Implement a type-annotated function to sum a list of floats.
- **Task 6: [6-sum_mixed_list.py](0x00-python_variable_annotations/6-sum_mixed_list.py)** - Implement a type-annotated function to sum a list of mixed integers and floats.
- **Task 7: [7-to_kv.py](0x00-python_variable_annotations/7-to_kv.py)** - Implement a type-annotated function to create key-value tuples.
- **Task 8: [8-make_multiplier.py](0x00-python_variable_annotations/8-make_multiplier.py)** - Implement a type-annotated function to create a multiplier function.
- **Task 9: [9-element_length.py](0x00-python_variable_annotations/9-element_length.py)** - Implement a type-annotated function to return a list of tuples with element lengths.
- **Task 10: [100-safe_first_element.py](0x00-python_variable_annotations/100-safe_first_element.py)** - Implement a type-annotated function to safely get the first element of a sequence.
- **Task 11: [101-safely_get_value.py](0x00-python_variable_annotations/101-safely_get_value.py)** - Implement a type-annotated function to safely get a value from a dictionary.
- **Task 12: [102-type_checking.py](0x00-python_variable_annotations/102-type_checking.py)** - Use `mypy` to validate type annotations in the provided code.

## Overview Concepts

The tasks in this directory cover the following Python concepts:

- Type annotations and variable annotations in Python 3.
- Duck typing and its relevance in Python.
- Using `mypy` for static type checking.
- Annotating function parameters and return types.
- Type hints for variables, including Union and TypeVar.
- Type annotations in variables, functions, and dictionaries.
- ...

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Pycodestyle 2.5.0
- Mypy

## Setup

1. Install Python 3.7:

```bash
sudo apt update
sudo apt install python3.7
```

2. Install Pycodestyle:

```bash
pip3 install pycodestyle==2.5.0
```

3. Install Mypy:

```bash
pip3 install mypy
```

## Usage

To run each task, execute the corresponding test file or use `mypy` for type checking:

- Example for Task 0:

```bash
./0-main.py
```

- Type checking using Mypy:

```bash
mypy 102-type_checking.py
```

