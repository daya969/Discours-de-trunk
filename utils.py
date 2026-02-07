import os
import sys
import time

# ANSI Colors for Professional TUI
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
B = '\033[1;34m' 
C = '\033[1;36m' 
W = '\033[0m'    

def clear_screen():
    """Clears the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def fade_print(text, color=W, delay=0.05):
    """Prints text with a typing effect for more style"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(W)

def purge_history():
    """Clears command history from the system"""
    try:
        os.system("history -c")
        return True
    except:
        return False

def show_footer():
    """Shows a consistent footer for all scripts"""
    print(f"\n{C}───────────────────────────────────────────────────────────{W}")
    print(f"{Y}[#] SB-PROJECT | ADMIN: DHIYA | 2026{W}")

if __name__ == "__main__":
    # Test if utils are working
    clear_screen()
    fade_print("[-] SB-UTILS MODULE LOADED SUCCESSFULLY...", G)
              
