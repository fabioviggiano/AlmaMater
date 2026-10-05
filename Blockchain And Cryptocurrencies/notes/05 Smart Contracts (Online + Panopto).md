# Lezione 5 — Smart contracts

[Lezione del 5 ottobre 2026 – Panopto](LINK_PANOPTO)

*Slide di riferimento: [da verificare – Smart contracts]*

---

## Smart contract: inquadramento

Definizione molto generale, il codice per ora non lo vediamo. Presentazione breve, dopodiché si passa ai **token**, l'altro aspetto importante già menzionato nelle lezioni precedenti.

L'idea non è nuova: è stata proposta circa 30 anni fa da **Nick Szabo** (1994). Il concetto di un programma che si comporta come una sorta di contratto era però introdotto in un contesto diverso (non esisteva la blockchain); alcuni aspetti restano comunque attuali.

## Szabo (1994): computerized transaction protocol

<img width="822" height="482" alt="image" src="https://github.com/user-attachments/assets/5b22ad8a-36b3-41a2-b50b-2a47e087a591" />

Uno smart contract è un **protocollo di transazione computerizzato** che esegue i termini di un contratto.

- **Obiettivi generali**
  - soddisfare le condizioni contrattuali comuni: termini di pagamento, garanzie (*liens*), riservatezza, perfino l'*enforcement*
  - **minimizzare le eccezioni**, sia malevole sia accidentali
  - **minimizzare il bisogno di intermediari fidati**
- **Obiettivi economici**: ridurre perdite da frode, costi di arbitrato ed enforcement, e in generale i costi di transazione

Il problema principale resta la fiducia (*trust*): l'idea è spostarla dalla controparte/intermediario al codice, che esegue automaticamente quanto pattuito.

<img width="912" height="538" alt="image" src="https://github.com/user-attachments/assets/3c50f269-c90a-41b0-b069-314500e31351" />

## Smart contract come programmi su blockchain

<img width="857" height="523" alt="image" src="https://github.com/user-attachments/assets/f8f4f252-7089-4f9b-bc03-941e729715ca" />

Oggi: **programmi definiti dall'utente che girano sopra una blockchain**.

- Gli utenti interagiscono con i contratti scambiando **denaro** e **dati** (tramite transazioni)
- Ogni contratto = **codice + storage** (stato persistente)
- Esecuzione e stato sono garantiti dal **consenso decentralizzato**: nessuna parte singola può alterare il risultato

## Flessibilità

<img width="862" height="462" alt="image" src="https://github.com/user-attachments/assets/9ebbd44e-a8b5-4aeb-8d84-c344695fd68c" />

- Uno smart contract può essere scritto in un linguaggio **Turing completo**
  - **Non in Bitcoin** (Script volutamente limitato)
  - **Ethereum** sì
- Può fare *qualsiasi cosa* faccia un normale computer
- **Ma si paga**: il codice viene eseguito in parallelo da **tutti i nodi** della rete → ogni computazione ha un costo (anticipa il concetto di *gas*)

## Applicazioni

<!-- screenshot "Smart Contract Applications" (elenco) da caricare -->

I contratti si possono usare per costruire:

- valute
- derivati finanziari
- sistemi di voto
- organizzazioni decentralizzate (DAO)
- *data feeds* (dati dal mondo esterno → oracoli)
- registri di titoli/proprietà
- ...

<!-- screenshot "Smart contracts – simple to complex" (spettro PwC) da caricare -->

Spettro dal semplice al complesso:

| Livello | Esempio |
|---|---|
| Digital value exchange | invio di bitcoin a un familiare |
| Smart right and obligation | acquisto di uno stream di contenuti digitali |
| Basic smart contract | il locatore blocca da remoto l'appartamento all'inquilino moroso |
| Multiparty smart contract | prestito dal venditore all'acquirente per comprare casa |
| Distributed autonomous business unit | unità aziendale che emette bond, pagamenti monitorati su ledger condiviso |
| Distributed autonomous organization | camion a guida autonoma che fanno consegne P2P e pagano pedaggi/energia |
| Distributed autonomous government | coloni di un'area disabitata che codificano servizi pubblici auto-applicanti |
| Distributed autonomous society | gruppi di coloni che stabiliscono accordi commerciali auto-applicanti |

## Esempio: licenza (contratto legale)

Spunto: Solidity come linguaggio per scrivere smart contract su Ethereum (non visto oggi).

<img width="905" height="618" alt="image" src="https://github.com/user-attachments/assets/2dfbfeaa-4831-4dc9-a947-5493481cc133" />

Licenza per la valutazione di un prodotto, 5 articoli:

1. Il licenziante concede al licenziatario la licenza di valutare il prodotto
2. Vietato pubblicare i risultati senza approvazione preventiva; se pubblica senza approvazione ha **24 h per rimuovere**
3. Vietato pubblicare commenti, a meno che non sia autorizzato a pubblicare i risultati
4. Se è **commissionato** per una valutazione indipendente, ha l'**obbligo** di pubblicare
5. La licenza termina automaticamente in caso di violazione

## Esempio: licenza come macchina a stati

<img width="905" height="566" alt="image" src="https://github.com/user-attachments/assets/a6ebec72-9815-4cdd-bafb-1b6e60b08713" />

Lo stesso contratto tradotto in un automa a stati finiti:

| Stato | Significato |
|---|---|
| 1 | iniziale, nessuna licenza |
| 2 | licenza attiva (può solo usare) |
| 3 | approvazione ottenuta: può usare, pubblicare, commentare, rimuovere |
| 4 | commissionato: obbligo di pubblicare |
| 5 | pubblicato senza approvazione: finestra per rimuovere |
| 6 | **violazione → licenza terminata** (stato assorbente) |

Transizioni principali:

- 1 → 2 *has license*; 1 → 6 se usa/pubblica/commenta senza licenza
- 2 → 3 *has approval*; 2 → 4 *is commissioned*; 2 → 5 *publish*; 2 → 6 *comment*
- 5 → 2 *remove* (entro 24 h); 5 → 6 *no remove* o *comment*; 5 → 4 *is commissioned*
- 4 → 3 *publish*; 4 → 6 *no publish*
- 3 → 4 *is commissioned*

Morale: un contratto legale si può formalizzare come macchina a stati, quindi come codice. Le parti delicate sono quelle legate al **tempo** (24 h, "non ha pubblicato") e agli **eventi esterni** (approvazione, commissione), che il contratto on-chain non osserva da solo.

---

## Punti su cui insiste il Prof.

> L'idea di smart contract non è nuova (Szabo 1994): la novità è eseguirli su un consenso decentralizzato.
> Obiettivo chiave: ridurre il bisogno di intermediari fidati.
> Turing completezza (Ethereum vs Bitcoin) ha un costo: ogni nodo esegue tutto.

## Dubbi da verificare

- [ ] Verificare ordine/associazione dei primi tre screenshot (Szabo vs schema "programs on top of a blockchain")
- [ ] Caricare i due screenshot sulle applicazioni (elenco + spettro PwC)
- [ ] In che punto il Prof. ha introdotto Solidity?
- [ ] Come si gestiscono tempo (24 h) ed eventi esterni in uno smart contract? → oracoli / timestamp del blocco
- [ ] Riferimento slide esatto

---

*Lezione in corso di trascrizione: da completare.*
