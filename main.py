import os, sys
from utils import R, G, Y, B, C, W, clear_screen, show_footer

def main_menu():
    while True:
        clear_screen()
        print(f"""
{B}   ██████╗ ██████╗       ██████╗  █████╗ ███╗   ██╗ ██████╗ 
  ██╔════╝ ██╔══██╗      ██╔══██╗██╔══██╗████╗  ██║██╔════╝ 
  ╚█████╗  ██████╔╝█████╗██████╔╝███████║██╔██╗ ██║██║  ███╗ 
   ╚═══██╗ ██╔══██╗╚════╝██╔══██╗██╔══██║██║╚██╗██║██║   ██║ 
  ██████╔╝ ██████╔╝      ██████╔╝██║  ██║██║ ╚████║╚██████╔╝ 
  ╚═════╝  ╚═════╝       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ {W}
                                {R}[ Admin Edition - 2026 ]{W}
        """)
        print(f"{G}[01]{W} Run SERVER BING (Lag Protocol)")
        print(f"{G}[02]{W} Run TARGET SCANNER (Webhook Check)")
        print(f"{G}[03]{W} Purge System Logs & History")
        print(f"{G}[00]{W} Exit Control Center")
        show_footer()
        
        choice = input(f"\n{R}SB-MASTER {G}>> {W}")

        if choice == "01":
            os.system("python3 server_bing.py")
        elif choice == "02":
            os.system("python3 scanner.py")
        elif choice == "03":
            os.system("history -c && clear")
            print(f"\n{G}[+] Logs Purged Successfully!{W}")
            input("\nPress Enter...")
        elif choice == "00":
            sys.exit()
        else:
            os.system("sleep 1")

if __name__ == "__main__":
    main_menu()

