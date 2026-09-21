# Sistemi Decentralizzati — Libro di Studio

Appunti ragionati del corso di **Sistemi Decentralizzati / Blockchain** del Prof. Ferretti, Laurea Magistrale in Informatica, Università di Bologna.

Ogni capitolo corrisponde a una lezione e incrocia tre fonti: gli appunti presi in aula, le slide del corso e la bibliografia di riferimento.

---

## Indice

| Cap. | Titolo | Lezione | Slide principali | Stato |
|---|---|---|---|---|
| 1 | [Il paradigma della decentralizzazione](<01 Il paradigma della decentralizzazione.md>) | 21/09/2026 | 01, 02, 07.a, 08.00, 08 | ✅ |
| 2 | *da scrivere* | | | ⏳ |

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

1. **Fondamenti** — definizioni e concetti chiave.
2. **Architettura** — schemi, modelli, componenti.
3. **Trade-off e attacchi** — costi, limiti, superficie d'attacco.
4. **Esempi e codice** — casi concreti e snippet eseguibili.
5. **Active Recall** — checklist, domande e tracce di risposta.

Solo il Capitolo 1 ha in più una sezione **0. Informazioni sul corso**.

### Legenda dei box

- ⚠️ **Punto da esame / Nota di rigore** — distinzioni sottili o errori tipici.
- 💡 **Punto su cui insiste il Prof. / Il filo del corso** — ciò che Ferretti ripete a lezione e i collegamenti tra capitoli.

I contenuti presi dalla letteratura generale e non dalle slide sono segnalati in fondo a ogni capitolo: vanno verificati prima di citarli all'esame.

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
.
├── README.md                  ← questo file (copertina e indice)
├── _template-capitolo.md      ← scheletro per i nuovi capitoli
└── capitoli/
    └── 01-paradigma-decentralizzazione.md
```

Convenzione per i nomi: `capitoli/NN-titolo-breve.md`.
