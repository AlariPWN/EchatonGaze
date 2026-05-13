import requests
import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS

# --- IDENTIDADE VISUAL ECHATONKIROS ---
BANNER = r"""
  ______      _           _              _____                
 |  ____|    | |         | |            / ____|               
 | |__   ____| |__   __ _| |_ ___  _ __| |  __  __ _ _______ 
 |  __| / __ \ '_ \ / _` | __/ _ \| '_ \ | |_ |/ _` |_  / _ \
 | |___| (__ | | | | (_| | || (_) | | | | |__| | (_| |/ /|  __/
 |______\____|_| |_|\__,_|\__\___/|_| |_|\_____|\__,_/___\___|
                                                              
         [ PROJECT: ECHATONGAZE - OSINT RECON TOOL ]
         [ GROUP: ECHATONKIROS | BY: LARISSA CRISTINA ]
"""

# Configuração de Cores para Terminal Linux (Kali)
CYAN = "\033[1;36m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def mostrar_ajuda():
    """Exibe as opções de comando e salvamento de logs."""
    print(CYAN + BANNER + RESET)
    print(f"{YELLOW}MODO DE USO:{RESET}")
    print("  python3 echatongaze.py <username>")
    print("\n" + f"{YELLOW}OPÇÕES DE CONSULTA:{RESET}")
    print("  <username>       Alvo no GitHub para investigação passiva.")
    print("  -h, --help       Exibe este menu de ajuda.")
    print("\n" + f"{YELLOW}SALVAMENTO DE EVIDÊNCIAS (LOGS):{RESET}")
    print("  Para salvar o resultado em um arquivo enquanto visualiza no terminal:")
    print(f"  {GREEN}python3 echatongaze.py alvo | tee log_investigacao.txt{RESET}")
    print("-" * 62)

def investigar_github(username):
    """Executa a varredura passiva de metadados e arquivos sensíveis."""
    print(CYAN + BANNER + RESET)
    print(f"[*] Alvo: {username}")
    print(f"[*] Grupo: Echatonkiros")
    print("-" * 62)

    # 1. BUSCA DE EMAILS EM COMMITS (CONTORNO DE PRIVACIDADE)
    url_events = f"https://api.github.com/users/{username}/events/public"
    try:
        res_events = requests.get(url_events, timeout=10)
        emails = set()
        if res_events.status_code == 200:
            for ev in res_events.json():
                if ev['type'] == 'PushEvent':
                    for commit in ev['payload'].get('commits', []):
                        email = commit['author']['email']
                        if "noreply" not in email:
                            emails.add(f"{commit['author']['name']} <{email}>")
            
            if emails:
                print(f"{GREEN}[+] Leads de E-mail Identificados (via Commits):{RESET}")
                for e in emails: print(f"    => {e}")
            else:
                print("[-] Nenhum e-mail exposto em eventos públicos recentes.")
    except Exception as e:
        print(f"{RED}[!] Erro ao acessar API de eventos: {e}{RESET}")

    # 2. MAPEAMENTO DE REPOSITÓRIOS E SEGREDOS
    url_repos = f"https://api.github.com/users/{username}/repos"
    try:
        repos = requests.get(url_repos, timeout=10).json()
        print(f"\n[*] Analisando repositórios por ficheiros críticos...")
        
        # Extensões que costumam vazar credenciais
        ext_criticas = ['.env', '.sql', '.conf', '.key', 'settings.py', 'wp-config.php', 'id_rsa']
        
        for repo in repos:
            repo_name = repo['name']
            default_branch = repo['default_branch'] # Detecta se é main ou master
            
            # Varredura recursiva na árvore do repositório
            url_tree = f"https://api.github.com/repos/{username}/{repo_name}/git/trees/{default_branch}?recursive=1"
            res_tree = requests.get(url_tree, timeout=10)
            
            if res_tree.status_code == 200:
                tree = res_tree.json().get('tree', [])
                for file in tree:
                    path = file['path']
                    if any(path.lower().endswith(ext) for ext in ext_criticas):
                        print(f"{RED}    [!] ALERTA DE SEGREDO: {repo_name} -> {path}{RESET}")
    except:
        print(f"{RED}[!] Erro ao mapear repositórios.{RESET}")

    print("-" * 62)
    print(f"[*] Scan finalizado pela Echatonkiros.")

if __name__ == "__main__":
    # Verifica argumentos ou comando de ajuda
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        mostrar_ajuda()
    else:
        investigar_github(sys.argv[1])
