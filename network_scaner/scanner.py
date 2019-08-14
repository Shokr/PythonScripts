import nmap

nm = nmap.PortScanner()

ip = input('IP:- ')
port = input('Port:- ')

print('------------------------------------')
print(nm.scan(ip, port))
print('------------------------------------')
print(nm.command_line())
print('------------------------------------')
print(nm.scaninfo())
print('------------------------------------')
print(nm.all_hosts())
print('------------------------------------')
print(nm[ip].hostname())
print('------------------------------------')