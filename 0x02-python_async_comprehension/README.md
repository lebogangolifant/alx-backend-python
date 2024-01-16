# 0x02. Python - Async Comprehension

This directory contains Python projects focused on asynchronous programming concepts, including asynchronous generators, asynchronous comprehensions, and type hints for asynchronous code. Each task explores various aspects of Python's async features.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-async_generator.py](0x02-python_async_comprehension/0-async_generator.py)** - Write an asynchronous generator that yields 10 random numbers.
- **Task 1: [1-async_comprehension.py](0x02-python_async_comprehension/1-async_comprehension.py)** - Write an asynchronous comprehension to collect 10 random numbers using the async generator.
- **Task 2: [2-measure_runtime.py](0x02-python_async_comprehension/2-measure_runtime.py)** - Import `async_comprehension` and measure its total runtime when executed four times in parallel using `asyncio.gather`.

## Overview Concepts

The tasks in this directory cover the following Python async concepts:

- Asynchronous generators and comprehensions.
- Using `asyncio` for concurrent execution of asynchronous tasks.
- Measuring runtime for async tasks.
- Type annotations for asynchronous code.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Pycodestyle 2.5.0
- Asyncio

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

3. Install Asyncio:

```bash
pip3 install asyncio
```

## Usage

To run each task, execute the corresponding test file or use the `asyncio.run` method:

- Example for Task 0:

```bash
./0-main.py
```
