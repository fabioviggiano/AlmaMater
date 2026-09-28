# Sistemi Decentralizzati — Libro di Studio

Appunti ragionati del corso di **Sistemi Decentralizzati / Blockchain** del Prof. Ferretti, Laurea Magistrale in Informatica, Università di Bologna.

Ogni capitolo corrisponde a una lezione e incrocia tre fonti: gli appunti presi in aula, le slide del corso e la bibliografia di riferimento.

---

## Indice

| Cap. | Titolo | Lezione | Slide principali | Stato |
|---|---|---|---|---|
| 1 | [Il paradigma della centralizzazione](<2026.09.21 - Lezione 1 - Il paradigma della centralizzazione- Appunti da Panopoto.md>) | 21/09/2026 | 01, 02, 07.a, 08.00, 08 | ✅ |
| 2.1 | [Smart contracts](<2026.09.25 - Lezione 2.1 - Smart Contracts - Appunti da Panopoto.md>) | 25/09/2026 | 02, 04.00 | ✅ |
| 2.2 | [Smart contracts - Some use cases](<2026.09.25 - Lezione 2.2 - Smart Contracts - Somo use cases - Appunti da Panopoto.md>) | 25/09/2026 | 02, 04.00 | ⏳ |
| 3 | [Applicazioni decentralizzate e Smart Transportation](<2026.09.28 - Lezione 3 - Smart Transportation.md>) | 28/09/2026 | 03.00 (Mobi talk) | ⏳ |
| 4 | [Cryptocurrencies: Architetture e modello UTXO vs Account](<2026.10.02 - Lezione 4 - Cryptocurrencies e Modelli di Stato.md>) | 02/10/2026 | 03.01 | ⏳ |
| 5 | [Bitcoin: Transazioni, Scripting e P2P Network](<2026.10.05 - Lezione 5 - Bitcoin Internals.md>) | 05/10/2026 | 03.01, 08 | ⏳ |
| 6 | [Tokenomics e Standard Fungibili (ERC-20)](<2026.10.12 - Lezione 6 - Token ed ERC-20.md>) | 12/10/2026 | 04.01 | ⏳ |
| 7 | [NFT, Crowdfunding (ICO) e Governance (DAO)](<2026.10.16 - Lezione 7 - NFT ICO e DAO.md>) | 16/10/2026 | 04.01 | ⏳ |
| 8 | [Ethereum Architecture: Account, Transazioni e Gas](<2026.10.19 - Lezione 8 - Ethereum e Gas Model.md>) | 19/10/2026 | 05 | ⏳ |
| 9 | [Ethereum Virtual Machine (EVM) e Storage](<2026.10.26 - Lezione 9 - EVM Internals.md>) | 26/10/2026 | 05 | ⏳ |
| 10 | [Sviluppo di Smart Contract: Fondamenti di Solidity](<2026.11.02 - Lezione 10 - Solidity Basics.md>) | 02/11/2026 | 06.01 | ⏳ |
| 11 | [Solidity Avanzato: Pattern architetturali e Remix IDE](<2026.11.06 - Lezione 11 - Solidity Advanced e Remix.md>) | 06/11/2026 | 06.01 | ⏳ |
| 12 | [Decentralized Finance (DeFi): Swap, Liquidity Pool e DEX](<2026.11.09 - Lezione 12 - DeFi e AMM.md>) | 09/11/2026 | 06.00 | ⏳ |
| 13 | [DeFi Protocols: Lending, Lending Pools e Cross-Chain Bridges](<2026.11.13 - Lezione 13 - DeFi Lending e Bridges.md>) | 13/11/2026 | 06.00 | ⏳ |
| 14 | [DeFi Security: Vulnerabilità degli Smart Contract e Attacchi](<2026.11.16 - Lezione 14 - DeFi Security e Vulnerabilita.md>) | 16/11/2026 | 9.1 | ⏳ |
| 15 | [Privacy, Pseudonimato e Tecniche di De-anonimizzazione](<2026.11.20 - Lezione 15 - Privacy e De-anonimizzazione.md>) | 20/11/2026 | 9.1 | ⏳ |
| 16 | [Strumenti Crittografici per DLT: Hash Pointers e Merkle Tree](<2026.11.23 - Lezione 16 - Merkle Tree e Strutture Dati.md>) | 23/11/2026 | 07 | ⏳ |
| 17 | [P2P Overlay e Distributed Hash Tables (DHT)](<2026.11.27 - Lezione 17 - DHT e Routing P2P.md>) | 27/11/2026 | 07.a | ⏳ |
| 18 | [Blockchain Ledger: Struttura del Blocco e Validazione](<2026.11.30 - Lezione 18 - Blockchain Data Structure.md>) | 30/11/2026 | 08 | ⏳ |
| 19 | [Distributed Consensus: Proof of Work (PoW) e Mining Dynamics](<2026.12.04 - Lezione 19 - Consenso PoW e Mining.md>) | 04/12/2026 | 08.00 | ⏳ |
| 20 | [Consenso Alternativo: Proof of Stake (PoS) e DPoS](<2026.12.11 - Lezione 20 - Consenso PoS e DPoS.md>) | 11/12/2026 | 08.00 | ⏳ |
| 21 | [Modelli di Consenso Permissioned (PBFT, PoA, BFT Voting)](<2026.12.14 - Lezione 21 - Consenso Byzantine e Permissioned.md>) | 14/12/2026 | 08.00 | ⏳ |
| 22 | [Riepilogo, Seminari / Discussione Project Work ed Esame](<2026.12.18 - Lezione 22 - Wrap-up e Progetti.md>) | 18/12/2026 | — | ⏳ |
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

## Struttura del repository

```
notes/
├── README.md                                    ← copertina e indice
├── _template-capitolo.md                        ← scheletro per i nuovi capitoli
├── 01 Il paradigma della decentralizzazione.md  ← capitoli ragionati
└── 2026.09.21 - Lezione 1.md                    ← appunti grezzi di lezione
```

Convenzioni per i nomi:
- capitoli: `NN Titolo del capitolo.md`
- appunti grezzi: `AAAA.MM.GG - Lezione N.md`

Nei link ai file con spazi usa le parentesi angolari: `[Titolo](<NN Titolo del capitolo.md>)`.
