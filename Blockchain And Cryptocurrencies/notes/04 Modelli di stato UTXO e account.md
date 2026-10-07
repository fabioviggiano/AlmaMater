# Capitolo 4 — Criptovalute: modelli di stato, Bitcoin e stablecoin

| | |
|---|---|
| **Data** | Venerdì 02/10/2026 · Lezione 4 (con la tassonomia anticipata a fine lezione 3) |
| **Macro tema** | Parte III — Criptovalute |
| **Slide** | 03.01 – Cryptocurrencies (Taxonomy, Bitcoin, Wallets, Exchanges, Stablecoins, Terra) · [registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c71434dc-97a7-4bf1-9658-b4d700985bcb) |

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Tassonomia delle piattaforme crypto

Ogni piattaforma deve rappresentare lo **stato globale**: chi possiede quali token e, se ci sono contratti, i valori delle loro variabili.

| Modello | Piattaforme (slide 13) |
|---|---|
| **UTXO-based** | Bitcoin, Cardano |
| **Account-based stateful** | **Ethereum**, Avalanche, Hedera, Tezos, Algorand |
| **Account-based stateless** | Solana |

### 1.2 Modello UTXO (*Unspent Transaction Output*)

Non esistono conti: lo stato è l'insieme degli **output non ancora spesi** (UTXO set). Ogni output = **token** (es. `5:T`) + **condizione di spesa** (script, es. `→p1`: serve la firma di p1).

Per spendere (*"you have to do previous checks"*) una transazione: **riferisce** output precedenti, verifica che siano **non spesi**, ne **soddisfa la condizione**, li **consuma per intero** e crea nuovi output.

| Tx | Consuma | Crea |
|---|---|---|
| `tx1` | — | `5:T→p1` |
| `tx2` | `5:T→p1` | `3:T→p2`, `2:T→p3` (**split**, con eventuale resto) |
| `tx3` | `3:T→p2` | `1:T→p4`, `2:T→p5` |
| `tx4` | `2:T→p3`, `2:T→p5` | `4:T→p6` (**merge**: più input) |

UTXO set finale: `1:T→p4`, `4:T→p6` (totale 5). Somma output ≤ somma input; la differenza è la **fee**.

> ⚠️ **Punto da esame.** Un output si spende **sempre per intero**: il resto torna al mittente come nuovo output. Il saldo non è scritto da nessuna parte: il wallet lo calcola sommando gli UTXO che sa sbloccare.

### 1.3 Modello account-based

Lo stato è una **mappa indirizzo → account**; le transazioni aggiornano **in place**.

- **User account (EOA):** controllato da chiavi; è l'unico che **avvia** una transazione firmandola.
- **Contract account:** contiene codice, si attiva solo quando chiamato.

Esempio (slide 5): `acct3.pay(acct1, acct2, 1)` → `acct1` da `5:T` a `4:T`, `acct2` da `1:T` a `2:T`; il resto invariato.

> ⚠️ **Nota di rigore.** Nell'esempio chiunque chiami `pay` sposta token da `acct1`: manca il controllo `msg.sender == a` (primo esempio di bug di access control, tornerà in *DeFi Security*). Le variabili di stato sugli EOA sono una semplificazione del modello astratto: in Ethereum un EOA ha saldo e nonce (da Pectra, maggio 2025, con EIP-7702 può delegare l'esecuzione a codice di un contratto).

**Stateful (slide 6–7):** *"Contract accounts can have code, state, and tokens."*

```
acct3   state: z=1   wallet: 10:T
  pay(b,x) { if z==0 then abort else transfer x:T from acct3 to b }
  lock()   { if signedBy(alice) z=0 }
```

`acct3.pay(acct2, 1)` paga dal **wallet del contratto** (10→9). Se Alice firma `lock()`, `z=0` e ogni `pay` abortisce: un contratto che custodisce fondi e cambia comportamento in base allo stato.

**Stateless (slide 8):** *"Only code in contract accounts! No state, no tokens."* Stato e token stanno in altri account passati esplicitamente alla chiamata (Solana). Poiché ogni tx dichiara gli account che tocca, tx su account diversi girano **in parallelo**.

> ⚠️ **Attenzione.** "Stateless" qui **non** significa *stateless validation* (nodi che non conservano lo stato, tema di ricerca di Ethereum).

---

## 2. Architettura: Bitcoin, wallet, exchange

### 2.1 Bitcoin ad alto livello

- **Fully digital currency**, **no government** che la emette (tetto di 21 milioni nel protocollo), **no banks** (transazioni P2P), **no one knows who invented it** (Satoshi Nakamoto, pseudonimo di persona o gruppo).
- **Caratteristiche (slide):** anonimato e privacy (**chiavi pubbliche come pseudonimi**), **apertura** (basta Internet), **decentralizzazione**, **forte volatilità**.
- **BTC / real money:** il cambio con il dollaro è stato molto volatile; il valore si basa sulla **fiducia in ciò che puoi comprarci**. Ci sono "bitcoin millionaires" che hanno minato nel 2009, e chi ha buttato un computer con una chiave privata legata a oltre 500k $: senza chiave, i fondi sono persi per sempre.
- **Storia:** whitepaper fine 2008, annuncio 2009; gennaio 2009 **Genesis Block** e prima transazione Satoshi → **Hal Finney**; maggio 2010 primo acquisto reale: **Laszlo Hanyecz** paga **10.000 BTC** per pizze da ~25 $ (*Bitcoin Pizza Day*, 22 maggio); **2013** il prezzo esplode.

**La rete.** Ogni nodo ha una copia del ledger (la blockchain). Le transazioni sono **broadcast** ai nodi, che le **validano** (firma, input UTXO non spesi, niente double spending), le inseriscono in un blocco e le ritrasmettono. Una tx è **accettata solo quando compare nella blockchain** (in pratica si attendono ~6 conferme). Obiettivo: **consenso globale** sulla storia.

**Possibilità (slide):** rimesse, *bank the unbanked*, micropagamenti. **Governi:** il contante digitale "non tracciabile" aggira il **controllo dei capitali**; contromisura degli Stati: **scollegare BTC dalle istituzioni finanziarie in valuta fiat**. **Implicazioni:** nelle crisi finanziarie Bitcoin viene percepito come bene rifugio rispetto alle banche (articolo *The Balance* in slide), pur non essendo un investimento sicuro.

**Statistiche di rete (slide, aprile 2025):** consumo energetico e impronta del mining da [Digiconomist](http://digiconomist.net/bitcoin-energy-consumption); il Prof. invita a esplorare i dati live su [blockchain.info](https://blockchain.info/). Ordini di grandezza per transazione nel [Capitolo 2](<02 DLT, smart contract e use case.md>), §1.5.

> ⚠️ **Nota di rigore.** Bitcoin è **pseudonimo**, non anonimo: le transazioni sono pubbliche e analizzabili. E con fee di 1–2 $ e ~1 h di latenza i micropagamenti on-chain non sono praticabili (da qui il livello 2, es. Lightning). Il Prof. insiste sul **valore sociale** del protocollo, non sul mercato.

### 2.2 Wallet

Bitcoin è un **protocollo**; il wallet è l'interfaccia più comune, come il **browser per HTTP**. Il wallet **non contiene bitcoin**: custodisce le **chiavi private** che sbloccano gli UTXO e firma le transazioni.

| Tipo | Caratteristiche (slide) | Rischio |
|---|---|---|
| **Desktop** | Il primo tipo; funzioni, autonomia, controllo (es. Electrum) | Dispositivo perso → chiavi perse → fondi persi; OS general purpose insicuri → chiavi rubate |
| **Mobile** | Il **più diffuso**, su smartphone; simile al desktop | Come il desktop |
| **Web** | Wallet su **server di terzi**, come la webmail; niente da installare | I furti sono avvenuti **tutti dai siti di wallet**: non tenerci grandi somme |
| **Hardware** | Dispositivo dedicato, via USB o NFC | Molto sicuro, adatto a grandi somme |
| **Paper** | Chiavi stampate, *cold storage* a lungo termine | Perdita o deterioramento del foglio |

> 💡 **Lettura da esame.** Hot (desktop, mobile, web) vs **cold** (hardware, paper): comodità contro sicurezza. Il furto da web wallet non viola il protocollo: per Bitcoin chi ha la chiave è il proprietario. Il web wallet è un **honeypot** che reintroduce la TTP (caso **Mt.Gox**, 2014, ~850.000 BTC).

### 2.3 Exchange

Marketplace dove si comprano e vendono cripto, con un **intermediario** che applica **commissioni**.

| | **Centralizzato (CEX)** | **Decentralizzato (DEX)** |
|---|---|---|
| Meccanismo | **Order book** ordinato per prezzo + **matching engine** sul miglior prezzo per il *lot size* | Scambi **on-chain tramite smart contract** (dettagli con la DeFi) |
| Dove si registrano gli scambi | **Database centrale** dell'exchange, di solito non on-chain | Sulla blockchain |
| Chiavi | Spesso custodial (web wallet dell'exchange) | Dell'utente |
| Fiducia / rischi | Nell'exchange: hack, insolvenza, blocco fondi | Nel codice: bug, fee e latenza on-chain |

> ⚠️ **Punto da esame.** Comprare BTC su un CEX significa avere una **riga nel suo DB**, non un UTXO a proprio nome: si va on-chain solo con depositi e prelievi.

---

## 3. Stablecoin e il caso Terra

### 3.1 Perché servono

**Altcoin.** Bitcoin è solo la prima di migliaia di criptovalute (elenco CryptoCompare in slide). Nota del Prof.: le cripto sono **strettamente legate al concetto di token**, introdotto subito dopo ([Capitolo 5](05%20Smart%20contract%20e%20token.md)). Nell'elenco dei prezzi alcune valgono stabilmente ~1 $: sono le stablecoin.

**Drawbacks of volatile cryptos:** la speculazione alimenta la volatilità; rischio di cambio inutile (*"can you pay someone salary in Bitcoin?"*); prestiti, derivati, prediction market e contratti richiedono stabilità; molti utenti vogliono solo **conservare denaro su un registro resistente alla censura**, fuori dal sistema bancario.

**Stablecoin:** cripto con prezzo **agganciato** (*peg*) a un altro asset, es. 1 token ≈ 1 USD. Per il Prof. sono le cripto davvero utili come servizio.

### 3.2 I tre tipi (triangolo della slide)

| Tipo | Garanzia | Esempi | Pro (slide) | Contro (slide) |
|---|---|---|---|---|
| **Fiat/asset-collateralized** | Valuta reale (o oro, Digix) in banca, **1:1** | Tether, TrueUSD, Digix | Il più semplice; **100% stabile** (1 $ in riserva per token, rimborsabile); meno esposto agli hack (collaterale non on-chain) | **Centralizzato** (custode fidato); servono **audit** delle riserve; molto regolato (*legacy payment rails*); conversione in fiat lenta e costosa |
| **Crypto-collateralized** | Altra cripto in uno **smart contract**, **> 100%** | MakerDAO (CDP), bitUSD | Più decentralizzato; liquidazione nel collaterale rapida ed economica; trasparente (ratio ispezionabile) | Meno stabile; **auto-liquidazione** in un crollo (si perde il collaterale); legato a un'altra cripto; capitale inefficiente; complessità massima |
| **Non-collateralized (algoritmica)** | Nessuna: un algoritmo regola l'offerta | Basis, Carbon, Terra | Nessuna garanzia (*no collateral required*: non serve immobilizzare collaterale); il più decentralizzato e indipendente; non legato a fiat o cripto; nessun incentivo a inflazionare o deflazionare (mira alla stabilità) | **Più vulnerabile a un crollo, senza poter liquidare**; complesso; limiti di sicurezza difficili da analizzare; **richiede crescita continua** |

Lati del triangolo: **collateralized** (fiat–crypto), **capital-efficient** (fiat–algoritmica), **decentralized** (crypto–algoritmica). Nessun tipo ha tutte e tre le proprietà.

**Fiat-collateralized: mint, transfer, burn.** Deposito di USD al custode → **mint** dello stesso numero di token; **transfer** on-chain tra utenti senza banca; prelievo → il custode paga e fa **burn** (es. Bob ritira 60 $: `burn(Bob, 60)`, riserva e token in circolazione da 135 a 75). Invariante: **USD in riserva = token in circolazione**. La blockchain garantisce i token, non la riserva: da qui gli audit.

**Collateralization ratio** = valore della garanzia / valore delle stablecoin emesse. *"The more volatile the crypto, the higher this ratio should be."*

| ETH = 1.000 $, emetto 1.000 stablecoin | Garanzia | Ratio | Dopo −20% su ETH |
|---|---|---|---|
| Senza margine | 1 ETH | 100% | 0,80 $ per token → peg perso |
| Sovra-collateralizzata | 1,5 ETH | 150% | 1,20 $ per token → ancora coperta |

**Algoritmiche.** Imitano una **banca centrale**: se il prezzo sale si emette moneta, se scende la si ricompra e distrugge. Lo smart contract usa **oracoli** per monitorare il prezzo sugli exchange.

### 3.3 Caso di studio: Terra (UST) e Luna

- **Terra:** blockchain su **Cosmos SDK + Tendermint**, con oltre 100 progetti nativi (NFT, DeFi, Web3) e più stablecoin: **UST** (USD), TerraEUR, TerraCNY, TerraJPY, TerraKRW, TerraSDR…
- **Luna**, token di staking: regola le stablecoin con mint/burn (**assorbe la volatilità**), paga le ricompense di staking, va bloccato per la **governance**.
- **Meccanismo:** in ogni momento **1 $ di Luna ↔ 1 UST** (si brucia uno, si conia l'altro).
  - **Espansione** (1 UST = 1,01 $): brucio 1 $ di Luna, conio 1 UST, lo vendo a 1,01 → +0,01; l'offerta di UST sale, il prezzo scende.
  - **Contrazione** (1 UST = 0,99 $): compro UST a 0,99, lo converto in 1 $ di Luna → +0,01; l'offerta di UST cala, il prezzo sale.
- **Anchor:** "conto di risparmio DeFi" con **20% APY** sugli UST depositati, pagato dagli interessi dei debitori. La domanda di UST era trainata dall'APY: **Anchor Ponzinomics**, rendimenti artificiali (*"20% of nothing"*, Wired).

**La caduta (maggio 2022).**

| Data | Evento |
|---|---|
| **7 maggio** | > 2 mld $ di UST ritirati da Anchor, centinaia di milioni venduti subito; UST a **0,91 $**. L'arbitraggio (0,90 $ di UST → 1 $ di Luna) era limitato a **100 mln $ al giorno** |
| **12 maggio** | Luna da **82,55 $** a **0,01 $** in una settimana |
| **26 maggio** | UST ≈ **0,086 €**, Luna ≈ **0,000146 €** |
| **Settembre 2022** | UST, ribattezzato *Terra Classic USD*, resta lontanissimo dal peg (grafici CoinMarketCap del 10/09/2022) |

> 💡 **Death spiral.** Ogni UST bruciato conia nuovi Luna: più si vende UST, più Luna entra in circolo e il suo prezzo crolla, quindi servono ancora più Luna per "1 $". Il cuscinetto (Luna) cade insieme a ciò che doveva proteggere, e il tetto giornaliero rende l'arbitraggio troppo lento.

**Attacco speculativo?** Ipotesi (*"some suppose"*): un attaccante accumula UST, ritira 2 mld $ in un colpo per rompere il peg, costringe Terra a vendere le **riserve in BTC**, il panico forza altre vendite e il calo di Bitcoin premia chi era **short** su BTC. È un'ipotesi, non un fatto accertato.

**Il collasso visto da Twitter.** Le ultime slide mostrano un'analisi del **sentiment** dei tweet durante il crollo e la loro **geolocalizzazione**. Anche i tweet "positivi" non erano di fiducia: esprimevano eccitazione per il crollo (sorpresa, ironia), erano pubblicità per attirare follower, o soddisfazione e sollievo per non aver investito. È un esempio di come si studia un evento cripto con i dati social.

---

## 4. Trade-off ed esempi

### 4.1 UTXO vs account

| | UTXO | Account |
|---|---|---|
| Stato | Output non spesi | Saldo e variabili per indirizzo |
| Spesa | Consuma input interi, crea output | Aggiorna in place |
| Double spending / replay | Un output si spende una volta | Serve un **nonce** per account |
| Parallelismo | Naturale | Difficile (lo stateless aiuta) |
| Privacy | Migliore (indirizzi nuovi per il resto) | Peggiore (storia accumulata) |
| Programmabilità | Script limitati (Bitcoin); eUTXO espressivo (Cardano) | Contratti con stato condiviso |

### 4.2 Simulazione UTXO (esempio delle slide)

```python
utxo = {("tx1", 0): (5, "p1")}                 # (txid, indice) -> (importo, owner)

def tx(txid, inputs, outputs, firme):
    tot = 0
    for ref in inputs:                          # previous checks
        assert ref in utxo, f"{ref} speso o inesistente"
        importo, owner = utxo[ref]
        assert owner in firme, f"manca la firma di {owner}"
        tot += importo
    assert sum(a for a, _ in outputs) <= tot, "output > input"
    for ref in inputs: del utxo[ref]
    for i, out in enumerate(outputs): utxo[(txid, i)] = out

tx("tx2", [("tx1", 0)], [(3, "p2"), (2, "p3")], {"p1"})
tx("tx3", [("tx2", 0)], [(1, "p4"), (2, "p5")], {"p2"})
tx("tx4", [("tx2", 1), ("tx3", 1)], [(4, "p6")], {"p3", "p5"})
print(utxo)   # {('tx3', 0): (1, 'p4'), ('tx4', 0): (4, 'p6')}
# tx("tx5", [("tx1", 0)], [(5, "p9")], {"p1"})  -> AssertionError: già speso
```

---

## 5. Quadro di riepilogo

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Tassonomia | UTXO (Bitcoin, Cardano) · account stateful (Ethereum…) · stateless (Solana) |
| UTXO | Token + condizione di spesa; previous checks; spesa per intero, resto, fee |
| Stateful vs stateless | Contratto con codice, stato e token vs solo codice |
| Bitcoin | Digitale, senza emittente né banche, pseudonimo, aperto, volatile; tx accettata solo in blocco |
| Wallet | Interfaccia al protocollo; custodisce chiavi; desktop/mobile/web (hot) vs hardware/paper (cold) |
| CEX vs DEX | Order book e DB centrale vs smart contract on-chain |
| Stablecoin | Fiat (1:1, centralizzata) · crypto (> 100%, ratio) · algoritmica (offerta, oracoli) |
| Terra | 1 $ Luna ↔ 1 UST; Anchor 20% APY; tetto 100 mln $/giorno → death spiral (maggio 2022) |

### 5.2 Parole chiave

`UTXO` · `spending condition` · `previous checks` · `change` · `fee` · `EOA` · `contract account` · `stateful / stateless` · `nonce` · `Genesis Block` · `pseudonimato` · `capital control` · `altcoin` · `hot / cold wallet` · `custodial` · `order book` · `matching engine` · `CEX / DEX` · `peg` · `mint / burn` · `audit delle riserve` · `collateralization ratio` · `CDP` · `stablecoin algoritmica` · `oracolo` · `UST / Luna` · `Anchor` · `arbitraggio` · `death spiral` · `sentiment analysis`

### 5.3 Domande

1. Descrivi la tassonomia e colloca Bitcoin, Ethereum, Cardano e Solana.
2. Cos'è un UTXO e cosa significa "previous checks"? Ricostruisci tx1–tx4.
3. Come si calcola il saldo nel modello UTXO? Perché un output si spende per intero?
4. EOA vs contract account; stateful vs stateless. Quale bug ha `acct3.pay(acct1, acct2, 1)`?
5. Perché il modello UTXO si presta al parallelismo? UTXO implica assenza di smart contract?
6. Quando una transazione Bitcoin è accettata e cosa verificano i nodi? Bitcoin è anonimo?
7. Cosa custodisce davvero un wallet? Confronta i cinque tipi della slide.
8. Le transazioni su un exchange centralizzato finiscono sulla blockchain? Differenze con un DEX.
9. Perché servono le stablecoin? Confronta i tre tipi con pro e contro.
10. Descrivi mint, transfer e burn di una fiat-collateralized e l'invariante che le regge.
11. Cos'è il collateralization ratio e perché deve crescere con la volatilità?
12. Come mantiene il peg Terra? Perché l'arbitraggio non l'ha salvata nel maggio 2022?

<details>
<summary><b>Tracce di risposta</b></summary>

1. UTXO: Bitcoin, Cardano. Account stateful: Ethereum. Stateless: Solana.
2. Output non speso = token + script. Si riferisce un output, si verifica che non sia speso, se ne soddisfa la condizione. Finale: `1:T→p4`, `4:T→p6`.
3. Somma degli UTXO sbloccabili. Gli output sono indivisibili: si consuma tutto e si crea il resto.
4. EOA firma e avvia; il contratto reagisce. Stateful: codice, stato, token; stateless: solo codice. Manca il controllo su chi chiama.
5. Tx su UTXO diversi non hanno dipendenze. No: Cardano (eUTXO) è programmabile.
6. Solo quando è in un blocco; firma, input non spesi, niente double spending. Pseudonimo, non anonimo.
7. Le chiavi private. Vedi tabella §2.2.
8. Di solito no (DB centrale); on-chain solo depositi e prelievi. Il DEX scambia on-chain via smart contract.
9. Volatilità, rischio di cambio, contratti, registro anti-censura. Vedi tabella §3.2.
10. Deposito → mint; transfer on-chain; prelievo → burn. USD in riserva = token in circolazione.
11. Garanzia / emesso; il margine assorbe i cali del collaterale.
12. 1 $ di Luna ↔ 1 UST con arbitraggio. Il tetto di 100 mln $/giorno era troppo basso rispetto a miliardi venduti, e i Luna coniati ne facevano crollare il prezzo: death spiral.

</details>

---

> **Fonti e verifica.** Verificato su 03.01 – Cryptocurrencies e 08 – Blockchain. **Correzioni rispetto alla versione precedente:** completati i contro delle algoritmiche e i pro/contro delle crypto-collateralized (dalle slide); aggiunti mobile wallet, caratteristiche di Bitcoin, oracoli, Cosmos SDK/Tendermint; le stablecoin di Terra in slide sono TerraEUR, TerraCNY ecc. (non "Altered e Soluna"); il grafico di Terra Classic è del 10/09/2022; esempio di arbitraggio allineato alla slide (1,01/0,99). Le immagini delle slide sulle stablecoin sono state tolte per stare nelle 5 pagine. Dalla letteratura: Mt.Gox, Lightning, EIP-7702, eUTXO, nonce, esempio numerico del ratio, death spiral, codice.

[← Indice](README.md)
