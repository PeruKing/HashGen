import hashlib
from art import *
from traceback import print_tb

tprint("Hash Generator\nby\nPeruKingo")

while True:
    # Hash Algorithmus in Variable speichern
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()
    sha512_hash = hashlib.sha512()

    # Methode auswählen
    while True:
        auswahl = input("\nWähle ein Hash-Methode aus: ")
        if auswahl == "md5" or auswahl == "sha1" or auswahl == "sha256" or auswahl == "sha512":
            break
        else:
            print("Du kannst md5, sha1, sha256 oder sha512 auswählen")

    # Datei oder str auswählen
    while True:
        str_file = input("\nWillst du einen Hash-Wert aus einer Datei(d) erstellen oder aus einem String(s)? ")
        if str_file == "d" or str_file == "s":
            break
    
    # str Hashwert erstellen   
    if str_file == "s":
        str_hash = input("\nBitte gib dein String ein: ")
        # str in byte encoden
        str_hash = str_hash.encode()
        if auswahl == "md5":
            md5_hash.update(str_hash)
            wert = md5_hash.hexdigest()
            # Hashwert ausgeben
            print(md5_hash.hexdigest())
        if auswahl == "sha1":
            sha1_hash.update(str_hash)
            wert = sha1_hash.hexdigest()
            print(sha1_hash.hexdigest())
        if auswahl == "sha256":
            sha256_hash.update(str_hash)
            wert = sha256_hash.hexdigest()
            print(sha256_hash.hexdigest())
        if auswahl == "sha512":
            sha512_hash.update(str_hash)
            wert = sha512_hash.hexdigest()
            print(sha512_hash.hexdigest())
        
        # Hashwert miteinander vergleichen
        com_hash = input("\nBitte gib den Hashwert ein mit dem du den Hashwert vergleichen willst: ")
        if wert == com_hash:
            print(wert)
            print(com_hash)
            print("Die Hashwerte sind identisch")
        else:
            print("Die Hashwerte sind nicht identisch")
    
    # Datei Hashwert erstellen        
    if str_file == "d":
        file = input ("\nBitte gib den Pfad zur Datei ein: ")
        # Block größe die pro Lesedurchgang verarbeitet werden soll 
        BLOCK_SIZE = 65536
        
        # Datei öffnen
        with open(file, 'rb') as f:
            # Datei lesen
            fb = f.read(BLOCK_SIZE) 
            # Soll die Datei solange lesen bis noch Size über ist
            if auswahl == "md5":
                while len(fb) > 0:
                    md5_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)
                # Hashwert ausgeben
                print (md5_hash.hexdigest())
                wert_file = md5_hash.hexdigest()
            if auswahl == "sha1":
                while len(fb) > 0:
                    sha1_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)
                print (sha1_hash.hexdigest())
                wert_file = sha1_hash.hexdigest()
            if auswahl == "sha256":
                while len(fb) > 0:
                    sha256_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)
                print (sha256_hash.hexdigest())
                wert_file = sha256_hash.hexdigest()
            if auswahl == "sha512":
                while len(fb) > 0:
                    sha512_hash.update(fb)
                    fb = f.read(BLOCK_SIZE)
                print (sha512_hash.hexdigest()) 
                wert_file = sha512_hash.hexdigest()
                
        # Hashwert miteinader vergleichen
        com_hash = input("\nBitte gib den Hashwert ein mit dem du den Hashwert vergleichen willst: ")
        if wert_file == com_hash:
            print(wert_file)
            print(com_hash)
            print("Die Hashwerte sind identisch")
        else:
            print("Die Hashwerte sind nicht identisch")
    





