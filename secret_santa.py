import smtplib
import random

def secret_santa():
    print("""
    Server: smtp.gmail.com
    Porta: 587
    Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
    """)

    partecipanti = ["partecipante1", "partecipante2"] #inserire i nomi dei partecipanti
    mail = [
        "partecipante1@gmail.com", "partecipante2@gmail.com" # inserire le mail dei partecipanti
    ]

    # Corrispondenze che richiedono ripetizione
    corrispondenze = {
        "partecipante1": "partecipante1@gmail.com", #inserire le corrispondenze tra nome e email come chiave: valore
        "partecipante2": "partecipante2@gmail.com"
    }

    username = "" #inserire la tua mail Google o quella di chi vuole usare l'applicazione
    password = "" # inserire password generata dal tuo account google (https://www.youtube.com/watch?v=GsXyF5Zb5UY)

    # Rimozione dei partecipanti dalla lista per evitare duplicati
    for persona in mail:
        # Trova la persona corrispondente all'email
        persona_nome = [k for k, v in corrispondenze.items() if v == persona][0]
        
        # Esegui l'estrazione e verifica che non ci sia un abbinamento non valido
        while True:
            estratto = random.choice(partecipanti)
            # Controlla se il nome estratto è valido
            if corrispondenze[persona_nome] != persona or estratto != persona_nome:
                partecipanti.remove(estratto)
                destinatario = persona
                oggetto = "Secret Santa al lampone - OFFICIAL"
                messaggio = f"Ciao! Sono il mitico bot creato da Gabri, tu dovrai fare il regalo aaaaaa...*rullo di tamburi*... {estratto} \n\n RICORDIAMOCI CHE QUEST ANNO I REGALI DOVRANNO ESSERE FATTI A MANO, POTRANNO ESSERE OGGETTI O ANCHE CIBO ECC. BASTA CHE NON SIANO COMPRATIIIIIIII"
                contenuto = f"Subject: {oggetto}\n\n{messaggio}"

                # Connessione al server e invio dell'email
                print("Sto effettuando la connessione col Server...")
                email = smtplib.SMTP("smtp.gmail.com", 587)
                email.ehlo()
                email.starttls()
                email.login(username, password)
                print("Sto inviando...")
                email.sendmail(username, destinatario, contenuto)
                email.quit()
                print("Messaggio Inviato!")
                break
            else:
                print(f"Ripetizione estrazione per {persona_nome} con {persona} perché non è consentito.")
                # Se l'estrazione non è valida, ripeti la selezione.

secret_santa()
