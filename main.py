import sys
import os

# To be able to add modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scenes.intro import show_intro_scene
from scenes.terminal import terminal_loop_first

def main():
    # Intro Scene
    show_intro_scene()
    
    # Terminal Loop
    terminal_loop_first()
    
    # End Of The Game ( Not Active For Now )
    # print("\n" + "="*50)
    # print("="*50)

if __name__ == "__main__":
    main()