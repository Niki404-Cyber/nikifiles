import os, sys
try:
    __import__("mac").main.ap4x()
except Exception as e:
    exit(str(e))
