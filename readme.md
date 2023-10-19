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
python python_boilerplate.py
```

Debugging is via vscode. Run the Python: Current file configuration.


todo
- add cli package
