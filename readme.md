# Python boilerplate project structure

Python is easy, right? Wrong! I can never remember how to structure a
project in a way that works. Hopefully this saves me some time in the future...

The goal is to be able to, without modifying any files:
- run all tests
- debug a test
- run & debug the cli module

```sh
python -m venv .venv  # if you've just cloned the repo
. .venv/Scripts/activate
# pip install -r requirements.txt  # none here, but if you've done pip freeze > requirements.txt
./run_tests.sh
python run_cli.py
```

Debugging is via vscode. Run the Python: Current file configuration.
You can also use vscode's test runner to run all tests, single tests, and debug
tests. To debug a test, right click on the play button next to the test.

To run & debug the cli, run `python run_cli.py` in this dir. Note that you can't
debug the cli.py directly with vscode, as the cli package and all other packages
are not 'self aware': they need to be run from an external context so that
pboil's __init__ file sets up package paths to allow inter-package dependencies.
