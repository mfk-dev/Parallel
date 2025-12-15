import sys
import time
import os
from .colors import *

# Slow Print Function
def slow_print(text, color=RESET, delay=0.08):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Clearing The Terminal Function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')