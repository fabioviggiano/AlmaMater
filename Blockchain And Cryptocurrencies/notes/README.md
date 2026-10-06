# Sistemi Decentralizzati — Libro di Studio

Appunti ragionati del corso di **Sistemi Decentralizzati / Blockchain** del Prof. Ferretti, Laurea Magistrale in Informatica, Università di Bologna.

Ogni capitolo corrisponde a una lezione e incrocia tre fonti: gli appunti presi in aula, le slide del corso e la bibliografia di riferimento.

---

## Indice

### Capitoli ragionati

| Cap. | Titolo | Lezione | Slide principali | Appunti grezzi |
|---|---|---|---|---|
| 1 | [Il paradigma della decentralizzazione](<01 Il paradigma della decentralizzazione.md>) | 1 · 21/09/2026 | 01, 02, 07.a, 08 | [Lezione 1](<2026.09.21 - Lezione 1 - Il paradigma della centralizzazione- Appunti da Panopoto.md>) |
| 2 | [DLT, smart contract e casi d'uso](<02 DLT, smart contract e use case.md>) | 2 (2.1 + 2.2) · 25/09/2026 | 02 | [2.1](<2026.09.25 - Lezione 2.1 - Smart Contracts - Appunti da Panopoto.md>) · [2.2](<2026.09.25 - Lezione 2.2 - Smart Contracts - Somo use cases - Appunti da Panopoto.md>) |
| 3 | [Smart Transportation: dati personali su DFS e DLT](<03 Smart Transportation.md>) | 3 · 28/09/2026 | 03.00 (Mobi talk) | [Lezione 3](<2026.09.28 - Lezione 3 -  Supply Chain e Tracciabilità - Appunti da Panopoto.md>) |
| 4 | [Criptovalute: modelli di stato, Bitcoin e stablecoin](<04 Modelli di stato UTXO e account.md>) | 4 · 02/10/2026 | 03.01 | [Lezione 4](<2026.10.02 - Lezione 4 - Criptocurrencies - Appunti da Panopoto.md>) |
| 5 | Smart Contracts | 5 | 05.10 | [Lezione 5](<2026.10.05 - Lezione 5.md>) |
 
5  (no presence friday)
12 e 15
19 (no presence friday)


### Programma indicativo delle prossime lezioni

| Lezione | Argomento previsto | Slide |
|---|---|---|
| 02/10/2026 | Bitcoin, wallet, exchange e stablecoin | 03.01 |
| — | Token: ERC-20, NFT, ICO, DAO | 04.01 |
| — | Ethereum: account, transazioni, gas, EVM | 05 |
| — | Solidity e Remix | 06.01 |
| — | DeFi: swap, AMM, lending, bridge | 06.00 |
| — | DeFi Security | 9.1 |
| — | Strumenti per DLT, Merkle tree, DHT | 07, 07.a |
| — | Struttura della blockchain e consenso (PoW, PoS, BFT) | 08, 08.00 |

I titoli e le date future sono indicativi: i capitoli si aggiungono man mano, uno per lezione.

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

Materiali e comunicazioni: [virtuale.unibo.it](https://virtuale.unibo.it).

## Testo di riferimento

Narayanan, Bonneau, Felten, Miller, Goldfeder, [*Bitcoin and Cryptocurrency Technologies*](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf), Princeton University Press (gratuito).

---

## Struttura del repository

```
notes/
├── README.md                                   ← copertina e indice
├── NN Titolo del capitolo.md                   ← capitoli ragionati (uno per lezione)
├── AAAA.MM.GG - Lezione N - ... .md            ← appunti grezzi (fonte dei capitoli)
└── images/                                     ← immagini delle slide
```

Nei link ai file con spazi usa le parentesi angolari: `[Titolo](<NN Titolo del capitolo.md>)`.
