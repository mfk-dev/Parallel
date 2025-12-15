import time
from utils.print_utils import slow_print, clear
from utils.colors import *

banner = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                PARALLEL-OBS TERMINAL v1.0                  ║
║     Welcome! Use 'list' command to see the commands!.      ║
║       Use 'messages' command to see your messages!         ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""

def show_terminal_banner_slowly():
    slow_print(banner, US, 0.01)

def show_terminal_banner():
    print(US + banner + RESET)

def message_no_one():
    clear()
    show_terminal_banner()
    slow_print("-"*40, US)
    slow_print("Message #001:", US)
    slow_print("'Welcome, Doctor Fairfall.'", YELLOW, 0.04)
    slow_print("'I am the developer of Parallel-OBS, you can call me 'X' for now.'", YELLOW, 0.04)
    slow_print("'I apologize for unauthorized access to your system.'", YELLOW, 0.04)
    slow_print("'Parallel-OBS is a system interface that allows you to observe some parallel universes.'", YELLOW, 0.04)
    slow_print("'We have activated 3 parallel universes for you at the moment.'", YELLOW, 0.04)
    slow_print("'You will be able to observe more universes when you complete your current missions.'", YELLOW, 0.04)
    slow_print("'To see your current mission, use the 'missions' command.'", YELLOW, 0.04)
    slow_print("-"*40, US)

    input(YELLOW + "\nPress ENTER to continue..." + RESET)
    clear()
    show_terminal_banner()

def list_command():
    clear()
    show_terminal_banner()
    slow_print("-"*40, US)
    commands = [
        ("list", "Shows all the commands."),
        ("messages", "Shows your messages."),
        ("universes", "Lists the universes."),
        ("observe [universe_name]", "Observe a universe."),
        ("missions", "Shows you your current missions."),
    ]
    
    for cmd_name, desc in commands:
        print(f"{cmd_name:20}-{desc}")

    input(YELLOW + "\nPress ENTER to continue..." + RESET)
    clear()
    show_terminal_banner()

def universes_command():
    clear()
    show_terminal_banner()
    slow_print("-"*40, US)
    # Unlocked Universes
    slow_print("UNLOCKED UNIVERSES:", US)
    universes_open = [
        "1. Universe L**Z--R2 (command name: u1)",
        "2. Universe F2q++57* (command name: u2)", 
        "3. Universe D*0SS95- (command name: u3)"
    ]

    for universe in universes_open:
        slow_print(f"  {universe}", YELLOW)
    # Locked Universes
    slow_print("\nLOCKED UNIVERSES:", RED)
    for i in range(4, 31):
        slow_print(f"  {i}. Universe-{i:04d} - [LOCKED]", RED, 0.01)

    slow_print(f"\nTotal: 3 unlocked / 30 locked", YELLOW)

    input(YELLOW + "\nPress ENTER to continue..." + RESET)
    clear()
    show_terminal_banner()

def observe_command(cmd):
    if cmd == "observe u1":
        clear()
        show_terminal_banner()
        slow_print("Observing Universe L**Z--R2...", US, 0.05)
        time.sleep(1)
        slow_print("Observation of Universe L**Z--R2 is active!", RED, 0.05)
        slow_print("Life signs are detected in Universe L**Z--R2.", YELLOW, 0.05)
        time.sleep(0.8)
        slow_print("A question appears in the interface of L**Z--R2...", RED, 0.05)
        time.sleep(0.5)
        slow_print("WHAT IS MY NAME? ( Clue: What Are You Observing? )", US, 0.05)
        answer = input(US + "\nYour Answer: " + YELLOW).strip().lower()
        if answer == "L**Z--R2" or answer == "l**z--r2":
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS GRANTED. THANK YOU, DOCTOR FAIRFALL." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Observation Starts...")
        else:
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS DENIED. INCORRECT ANSWER." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Try Again...")
        input(YELLOW + "\nPress ENTER to continue..." + RESET)
        clear()
        show_terminal_banner()
    elif cmd == "observe u2":
        clear()
        show_terminal_banner()
        slow_print("Observing Universe F2q++57*...", US, 0.05)
        time.sleep(1)
        slow_print("Observation of Universe F2q++57* is active.", RED, 0.05)
        slow_print("Advanced technological structures detected in Universe F2q++57*.", YELLOW, 0.05)
        time.sleep(0.8)
        slow_print("A question appears in the interface of F2q++57*...", RED, 0.05)
        time.sleep(0.5)
        slow_print("WHAT IS MY NAME? ( Clue: What Are You Observing? )", US, 0.05)
        answer = input(US + "\nYour Answer: " + YELLOW).strip().lower()
        if answer == "F2q++57*" or answer == "f2q++57*":
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS GRANTED. THANK YOU, DOCTOR FAIRFALL." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Observation Starts...")
        else:
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS DENIED. INCORRECT ANSWER." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Try Again...")
        input(YELLOW + "\nPress ENTER to continue..." + RESET)
        clear()
        show_terminal_banner()
    elif cmd =="observe u3":
        clear()
        show_terminal_banner()
        slow_print("Observing Universe D*0SS95-...", US, 0.05)
        time.sleep(1)
        slow_print("Observation of Universe D*0SS95- is active!", RED, 0.05)
        slow_print("Unknown energy sources detected in Universe D*0SS95-.", YELLOW, 0.05)
        time.sleep(0.8)
        slow_print("A question appears in the interface of D*0SS95-...", RED, 0.05)
        time.sleep(0.5)
        slow_print("WHAT IS MY NAME? ( Clue: What Are You Observing? )", US, 0.05)
        answer = input(US + "\nYour Answer: " + YELLOW).strip().lower()
        if answer == "D*0SS95-" or answer == "d*0ss95-":
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS GRANTED. THANK YOU, DOCTOR FAIRFALL." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Observation Starts...")
        else:
            time.sleep(1)
            clear()
            slow_print(RED + "\nACCESS DENIED. INCORRECT ANSWER." + RESET, 0.05)
            time.sleep(0.5)
            slow_print("Try Again...")
        input(YELLOW + "\nPress ENTER to continue..." + RESET)
        clear()
        show_terminal_banner()
    else:
        clear()
        show_terminal_banner()
        slow_print(f"Universe '{cmd}' not found or locked. Type 'universes' to see which universes are unlocked and are not unlocked.", RED)


current_mission = "Solve the questions of the Universe 'L**Z--R2' and observe the environment of it." + False

def missions_command():
    clear()
    show_terminal_banner()
    slow_print("-"*40, US)
    slow_print(f"Current Mission: {current_mission}", YELLOW)
    slow_print("-"*40, US)
    input(YELLOW + "\nPress ENTER to continue..." + RESET)
    clear()
    show_terminal_banner()


def terminal_loop_first():
    show_terminal_banner_slowly()
    time.sleep(1)
    slow_print("A MESSAGE HAS BEEN DETECTED.", RED, 0.07)
    time.sleep(0.5)
    clear()
    
    show_terminal_banner()
    slow_print("You have 1 active message.", RED, 0.07)
    
    while True:
        slow_print("Enter command...", GREEN, 0.05)
        cmd = input(US + ">" + RESET + " ").strip().lower()
        
        if cmd == "messages":
            message_no_one()
        elif cmd == "list":
            list_command()
        elif cmd == "universes":
            universes_command()
        elif cmd.startswith("observe"):
            observe_command(cmd)
        elif cmd == "missions":
            missions_command()
        else:
            clear()
            show_terminal_banner()
            slow_print(f"Command '{cmd}' not found. Type 'list' to see all commands.", RED)