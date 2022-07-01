import hashlib
from art import *
from traceback import print_tb

tprint("Hash Generator\nby\nPeruKingo")

while True:
    # Methode auswählen
    while True:
        auswahl = input("\nWähle ein Hash-Methode aus: ")
        if auswahl == "md5" or auswahl == "sha1" or auswahl == "sha256" or auswahl == "sha512":
            break
        else:
            print("Du kannst md5, sha1, sha256 oder sha512 auswählen")

    if auswahl == "md5":
        hashval = hashlib.md5()
    if auswahl == "sha1":
        hashval = hashlib.sha1()
    if auswahl == "sha256":
        hashval = hashlib.sha256()
    if auswahl == "sha512":
        hashval = hashlib.sha512()
    
    # Funktion um String Hash zu bestimmen
    def hashcalstr():
        str_hash = input("\nBitte gib dein String ein: ")
        str_hash = str_hash.encode()
        hashval.update(str_hash)
        wert = hashval.hexdigest()
        print(hashval.hexdigest())
        # Hashwert abgleichen
        com_hash = input("\nBitte gib den Hashwert ein mit dem du den Hashwert vergleichen willst: ")
        com_hash = com_hash.lower()
        if wert == com_hash:
            print(wert)
            print(com_hash)
            print("Die Hashwerte sind identisch")
        else:
            print("Die Hashwerte sind nicht identisch")
    
    # Funktion um Datei Hash zu bestimmen      
    def hashcatfile():
        file = input ("\nBitte gib den Pfad zur Datei ein: ")
        # Block größe die pro Lesedurchgang verarbeitet werden soll
        BLOCK_SIZE = 65536
        # Datei öffnen
        with open(file, 'rb') as f:
            # Datei lesen
            fb = f.read(BLOCK_SIZE) 
            # Solange lesen bis noch Size über ist
            while len(fb) > 0:
                hashval.update(fb)
                fb = f.read(BLOCK_SIZE)
        print (hashval.hexdigest())
        wert_file = hashval.hexdigest()
        com_hash = input("\nBitte gib den Hashwert ein mit dem du den Hashwert vergleichen willst: ")
        com_hash = com_hash.lower()
        if wert_file == com_hash:
            print(wert_file)
            print(com_hash)
            print("Die Hashwerte sind identisch")
        else:
            print("Die Hashwerte sind nicht identisch")
    
    # Datei oder str auswählen
    while True:
        str_file = input("\nWillst du einen Hash-Wert aus einer Datei(d) erstellen oder aus einem String(s)? ")
        if str_file == "d" or str_file == "s":
            break

    if str_file == "s": 
        hashcalstr()
        
    if str_file == "d":
        hashcatfile()