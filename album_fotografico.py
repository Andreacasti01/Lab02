def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    from csv import reader
    try:
        filein = open(file_path, "r")
        csv_reader = reader(filein)
        struttura_album={}
        for row in csv_reader:
            #print(row[4])
            if row[4].isdigit():
                if row[4] not in struttura_album:
                    struttura_album[row[4]] = []
                    struttura_album[row[4]].append([row[1], row[2], row[3], row[0]])
                else:
                    struttura_album[row[4]].append([row[1], row[2], row[3], row[0]])
            else:
                continue
        #print(struttura_album)
        return struttura_album
    except FileNotFoundError:
        #print('None')
        return None
    filein.close()


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    import csv
    nuova_riga = [codice, titolo, autore, mese, anno]
    file = open(file_path, "a", newline="")
    for chiave in list(album):
        if anno==int(chiave):
            for i in album[chiave]:
                for ii in i:
                    if codice!=ii[0] and (1<=int(mese)<=12):
                        album[chiave].append([codice,titolo,autore,mese])
                        modifica = csv.writer(file)
                        modifica.writerow(nuova_riga)
                        file.close()
                        return True
                    if codice==ii[0] or not (1<=int(mese)<=12):
                        return None
        if anno!=int(chiave):
            continue
    album[anno]=[]
    album[anno].append([codice,titolo,autore,mese])
    modifica = csv.writer(file)
    modifica.writerow(nuova_riga)
    file.close()
    return True




def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    #print(album)
    for key in album:
        for i in album[key]:
            if codice==i[3]:
                richiesta=[i[3],i[0],i[1],i[2],key]
                s=richiesta[0]+', '+richiesta[1]+', '+richiesta[2]+', '+richiesta[3]+', '+richiesta[4]
                return s
            if codice!=i[3]:
                continue
    return None


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    print(album)
    album_int={}
    for chiave, valore in album.items():
        chiave_int=int(chiave)
        album_int[chiave_int]=valore
    if anno in album_int:
        ris=[]
        for key in album_int.values():
            for i in key:
                ris.append(i[0])
        ris_ordinati = sorted(ris)
        #print(ris)
        #print(ris_ordinati)
        return ris_ordinati
    else:
        return None

def main():
    album={}
    #album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                #rint(album)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue
            #print(album)
            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
