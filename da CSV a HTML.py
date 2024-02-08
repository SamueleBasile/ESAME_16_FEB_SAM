def genera_html_da_file(percorso_file):
    # Apre il file in modalità di lettura
    with open(percorso_file, 'r') as file:
        # Legge il contenuto del file
        contenuto_file = file.read()

    # Genera il codice HTML usando il contenuto del file
    codice_html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Generato</title>
    </head>
    <body>
        <div>
            {contenuto_file}
        </div>
    </body>
    </html>
    """

    # Ottiene il percorso per il file HTML
    percorso_html = percorso_file.replace('.csv', '.html')

    # Salva il codice HTML nel file HTML
    with open(percorso_html, 'w') as html_file:
        html_file.write(codice_html)

    return codice_html

# Esempio di utilizzo:
percorso_file = "/home/roberto/Scrivania/Prova GITHUB/dati_sensore.csv"  # Aggiorna con il percorso del tuo file
codice_html = genera_html_da_file(percorso_file)
print(codice_html)
