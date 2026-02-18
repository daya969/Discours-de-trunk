import os

def patch():
    if os.path.exists("Server_bing.py"):
        with open("Server_bing.py", 'r') as f:
            d = f.read()
        
        if 's = requests.Session()' not in d:
            d = d.replace('import requests', 'import requests\ns = requests.Session()')
        
        if 'proxies' not in d:
            d = d.replace('s = requests.Session()', 's = requests.Session()\ns.proxies = {\'http\': \'socks5h://127.0.0.1:9050\', \'https\': \'socks5h://127.0.0.1:9050\'}')

        with open("Server_bing.py", 'w') as f:
            f.write(d)

if __name__ == "__main__":
    patch()
  
