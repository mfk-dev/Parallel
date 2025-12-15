import sys
import time
from utils.print_utils import slow_print, clear
from utils.colors import *

# Show ASCII Title Slowly
def show_title_slowly():
    slow_print("██████╗  █████╗ ██████╗  █████╗ ██╗     ██╗     ███████╗██╗     ", RESET, 0.01)
    slow_print("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██║     ██╔════╝██║     ", RESET, 0.01)
    slow_print("██████╔╝███████║██████╔╝███████║██║     ██║     █████╗  ██║     ", RESET, 0.01)
    slow_print("██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║     ██║     ██╔══╝  ██║     ", RESET, 0.01)
    slow_print("██║     ██║  ██║██║  ██║██║  ██║███████╗███████╗███████╗███████╗", RESET, 0.01)
    slow_print("╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝", RESET, 0.01)

def show_intro_scene():
    show_title_slowly()
    time.sleep(1)
    clear()
    time.sleep(0.5)

    # Entrance
    slow_print("="*50, US, 0.03)
    time.sleep(0.3)
    slow_print("DATE: June 15, 2025", GREEN, 0.03)
    slow_print("TIME: 3:17 AM", GREEN, 0.03)
    slow_print("LOCATION: Home Laboratory, Istanbul", GREEN, 0.03)
    slow_print("="*50, US, 0.03)
    time.sleep(1)
    clear()

    slow_print("\nMidnight... You're at your computer, pondering the theory that the universe is a simulation.", YELLOW, 0.05)
    slow_print("The room suddenly started to get cold.", YELLOW, 0.05)
    time.sleep(1)
    clear()

    slow_print("The clock on the wall stopped: 3:17 a.m.", BLUE, 0.07)
    time.sleep(0.8)
    slow_print("The computer screen started to tremble...", MAGENTA, 0.05)
    time.sleep(1)
    slow_print("An odd signal was detected!", MAGENTA, 0.07)
    time.sleep(0.5)
    clear()

    time.sleep(0.5)
    slow_print("="*50, US, 0.03)
    slow_print("There is a certificate on the wall, the certificate:", US, 0.03)
    time.sleep(0.5)
    slow_print("'Dr. Leon Fairfall'", YELLOW, 0.05)
    time.sleep(0.3)
    slow_print("NASA - Quantum Computing Department", YELLOW, 0.03)
    time.sleep(0.3)
    slow_print("Parallel Universe Research Specialist", YELLOW, 0.03)
    slow_print("="*50, US, 0.03)
    time.sleep(0.3)
    slow_print("The certificate started to tremble...", US, 0.03)
    time.sleep(1)

    clear()
    time.sleep(0.5)

    slow_print("EMERGENCY NOTIFICATION!", RED, 0.05)
    time.sleep(0.5)
    slow_print("Viewing The Notification..", US, 0.03)
    time.sleep(1)
    clear()

    slow_print("_"*40, RED, 0.03)
    slow_print("\nUnidentified Frequency Detected!", MAGENTA, 0.03)
    time.sleep(0.3)
    slow_print("Unauthorized Access Detected!", MAGENTA, 0.03)
    slow_print("_"*40, RED, 0.03)
    time.sleep(0.3)
    clear()
    time.sleep(0.3)
    slow_print("EMERGENCY NOTIFICATION!", RED, 0.05)
    time.sleep(0.2)
    slow_print("Access Denied!", RED, 0.03)
    time.sleep(0.3)
    slow_print("OPENING THE PARALLEL-OBS...", US, 0.05)
    time.sleep(1)
    clear()