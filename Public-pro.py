import os, sys
try:
    __import__("test")._login()
except Exception as e:
    exit(str(e))
