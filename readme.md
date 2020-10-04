Python is easy, right? Wrong! I can never remember how to structure a
project in a way that works. Hopefully this saves me some time in the future...


# Before starting

- do you really want to use python for your next project? It's really annoying!
- This may be outdated. Google 'modern python' first
    - eg. https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769


# If you have to

```sh
python -m venv .  # if you've just cloned the repo
. Scripts/activate
pip install -r requirements.txt  # none here, but if you've done pip freeze > requirements.txt
./run_tests.sh
python python_boilerplate.py
```
