import requests, time, os
from utils import R, G, Y, B, C, W, clear_screen, show_footer

def scanner_logic():
    clear_screen()
    print(f"""
{C}   _____  _____          _   _ _   _ ______ _____  
  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | (___ | |       /  \  |  \| |  \| | |__  | |__) |
  \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
  ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\ {W}
    """)
    
    target_url = input(f"\n{B}ENTER WEBHOOK URL {G}>> {W}")
    
    print(f"\n{Y}[*] Scanning Target Port...{W}")
    time.sleep(1.5)
    
    try:
        response = requests.get(target_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"\n{G}[+] TARGET FOUND!{W}")
            print(f"{C}─╼ Name: {W}{data.get('name')}")
            print(f"{C}─╼ ID:   {W}{data.get('id')}")
            print(f"{C}─╼ Status:{G} Ready for Injection{W}")
        else:
            print(f"\n{R}[X] TARGET OFFLINE OR INVALID!{W}")
    except:
        print(f"\n{R}[X] CONNECTION ERROR!{W}")
    
    show_footer()
    input(f"\n{Y}Press Enter to return to Master Menu...{W}")

if __name__ == "__main__":
    scanner_logic()
    
