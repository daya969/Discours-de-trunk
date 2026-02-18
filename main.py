import os, sys, subprocess

try:
    from utils import R, G, Y, B, C, W, clear_screen, show_footer
except ImportError:
    R, G, B, W, Y = "\033[31m", "\033[32m", "\033[34m", "\033[37m", "\033[33m"
    def clear_screen(): os.system('clear' if os.name == 'posix' else 'cls')
    def show_footer(): pass

def main_menu():
    while True:
        try:
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

            if choice == "1" or choice == "01":
                if os.path.exists("server_bing.py"):
                    subprocess.run(["python3", "server_bing.py"])
                else:
                    print(f"\n{R}[!] Error: server_bing.py not found.{W}")
                    os.system("sleep 2")
            elif choice == "2" or choice == "02":
                if os.path.exists("scanner.py"):
                    subprocess.run(["python3", "scanner.py"])
                else:
                    print(f"\n{R}[!] Error: scanner.py not found.{W}")
                    os.system("sleep 2")
            elif choice == "3" or choice == "03":
                os.system("history -c && rm -f ~/.bash_history && clear")
                input("\n[+] Logs Purged. Press Enter...")
            elif choice == "0" or choice == "00":
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    main_menu()
    
