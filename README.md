# Sol Does Python

*These instructions assume that you are working within a Debian-based Linux operating system, e.g. Ubuntu; but it should not be difficult to adapt them to other platforms.*

*All console commands given here should be run **from this directory**, and not from the root of this project.*

## Installation

Before you begin in earnest, you will need access to the **python3** and **venv** commands system-wide. Python will likely be installed by default, but you can install venv with:

```
sudo apt install python3-venv
```

Then you can build your local virtual environment by running, from this directory:

```
python3 -m venv venv
```

Once the environment is built, activate it by running, again from this directory:

```
source venv/bin/activate
```

Finally, install the required PIP packages within this virtual environment by running:

```
pip install -r requirements.txt
pip install -r test_requirements.txt
```

## Activate/Deactivate Virtual Environment

As above, you can activate the virtual environment by calling `source venv/bin/activate` from this directory.

Whenever you're finished with the virtual environment, shut it down by calling `deactivate` or closing the terminal.

## Running Unit Tests Locally

1. Activate the virtual environment.
1. Run `python3 run_unit_tests_locally.py` from this directory.

## Linting

1. Activate the virtual environment.
1. Run `pylint src` from this directory.
