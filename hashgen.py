import hashlib
from traceback import print_tb

# Hash Algorithmus in Variable speichern
md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1()
sha256_hash = hashlib.sha256()
sha512_hash = hashlib.sha512()

# Metode auswählen
while True:
    auswahl = input("\nWähle ein Hash-Methode aus: ")
    if auswahl == "md5" or auswahl == "sha1" or auswahl == "sha256" or auswahl == "sha512":
        break
    else:
        print("Du kannst md5, sha1, sha256 oder sha512 auswählen")

# Datei oder str auswhählen
while True:
    str_file = input("\nWillst du ein Hash-Wert aus ein Datei(d) erstellen oder aus einem String(s)? ")
    if str_file == "d" or str_file == "s":
        break
 
# str Hashwert erstellen   
if str_file == "s":
    str_hash = input("\n Bitte gib dein String ein: ")
    # str in byte encoden
    str_hash = str_hash.encode()
    if auswahl == "md5":
        md5_hash.update(str_hash)
        # Hashwert ausgeben
        print(md5_hash.hexdigest())
    if auswahl == "sha1":
        sha1_hash.update(str_hash)
        print(sha1_hash.hexdigest())
    if auswahl == "sha256":
        sha256_hash.update(str_hash)
        print(sha256_hash.hexdigest())
    if auswahl == "sha512":
        sha512_hash.update(str_hash)
        print(sha512_hash.hexdigest())
 
# Datei Hashwert erstellen        
if str_file == "d":
    file = input ("\nBitte gib den Pfad zu Datei ein: ")
    # Block größe die pro lesedurchgang verarbeitet werden soll 
    BLOCK_SIZE = 65536
    
    # Datei öffnen
    with open(file, 'rb') as f:
        # Datei lesen
        fb = f.read(BLOCK_SIZE) 
        # Soll die Datei solange lesen bis das noch Size ist
        if auswahl == "md5":
            while len(fb) > 0:
                md5_hash.update(fb)
                # Nochsten block der Datei lesen
                fb = f.read(BLOCK_SIZE)
            # Hashwert ausgeben
            print (md5_hash.hexdigest()) 
        if auswahl == "sha1":
            while len(fb) > 0:
                sha1_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
            print (sha1_hash.hexdigest()) 
        if auswahl == "sha256":
            while len(fb) > 0:
                sha256_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
            print (sha256_hash.hexdigest()) 
        if auswahl == "sha512":
            while len(fb) > 0:
                sha512_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
            print (sha512_hash.hexdigest()) 
    





