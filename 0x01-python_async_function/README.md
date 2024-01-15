# 0x01. Python - Async

This directory contains Python projects focused on asynchronous programming in Python, specifically using Async IO. Each task explores various aspects of Async IO, asyncio, and related concepts.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-basic_async_syntax.py](0x01-python_async_function/0-basic_async_syntax.py)** - Implement an asynchronous coroutine to wait for a random delay.
- **Task 1: [1-concurrent_coroutines.py](0x01-python_async_function/1-concurrent_coroutines.py)** - Implement an async routine to run concurrent coroutines.
- **Task 2: [2-measure_runtime.py](0x01-python_async_function/2-measure_runtime.py)** - Measure the runtime of an async program using asyncio.
- **Task 3: [3-tasks.py](0x01-python_async_function/3-tasks.py)** - Create an asyncio.Task using regular function syntax.
- **Task 4: [4-tasks.py](0x01-python_async_function/4-tasks.py)** - Alter code from wait_n to create a new function task_wait_n.

## Overview Concepts

- Understand async and await syntax in Python.
- Execute an async program with asyncio.
- Run concurrent coroutines using asyncio.
- Create asyncio tasks using regular function syntax.
- Use the random module for generating random values.

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

## Usage

To run each task, execute the corresponding test file or use asyncio.run:

- Example for Task 0:

```bash
./0-main.py
```

- Example for Task 1:

```bash
./1-main.py
```
