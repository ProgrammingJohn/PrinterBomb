# PrinterBomb
send PS files to the open raw ports on all printers on your network or just one!
# Use
simply run printer.py in the directory with discovery_printless.py
# Program
the methods used in printer.py are based off of https://github.com/RUB-NDS/PRET as well as the discovery of local printers is taken from https://github.com/RUB-NDS/PRET
only printers with port 1900 open are used to print. Some printers cannot read PS files and will error when trying to print them via the raw port, such as "ENVY" printers.
