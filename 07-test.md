# Verifica pratica - I Love Physical AI

## Domande scritte

Rispondere in modo sintetico ma motivato sul **FILE WORD**.

1. Quali sono le quattro aree principali di Git? Indica dove si trovano le modifiche dopo `git add` e dopo `git commit`.
2. Che cosa aggiorna `git fetch` e `git pull`? Spiega anche perché una **pull request** non è un comando Git e in che modo è collegata al **merge**.
3. Descrivi come una Issue accompagna il lavoro dal branch alla Pull Request, includendo commit, push, review e merge.

## Il progetto

Un'azienda che opera nel settore delle energie rinnovabili installa impianti fotovoltaici. Realizzare un programma Python per registrare gli impianti, i pannelli installati e lo stato dei lavori. La soluzione deve contenere **esattamente due classi**, ciascuna in un modulo separato e un programma dimostrativo (main):

- `pannello.py`: classe `PannelloFotovoltaico`;
- `impianto.py`: classe `ImpiantoSolare`, che contiene una lista di pannelli;
- `main.py`: contiene funzioni per gestire la lista degli impianti, crea i dati di esempio e dimostra le funzionalita.

## Modelli richiesti (features/pannelli-solari)

In `pannello.py`, `PannelloFotovoltaico` rappresenta un pannello installabile:

- `codice: str`, identificativo univoco del pannello;
- `modello: str`, per esempio `"Aurora"` o `"Helios bifacciale"`;
- `potenza_kw: float`, potenza nominale non negativa.

Firma del costruttore: `__init__(self, codice: str, modello: str, potenza_kw: float) -> None`.

In `impianto.py`, `ImpiantoSolare` rappresenta un impianto fotovoltaico:

- `codice: str`, identificativo univoco dell'impianto;
- `modello: str`;
- `localita: str`, per esempio `"Bologna"` o `"Parma"`;
- `potenza_massima_kw: float`, potenza massima ammessa per i pannelli installati;
- `stato: str`, per esempio `"in installazione"`, `"in collaudo"` o `"attivo"`;
- `pannelli: list[PannelloFotovoltaico]`, inizialmente vuota.

Firma del costruttore: `__init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None`.

Implementare questi metodi:

| Metodo | Parametri | Tipo di ritorno e comportamento |
|---|---|---|
| `aggiungi_pannello` | `pannello: PannelloFotovoltaico` | `None`; aggiunge il pannello, rifiuta codici duplicati nell'impianto e rifiuta l'aggiunta se la potenza totale supererebbe il massimo; in questi casi solleva `ValueError` |
| `potenza_pannelli` | nessuno | `float`; restituisce la somma delle potenze dei pannelli installati |
| `cerca_pannello` | `codice: str` | `PannelloFotovoltaico`; restituisce il pannello con quel codice oppure `None` |
| `rimuovi_pannello` | `codice: str` | `PannelloFotovoltaico`; rimuove e restituisce il pannello trovato, oppure restituisce `None` se non esiste |
| `pannelli_sotto_potenza` | `potenza_massima: float` | `list[PannelloFotovoltaico]`; restituisce i pannelli con potenza minore o uguale al valore indicato; **deve usare una list comprehension** |

In `main.py`, gestire la lista degli impianti registrati. Implementare le seguenti funzioni con parametri e tipi di ritorno annotati: **(features/gestione-impianti)**

| Funzione | Parametri | Tipo di ritorno e comportamento |
|---|---|---|
| `registra_impianto` | `impianti: list[ImpiantoSolare]`, `impianto: ImpiantoSolare` | `None`; aggiunge un impianto e solleva `ValueError` se il codice è già presente |
| `cerca_impianto` | `impianti: list[ImpiantoSolare]`, `codice: str` | `ImpiantoSolare`; restituisce l'impianto trovato ignorando maiuscole/minuscole, oppure `None` |
| `riepilogo_impianti` | `nome_azienda: str`, `impianti: list[ImpiantoSolare]` | `None`; stampa gli impianti registrati, il modello, lo stato e la potenza dei pannelli installati |


## Dimostrazione richiesta

Nel programma `main.py`:

- Creare una lista di impianti.
- Registrare almeno quattro impianti.
- Utilizzare almeno tre stati di avanzamento diversi.
- Installare almeno due pannelli per ciascun impianto.
- Utilizzare modelli differenti di pannello nell'insieme degli impianti.
- Stampare il riepilogo degli impianti.
- Dimostrare una ricerca di un impianto esistente e una ricerca senza risultati.
- Dimostrare una ricerca di un pannello senza risultati.
- Provare e gestire:
  - registrazione di un impianto con codice duplicato;
  - aggiunta di un pannello con codice duplicato nello stesso impianto;
  - aggiunta di un pannello che supera la potenza massima.
- Dimostrare la ricerca e la rimozione di un pannello.
- Dimostrare il filtro dei pannelli tramite `pannelli_sotto_potenza()`.

Gli errori devono essere gestiti tramite `try/except`, evitando per quanto possibile l'interruzione del programma.


## Lavoro Git e GitHub

Tutto il progetto deve essere gestito tramite Git e GitHub. Si utilizza `main` come branch principale.
Devono essere creati esattamente due branch di lavoro, nell'ordine indicato:

1. `features/pannelli-solari`
2. `features/gestione-impianti`

Ogni branch deve:

- partire da `main` aggiornato;
- avere una Issue dedicata;
- contenere almeno due commit descrittivi;
- essere pubblicato su GitHub tramite `push`;
- avere una Pull Request verso `main`;
- avere almeno una review;
- essere integrato in `main` dopo l'approvazione.

Per ciascuna PR richiedere la review e integrare dopo approvazione (sia review che approvazione la fate in maniera autonoma in questo caso). 
In ogni descrizione indicare i comandi di verifica e collegare la Issue con `Closes #NUMERO`.

---

# Screenshot da consegnare (sul FILE WORD)

Ogni screenshot deve essere leggibile e mostrare il contesto. Non ritagliare le immagini in modo da nascondere il comando eseguito, il risultato o il nome del branch.

Consegnare URL del repository e il documento con gli screenshots.

## Valutazione (scala 1-10)


| Criterio | Punti | Come si ottengono |
|---|---:|---|
| Modello a due classi e struttura in moduli | 1,5 | Esattamente due classi richieste, responsabilità distinte, import corretti e file organizzati |
| Funzionalità e gestione dei casi limite | 2,0 | Metodi di `ImpiantoSolare` e funzioni di gestione corretti; duplicati, potenza massima e risultati assenti gestiti |
| Tipi e list comprehension | 1,5 | Annotazioni di parametri e ritorni complete; il filtro dei pannelli per potenza usa una list comprehension |
| Dimostrazione ed esecuzione | 1,0 | Dati minimi e condizioni richieste visibili con `python main.py`; output chiaro |
| Git e GitHub | 1,5 | Tre branch corretti, Issue e PR collegate, commit descrittivi, review, merge e aggiornamento di `main` |
| Domande scritte e documentazione | 1,5 | Risposte corrette e motivate; README con istruzioni di avvio |
| **Totale** | **9,0+1=10** | **Il totale corrisponde al voto in decimi** |
