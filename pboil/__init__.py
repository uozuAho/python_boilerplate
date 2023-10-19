import sys, os

# add pboil to the package path, so packages can use each other
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
