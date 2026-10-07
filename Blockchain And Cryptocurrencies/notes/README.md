# Sistemi Decentralizzati — Libro di Studio

Appunti ragionati del corso di **Sistemi Decentralizzati / Blockchain** del Prof. Ferretti, Laurea Magistrale in Informatica, Università di Bologna.

Ogni capitolo corrisponde a una lezione e incrocia tre fonti: gli appunti presi in aula, le slide del corso e la bibliografia di riferimento.

---

## Indice

### Capitoli ragionati

| Cap. | Titolo | Lezione | Macro tema | Slide principali |
|---|---|---|---|---|
| 1 | [Il paradigma della decentralizzazione](01%20Il%20paradigma%20della%20decentralizzazione.md) | 1 · lun 21/09/2026 | I — Problem statement e preliminari | 01, 02, 07.a, 08 |
| 2 | [DLT, smart contract e casi d'uso](02%20DLT%2C%20smart%20contract%20e%20use%20case.md) | 2 (2.1 + 2.2) · ven 25/09/2026 | I–II — Introduzione e prime applicazioni | 02 |
| 3 | [Smart Transportation: dati personali su DFS e DLT](03%20Smart%20Transportation.md) | 3 · lun 28/09/2026 | II — Applicazioni | 03.00 (Mobi talk) |
| 4 | [Criptovalute: modelli di stato, Bitcoin e stablecoin](04%20Modelli%20di%20stato%20UTXO%20e%20account.md) | 4 · ven 02/10/2026 | III — Criptovalute | 03.01 |
| 5 | [Smart contract e token](05%20Smart%20contract%20e%20token.md) | 5 · lun 05/10/2026 | III–IV — Token e smart contract | 04.00, 04.01 |

Tutti e cinque i capitoli sono nella versione revisionata (formato uniforme, verificati sulle slide; codice Python e Solidity testato). Il 5 copre per intero le slide 04.00 e 04.01, quindi è più lungo del limite di 5 pagine.

**Copertura del programma ufficiale:** P2P e overlay (Cap. 1) · introduzione alle criptovalute (Cap. 4) · decentralizzazione e DLT (Cap. 1–2) · smart contract (Cap. 2, 5). Da trattare: transazioni e scripting, mining, attacchi, anonimato.

> Gli appunti grezzi da Panopto (`AAAA.MM.GG - Lezione N - ... .md`) non sono ancora caricati nel repository: per ora la fonte di verifica dei capitoli sono le slide.

**Note di calendario (ottobre):** 5 *(no presence friday)* · 12 e 15 · 19 *(no presence friday)*.

### Programma indicativo delle prossime lezioni

| Argomento previsto | Slide |
|---|---|
| Ethereum: account, transazioni, gas, EVM | 05 |
| Solidity e Remix | 06.01 |
| DeFi: swap, AMM, lending, bridge | 06.00 |
| DeFi Security | 9.1 |
| Strumenti per DLT, Merkle tree, DHT | 07, 07.a |
| Struttura della blockchain e consenso (PoW, PoS, BFT) | 08, 08.00 |

Titoli e ordine sono indicativi: si aggiunge un capitolo per lezione, con il prossimo numero libero (`06 …`, `07 …`).

---

## Mappa del corso

Il corso segue un approccio **top-down**: dal problema alle applicazioni, fino agli internals e al consenso, che viene studiato per ultimo. I capitoli seguono le lezioni, quindi la corrispondenza con le parti è indicativa.

| Parte | Argomento | Slide |
|---|---|---|
| I | Problem statement e preliminari | 01 – Preliminaries, 02 – Introduction Blockchain |
| II | Applicazioni | 03.00 – Smart Transportation (Mobi talk 2021) |
| III | Criptovalute e token | 03.01 – Cryptocurrencies, 04.01 – Tokens |
| IV | Smart contract | 04.00 – Smart Contracts, 05 – Ethereum, 06.01 – Solidity |
| V | DeFi e sicurezza | 06.00 – DeFi, 9.1 – DeFi Security |
| VI | Strumenti e P2P | 07 – Tools for DLT, 07.a – DHT short intro |
| VII | Internals e consenso | 08 – Blockchain, 08.00 – Consensus short |

---

## Struttura di ogni capitolo

Ogni capitolo sta in **4–5 pagine** e si apre con una scheda: **data**, **macro tema** (la parte del corso) e **slide** di riferimento.

1. **Fondamenti** — definizioni e concetti chiave.
2. **Architettura** — schemi, modelli, componenti.
3. **Trade-off e attacchi** — costi, limiti, superficie d'attacco.
4. **Esempi e codice** — casi concreti e snippet eseguibili (l'esame sarà molto pratico).
5. **Quadro di riepilogo** — tabella dei concetti chiave, **parole chiave**, **domande** con tracce di risposta.

In fondo, un box **Fonti e verifica** separa ciò che viene dalle slide da ciò che viene dalla letteratura.

### Legenda dei box

- ⚠️ **Punto da esame / Nota di rigore** — distinzioni sottili o errori tipici.
- 💡 **Punto su cui insiste il Prof. / Il filo del corso** — ciò che Ferretti ripete a lezione e i collegamenti tra capitoli.

I contenuti presi dalla letteratura generale e non dalle slide sono segnalati nel box finale di ogni capitolo.

---

## Esame

- **Project work** obbligatorio, da 1 a 3 persone.
- **A scelta:** presentazione di un paper durante il corso (prenotazione su Virtuale) **oppure** orale tradizionale.

> ⚠️ **Da verificare.** La scheda ufficiale dell'insegnamento (90748, A.A. 2026/2027) parla di verifica *solo* tramite **prova di progetto**, senza paper né orale. Chiarire con il Prof.

Materiali e comunicazioni: [virtuale.unibo.it](https://virtuale.unibo.it).

## Testo di riferimento

Narayanan, Bonneau, Felten, Miller, Goldfeder, [*Bitcoin and Cryptocurrency Technologies*](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf), Princeton University Press (gratuito).

---

## Struttura della cartella

```
notes/
├── README.md                 ← questa pagina: copertina e indice
├── NN Titolo del capitolo.md ← capitoli ragionati, uno per lezione (01, 02, …)
└── images/                   ← immagini delle slide
```

**Per aggiungere un capitolo:** crea `NN Titolo.md` con la stessa struttura e aggiungi una riga alla tabella *Capitoli ragionati*. Nei link sostituisci gli spazi con `%20` (es. `[Titolo](06%20Token.md)`) così funzionano sia su GitHub sia negli editor.

[↑ Torna al corso](../README.md)
