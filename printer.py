
# python standard library
from socket import socket
import os, re, time
from discovery_printless import discovery

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
# ------------------------[ print <file>|"text" ]----------------------------

def do_print(path, target):
  sock = socket()
  file = None
  port = 9100
  sock.settimeout(10)
  # target is a character device
  if os.path.exists(target) \
    and stat.S_ISCHR(os.stat(target).st_mode):
      file = os.open(target, os.O_RDWR)
  # treat target as ipv4 socket
  else:
    m = re.search('^(.+?):([0-9]+)$', target)
    if m:
      [target, port] = m.groups()
      port = int(port)
    sock.connect((target, port))

  # if path.endswith('.ps'): data = file().read(arg) # postscript file

  with open(path, 'rb') as f:
    data = f.read()
    # print(data)

  UEL = '\x1b' + '%-12345X'

  if data: sock.sendall((UEL + data.decode() + UEL).encode()) # send pcl datastream to printer
  sock.close()


if __name__ == "__main__":
  dis = discovery()
  scan = dis.scan()
  if scan[0] == 0: 
    print(f'{bcolors.FAIL}no printers found...')
  else:
    for i in scan[1]:
      print(f"{bcolors.OKCYAN}{i[0]} : {i[1][0]} ({i[1][2].strip()})")
    path = input(f'{bcolors.ENDC}{bcolors.BOLD}path: ')
    cont = input(f"{bcolors.ENDC}{bcolors.BOLD}print on all? y/n: ")
    if cont == 'y':
      for i in scan[1]:
        printer_ip = i[0]
        if 'ENVY' not in i[1][0]:
          do_print(path, printer_ip)
        else:
          print(f'{bcolors.ENDC}{bcolors.FAIL}ENVY printer doesn\'t support raw printing')
      print(f"\n{bcolors.ENDC}{bcolors.OKGREEN}-- done ----------\n")
      # time.sleep(2)
      for i in scan[1]:
        print(f"{bcolors.ENDC}{bcolors.OKCYAN}{i[0]} : {i[1][0]} ({i[1][2].strip()})")
    else:
      if input(f"{bcolors.ENDC}{bcolors.BOLD}print to one? y/n: ") == "y":
        printer_ip = input('printer ip: ')
        if 'ENVY' not in i[1][0]:
          do_print(path, printer_ip)
          print(f"\n{bcolors.ENDC}{bcolors.OKGREEN}-- done ----------\n")
          a = [i[0] for i in scan[1]]
          i = scan[1][a.index(printer_ip)]
          print(f"{bcolors.ENDC}{bcolors.OKCYAN}{i[0]} : {i[1][0]} ({i[1][2].strip()})")
        else:
          print(f'{bcolors.ENDC}{bcolors.FAIL}ENVY printer doesn\'t support raw printing')
