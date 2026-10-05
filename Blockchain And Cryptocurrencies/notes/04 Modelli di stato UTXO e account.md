# Capitolo 4 — Modelli di stato (UTXO vs account) e Bitcoin

*Lezione 4 (02/10/2026) · Slide "03.01 – Cryptocurrencies": sezione "Taxonomy of Crypto Platforms" (slide 3–13, anticipata a fine della lezione precedente) e prima parte su Bitcoin. [Registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c71434dc-97a7-4bf1-9658-b4d700985bcb)*

> 🚧 **Capitolo in corso.** Copre la lezione fino al minuto 55:41 (slide *Fiat-Asset Collateralized Currency*). Vedi la nota in fondo.

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 La domanda

Ogni piattaforma crypto deve rappresentare lo **stato globale**: chi possiede quali token e, se ci sono smart contract, quali sono i valori delle loro variabili. Le slide classificano le piattaforme in base a **come** rappresentano questo stato. È la premessa necessaria per capire Bitcoin, che usa il modello UTXO.

### 1.2 Tassonomia (slide 13)

```
                        Crypto platform
               ┌───────────────┴───────────────┐
           UTXO-based                     account-based
               │                    ┌──────────┴──────────┐
        Bitcoin, Cardano        stateful               stateless
                          Ethereum, Avalanche,          Solana
                          Hedera, Tezos, Algorand
```

| Modello | Piattaforme (slide 13) |
|---|---|
| **UTXO-based** | Bitcoin, Cardano |
| **Account-based stateful** | **Ethereum**, Avalanche, Hedera, Tezos, Algorand |
| **Account-based stateless** | Solana |

> 💡 Ethereum è evidenziato in blu nella slide: è il riferimento del modello account-based stateful e sarà la piattaforma usata nelle prossime lezioni (Solidity).

### 1.3 Bitcoin ad alto livello

- **Valuta completamente digitale**: non esistono monete o banconote fisiche. Bitcoin esiste solo come registrazioni sulla blockchain.
- **Nessun governo la emette**: non c'è una banca centrale che stampa moneta o ne controlla l'offerta. Le regole di emissione sono scritte nel protocollo, con un tetto massimo di **21 milioni di BTC**.
- **Nessuna banca gestisce conti e transazioni**: le transazioni passano direttamente da utente a utente (**peer-to-peer**). A validarle è una rete distribuita di nodi e miner, non un intermediario fidato.
- **Nessuno sa chi l'ha inventata**: il whitepaper del 2008 (*"Bitcoin: A Peer-to-Peer Electronic Cash System"*) è firmato **Satoshi Nakamoto**, uno pseudonimo. Non si sa se dietro ci sia una persona o un gruppo.

### 1.4 Storia

- **2008–2009 – Nascita**
  - Fine 2008: pubblicazione del whitepaper.
  - Gennaio 2009: rilascio del software e annuncio di Bitcoin.
- **2009–2011 – Partenza lenta**
  - **Gennaio 2009**: viene creato il **Genesis Block**, il primo blocco della catena, che dà avvio al **mining**. Pochi giorni dopo avviene la **prima transazione**: Satoshi invia BTC a **Hal Finney**, sviluppatore e attivista della crittografia.
  - **Maggio 2010 – Primo acquisto di beni reali**: **Laszlo Hanyecz** (Florida) offre su *Bitcointalk* **10.000 BTC** a chi gli consegna "un paio di pizze". Un utente della West Coast accetta, per circa **25 $ di pizza**. Il **22 maggio** è ricordato come **Bitcoin Pizza Day**: oggi quei BTC varrebbero centinaia di milioni di dollari.
- **2013 – Il prezzo esplode**: Bitcoin esce dalla nicchia e attira media e investitori.

La slide *BTC / Real money* mostra l'andamento del valore nel tempo, senza scendere nei dettagli.

---

## 2. Architettura

### 2.1 Modello UTXO (*Unspent Transaction Output*)

Nel modello UTXO **non esistono conti con un saldo**. Lo stato globale è l'insieme degli output di transazioni passate **non ancora spesi** (**UTXO set**).

**Anatomia di un UTXO** (slide 9). Ogni output di una transazione è una coppia:

- **token**: la quantità (es. `5:T` = 5 unità del token T);
- **condizione di spesa** (*spending condition*, lo **script**): cosa bisogna dimostrare per spenderlo (es. `→p1`: serve la firma corrispondente a p1).

```
tx1
 └── 5:T → p1        ← UTXO: token (5:T) + condizione di spesa (p1)
```

**Come si spende** (slide 10–12). Una nuova transazione:

1. **fa riferimento** a uno o più output precedenti (input);
2. dimostra che sono **ancora non spesi** (altrimenti sarebbe double spending);
3. **soddisfa la condizione di spesa** di ciascuno (es. con la firma di p1);
4. li **consuma interamente** e crea **nuovi output**.

> 💡 **Punto su cui insiste il Prof.** *"In order to spend data/tokens, you have to do previous checks."* Non si "scala" un saldo: si dimostra di avere diritto a un output precedente non speso e lo si consuma.

**Esempio completo delle slide**

| Passo | Consuma | Crea |
|---|---|---|
| `tx1` | — | `5:T→p1` |
| `tx2` | `5:T→p1` | `3:T→p2`, `2:T→p3` |
| `tx3` | `3:T→p2` | `1:T→p4`, `2:T→p5` |
| `tx4` | `2:T→p3`, `2:T→p5` | `4:T→p6` |

Alla fine l'UTXO set contiene solo `1:T→p4` e `4:T→p6`: totale 5, come all'inizio.

- `tx2` mostra lo **split**: un output ne genera due (uno può essere il **resto**, *change*, che torna al mittente).
- `tx4` mostra il **merge**: una transazione può avere **più input**.
- **Conservazione del valore**: la somma degli output non può superare quella degli input; l'eventuale differenza è la **fee** per il miner.

> ⚠️ **Nota di rigore** (sintesi mia). Un output si spende **sempre per intero**: non si possono spendere "2 dei 5 token" di `5:T→p1`. Si consuma tutto l'output e si crea un output di resto. Il "saldo" di un utente non è scritto da nessuna parte: il wallet lo calcola sommando gli UTXO che sa sbloccare.

### 2.2 Modello account-based

Lo stato globale è una **mappa indirizzo → account**. Le transazioni **aggiornano in place** gli account esistenti, invece di consumare e creare output.

**Tipi di account** (slide 4):

- **User account (EOA, *Externally Owned Account*)**: controllato da una coppia di chiavi. È l'unico che può **iniziare** una transazione firmandola (e pagando le fee).
- **Contract account**: contiene **codice** (lo smart contract). Non agisce mai da solo: si attiva quando riceve una chiamata da un EOA o da un altro contratto.

Nelle slide ogni account ha uno **state** (variabili) e un **wallet** (token posseduti, anche di tipi diversi):

- `acct1`: state `x=1, y=7`, wallet `5:T`
- `acct2`: state `x=2, b=false`, wallet `1:T, 3:T'`
- `acct3`: contratto con `pay(a,b,x) { transfer x:T from a to b }`

> ⚠️ **Nota di rigore.** Lo schema delle slide è un **modello astratto**. In Ethereum reale un EOA ha solo saldo e nonce, **senza codice né storage**; le variabili di stato stanno solo nei contract account.

**Transazione di esempio** (slide 5): `acct3.pay(acct1, acct2, 1)`

| Account | Prima | Dopo |
|---|---|---|
| `acct1` | wallet `5:T` | wallet `4:T` |
| `acct2` | wallet `1:T, 3:T'` | wallet `2:T, 3:T'` |
| `acct3` | codice `pay` | invariato |

Le variabili non coinvolte (`x, y`, `x, b`) e il token `T'` restano invariati; nessun account viene creato o distrutto.

> ⚠️ **Nota di rigore.** Nell'esempio chiunque chiami `pay` sposta token da `acct1`. È una semplificazione didattica: in un contratto reale bisogna controllare che chi chiama sia autorizzato (es. `msg.sender == a`). È il primo esempio di bug di controllo degli accessi, che tornerà in *DeFi Security*.

### 2.3 Account-based **stateful** (slide 6–7)

> *"Contract accounts can have code, state, and tokens."*

```
acct3
  state:  z=1
  wallet: 10:T
  code:
    pay(b,x) { if z==0 then abort else transfer x:T from acct3 to b }
    lock()   { if signedBy(alice) z=0 }
```

- **code**: la logica;
- **state**: variabili persistenti (qui il flag `z`);
- **wallet**: token posseduti **dal contratto stesso**.

**Transazione:** `acct3.pay(acct2, 1)` con `z=1` → il contratto trasferisce 1 token dal **proprio** wallet: `acct3` passa da `10:T` a `9:T`, `acct2` da `1:T` a `2:T`.

**Ruolo di `lock()`**: se Alice firma la chiamata, `z` diventa 0 e da quel momento ogni `pay` **abortisce**. È un esempio minimo di contratto che **custodisce fondi** e ha uno **stato che ne cambia il comportamento**, con un'operazione riservata a un utente specifico.

### 2.4 Account-based **stateless** (slide 8)

> *"Only code in contract accounts! No state, no tokens."*

Nel modello stateless il contract account contiene **solo il codice**. Stato e token stanno in **altri account** (di dati o di utenti), che la transazione deve indicare esplicitamente; il codice li legge e li modifica.

- **Esempio: Solana.** I *program* sono privi di stato; i dati vivono in account separati, "posseduti" dal programma, che vengono passati a ogni chiamata.
- **Vantaggio**: dato che ogni transazione dichiara in anticipo quali account tocca, transazioni su account diversi possono essere eseguite **in parallelo**.

> ⚠️ **Correzione rispetto agli appunti.** Negli appunti "stateless" era definito come "i validatori non conservano l'intero stato e le transazioni allegano una prova (witness)". Quello è un concetto diverso (*stateless clients / stateless validation*, un tema di ricerca per Ethereum). Nella tassonomia del corso **stateless significa: il contratto contiene solo codice, senza stato né token propri**.

### 2.5 Bitcoin at a High-Level: la rete

- **Bitcoin è una rete P2P di nodi** (i *client* Bitcoin).
  - Ogni nodo conserva una copia del **ledger** di *tutte* le transazioni.
  - Il ledger è la **blockchain**: distribuito e replicato, senza archivio centrale.
- **Le transazioni vengono trasmesse (broadcast) ai nodi** (flooding sulla rete non strutturata, vedi Capitolo 1, §2.1.7).
  - I nodi **validano** ogni transazione: firma corretta, fondi disponibili, nessun **double spending**. In termini del §2.1: gli input devono essere **UTXO non spesi** e le loro condizioni di spesa devono essere soddisfatte.
  - Le transazioni valide vengono **inserite in un blocco**, aggiunte alla blockchain e **ritrasmesse**.
  - Una transazione è **accettata solo quando compare nella blockchain**, non al semplice invio.
- **Obiettivo: tutte le transazioni sono note e condivise dall'intera rete.**
  - Si raggiunge un **consenso globale** sulla storia del ledger.
  - Tutti i nodi concordano su chi possiede cosa, senza un'autorità centrale.

> 💡 **Collegamento.** "Accettata solo quando compare nella blockchain" va letto insieme alla finalità probabilistica del PoW (Capitolo 1, §1.6): un blocco può ancora essere riorganizzato, per questo si attendono circa 6 conferme (la latenza "1 h" della tabella del Capitolo 2, §1.7).

### 2.6 Wallet

**Bitcoin wallet.**

- **Bitcoin è un protocollo**: vi si accede tramite un'applicazione client in grado di "parlarlo".
- **Il wallet è l'interfaccia utente più comune** verso il sistema Bitcoin. L'analogia della slide: il wallet sta a Bitcoin come il **browser** sta al protocollo **HTTP**.
- Esistono **molte implementazioni** diverse di wallet.

> ⚠️ **Nota di rigore** (sintesi mia). Il wallet **non contiene bitcoin**. I fondi sono UTXO registrati sulla blockchain (§2.1); il wallet custodisce le **chiavi private** che soddisfano le loro condizioni di spesa, calcola il saldo sommando gli UTXO che sa sbloccare e firma le nuove transazioni. Chi ha le chiavi controlla i fondi.

**Tipologie di wallet: Desktop wallet.**

- **Storia**: è stata la **prima** tipologia di wallet Bitcoin.
- **Vantaggi**: molte funzionalità, **autonomia** e opzioni di **controllo** avanzate; pratico da usare. Esempio in slide: **Electrum**.
- **Disponibilità**: limitata al **dispositivo** su cui è installato il software.
  - **Dispositivo perso → chiavi perse → fondi persi.**
- **Sicurezza**: gira su **sistemi operativi general purpose** (Windows, macOS), spesso insicuri o configurati male. Un malware sul computer può rubare le chiavi.

> 💡 **Collegamento** (sintesi mia). La catena "dispositivo perso → fondi persi" è la conseguenza diretta dell'assenza di una TTP (Capitolo 1, §1.2): non esiste una banca a cui chiedere il recupero. Nella pratica la perdita si mitiga con un **backup delle chiavi**, tipicamente una *seed phrase* di 12–24 parole da cui il wallet rigenera tutte le chiavi.

**Tipologie di wallet: Web wallet.**

- Si usa **dal browser** e conserva il wallet dell'utente su un **server di terze parti**.
- È come la **webmail**: dipende interamente dal server di qualcun altro.
- **Comodo**: niente da installare, funziona su più dispositivi.
- **Problemi di sicurezza**: *"what's up with the stolen bitcoins?"*
  - i furti di bitcoin sono avvenuti **tutti dai siti di wallet**;
  - gli hacker entrano nel server, **rubano le chiavi private** e trasferiscono i bitcoin a sé stessi;
  - **non conviene tenere grandi quantità di bitcoin su sistemi di terze parti**.
- Loghi in slide: Coinbase, Electrum, **Mt.Gox**.

> ⚠️ **Nota di rigore** (sintesi mia). Il furto avviene **sul server**, non sulla blockchain: il protocollo non viene violato, perché chi ha la chiave privata è, per il protocollo, il legittimo proprietario. Il web wallet reintroduce proprio la TTP che Bitcoin voleva eliminare, ed è un **honeypot** (Capitolo 1, §2.1.2): tante chiavi in un solo posto. Il caso storico è **Mt.Gox** (2014): circa 850.000 BTC persi, all'epoca il principale exchange al mondo. Electrum in realtà è un desktop wallet, non custodial.

**Altre tipologie: hardware e paper wallet.**

- **Hardware wallet**: dispositivi fisici dedicati, simili a una **chiavetta USB**, che custodiscono le chiavi offline. La chiave privata non esce mai dal dispositivo: le transazioni vengono firmate al suo interno.
- **Paper wallet**: le chiavi (spesso come QR code) sono **stampate su carta**. Completamente offline, quindi immune ai malware, ma vulnerabile a perdita, furto o deterioramento del foglio.

> 💡 **Lettura da esame** (sintesi mia). Hardware e paper wallet sono **cold wallet** (offline); desktop e web wallet sono **hot wallet** (connessi). Il trade-off è sempre comodità contro sicurezza, e custodia propria contro custodia di terzi: *not your keys, not your coins*.

### 2.7 Exchange centralizzati (*Centralized Crypto Exchanges*)

Gli exchange sono **marketplace** dove si comprano e vendono criptovalute, anche contro valute tradizionali. C'è un **intermediario**, che applica **commissioni** sugli scambi.

- **Order book**: gli ordini di acquisto e vendita sono elencati e ordinati per prezzo.
  - Un **matching engine** abbina compratori e venditori al miglior prezzo eseguibile per la quantità richiesta (*lot size*).
  - Il prezzo di un asset dipende dalla **domanda e offerta** rispetto a un altro asset.
- Molti offrono anche **web wallet custodial**: le chiavi le tiene l'exchange.
- 💡 **Punto evidenziato in slide:** le transazioni sull'exchange **di solito non vengono registrate sulla blockchain**. L'exchange tiene un **registro o database centrale** con le operazioni dei suoi utenti.

> ⚠️ **Nota di rigore** (sintesi mia). Comprare bitcoin su un exchange significa avere una **riga nel database dell'exchange**, non un UTXO a proprio nome. Solo con un **prelievo** verso un proprio indirizzo la transazione va on-chain. È un sistema **centralizzato** costruito sopra un sistema decentralizzato, con tutti i rischi di una TTP (insolvenza, hack, blocco dei fondi). È anche il motivo per cui l'exchange è veloce ed economico: non paga fee né attende conferme per ogni scambio interno.

### 2.8 Exchange decentralizzati (*Decentralized Crypto Exchanges*, DEX)

- Le transazioni avvengono **direttamente sulla blockchain**, tramite **smart contract**.
- La slide si ferma qui: *"To look for the details, we need to introduce some concepts, first"*. I dettagli (es. liquidity pool e AMM) arriveranno con la parte su DeFi.

**Centralizzati vs decentralizzati**

| | **Exchange centralizzato (CEX)** | **Exchange decentralizzato (DEX)** |
|---|---|---|
| **Chi gestisce** | Un'azienda intermediaria | Smart contract sulla blockchain |
| **Dove si registrano gli scambi** | Database centrale dell'exchange | On-chain |
| **Custodia delle chiavi** | Dell'exchange (custodial) | Dell'utente (non custodial) |
| **Prezzo** | Order book + matching engine | Definito dalla logica del contratto (dettagli più avanti) |
| **Fiducia** | Nell'exchange (TTP) | Nel codice e nel consenso |
| **Rischi tipici** | Hack del server, insolvenza, blocco dei fondi | Bug nel contratto, fee e latenza on-chain |

> 💡 **Lettura da esame** (sintesi mia). È la distinzione del Capitolo 1 applicata agli scambi: il CEX è un client/server con una TTP, il DEX sostituisce l'intermediario con il protocollo. In cambio paga i costi della blockchain (fee, latenza, codice immutabile).

### 2.9 Non solo Bitcoin: le altre criptovalute

Bitcoin è solo la prima di **moltissime** criptovalute (spesso chiamate *altcoin*). Il Prof. ne mostra tanti esempi. Guardando i prezzi, salta all'occhio che **alcune valgono stabilmente circa 1 (dollaro)**: sono le **stablecoin** (§2.11).

### 2.10 I limiti delle cripto volatili (*Drawbacks of Volatile Cryptos*)

- **La speculazione alimenta la volatilità**: chi compra per rivendere amplifica le oscillazioni di prezzo.
- **Rischio di cambio inutile** (*unnecessary currency risk*). Domanda della slide: *"Can you pay someone salary in Bitcoin?"* Se il valore cambia molto in pochi giorni, né chi paga né chi riceve sa quanto vale davvero lo stipendio.
- **Difficili da usare negli scambi**: la volatilità ostacola **prestiti, derivati, prediction market** e in generale tutti i **contratti che richiedono stabilità del prezzo**.
- **Molti utenti non vogliono speculare**: vogliono solo **conservare denaro su un registro resistente alla censura**, ad esempio per **sottrarsi al sistema bancario** (vedi i casi di Cipro e Argentina, §3.4).

> 💡 **Collegamento** (sintesi mia). È la contraddizione delle "possibilità offerte" del §3.2: rimesse, unbanked e micropagamenti richiedono una moneta stabile, mentre BTC è soprattutto un asset speculativo.

### 2.11 Stablecoin

**Definizione.** Una stablecoin è una criptovaluta progettata per avere un **valore stabile**, agganciato (*peg*) a un riferimento esterno, di solito una valuta tradizionale: **1 stablecoin ≈ 1 USD** (o 1 EUR).

Unisce i vantaggi della blockchain (trasferimento P2P, senza intermediari bancari, resistenza alla censura) a quelli di una moneta stabile (prezzi, stipendi e contratti si possono esprimere senza rischio di cambio).

> 💡 **Punto su cui insiste il Prof.** Le stablecoin sono le criptovalute **davvero utili come servizio sociale**: è qui che le promesse di §3.2 (rimesse, unbanked, pagamenti) diventano praticabili.

#### Tipi di stablecoin (slide *Types of Stablecoins*)

La slide le dispone su un **triangolo**: tre tipi ai vertici, e ogni lato indica la proprietà che i due vertici hanno in comune.

```
                    Fiat/asset-collateralized
                   (Digix, Tether, TrueUSD)
                      ╱                  ╲
          Collateralized              Capital-efficient
                    ╱                      ╲
   Crypto-collateralized ─── Decentralized ─── Non-collateralized
   (MakerDAO, bitUSD)            (Terra)         (Basis, Carbon)
          └──────── algoritmiche (ellisse rossa) ────────┘
```

| Tipo | Su cosa si basa il valore | Esempi in slide |
|---|---|---|
| **Fiat/asset-collateralized** | Riserve in valuta reale (es. USD) o in un bene (es. oro) | Digix, Tether, TrueUSD |
| **Crypto-collateralized** | Garanzie in altre criptovalute | MakerDAO, bitUSD |
| **Non-collateralized** | Nessuna garanzia: il valore è regolato da **algoritmi** | Basis, Carbon |

**I lati del triangolo:**

- **Collateralized** (fiat ↔ crypto): entrambi hanno una **garanzia** dietro ogni token.
- **Capital-efficient** (fiat ↔ non-collateralized): entrambi emettono un token per ogni unità di valore, senza bisogno di **bloccare più capitale** di quello emesso.
- **Decentralized** (crypto ↔ non-collateralized): entrambi vivono **interamente on-chain**, senza un custode centrale.

**Stablecoin algoritmiche.** L'ellisse rossa racchiude le **non-collateralized** e la zona di confine con le crypto-collateralized: sono le **stablecoin algoritmiche**, dette anche **ibride**, in cui il valore è mantenuto da **algoritmi** che regolano l'offerta. **Terra** sta proprio sul lato *Decentralized*, a metà tra i due vertici.

> ⚠️ **Nota di rigore** (sintesi mia).
> - Nessun tipo ha tutte e tre le proprietà: è un altro **trilemma**, simile a quello del Capitolo 1.
> - Le **fiat-collateralized** sono le più stabili, ma reintroducono un emittente centralizzato: può congelare indirizzi e la stabilità dipende dalle sue riserve.
> - Le **crypto-collateralized** sono decentralizzate ma poco efficienti: servono garanzie superiori al valore emesso (*sovra-collateralizzazione*), perché il collaterale è volatile.
> - Le **algoritmiche** sono efficienti e decentralizzate, ma fragili: **Terra (UST)** ha perso il peg ed è collassata nel 2022.
> - Digix in realtà è agganciata all'**oro**: è per questo che il vertice si chiama *fiat/asset*.

#### Fiat-asset collateralized currency

- Ogni token è **garantito da una valuta reale** (es. USD), depositata presso una **banca**.
- Lo schema della slide (animato) parte da **banca** e **utente**. Primo passo: **si depositano USD su un conto bancario** (*Deposit USD to a bank account*).

*(Sezione in corso: lezione sospesa al minuto 55:41, sul primo passo dello schema.)*

---

## 3. Trade-off e implicazioni

### 3.1 UTXO vs account

| Caratteristica | UTXO-based | Account-based |
|---|---|---|
| **Unità di stato** | Output non speso (token + condizione di spesa) | Account (indirizzo + wallet + state + eventuale codice) |
| **Come si spende** | Si referenziano output non spesi e si soddisfano le loro condizioni (*previous checks*) | Una transazione firmata aggiorna i saldi, se sufficienti |
| **Effetto della transazione** | Consuma input interi, crea nuovi output | Modifica in place saldi e variabili |
| **Saldo** | Somma degli UTXO sbloccabili (calcolata dal wallet) | Scritto esplicitamente nell'account |
| **Parallelismo** | Naturale: transazioni su UTXO diversi sono indipendenti | Più difficile: transazioni sullo stesso account sono in conflitto (lo stateless aiuta dichiarando gli account toccati) |
| **Double spending** | Un output si spende una sola volta | Serve un contatore per account (**nonce**) per evitare replay |
| **Privacy** | Migliore: si possono usare indirizzi nuovi per ogni resto | Peggiore: un account accumula tutta la storia |
| **Programmabilità** | Script associati ai singoli output; Bitcoin Script non Turing-completo | Contratti con stato condiviso, tipicamente Turing-completi |
| **Piattaforme** | Bitcoin, Cardano | Ethereum, Avalanche, Hedera, Tezos, Algorand (stateful); Solana (stateless) |

> ⚠️ **Nota** (sintesi mia). Cardano usa un **eUTXO** (*extended UTXO*): gli output possono portare dati e i validatori (in Plutus) sono molto più espressivi di Bitcoin Script. Quindi "UTXO = non programmabile" vale per Bitcoin, non per il modello in generale.

### 3.2 Bitcoin: possibilità offerte

- **Rimesse** (*remittances*): invio di denaro all'estero senza intermediari e con costi ridotti.
- **Bank the unbanked**: servizi finanziari per chi non ha un conto bancario.
- **Micropagamenti**: importi molto piccoli, poco sostenibili con i circuiti tradizionali.

> ⚠️ **Nota di rigore** (sintesi mia). Sono le promesse originarie. Con fee di 1–2 $ e latenza di circa un'ora (Capitolo 2, §1.7), i micropagamenti sulla catena principale non sono praticabili; per questo sono nate soluzioni di livello 2 come Lightning Network.

### 3.3 Bitcoin e governi

**Elusione del controllo dei capitali**: essendo digitale e decentralizzato, Bitcoin rende difficile agli Stati bloccare il flusso di valore in entrata e in uscita dai propri confini.

> ⚠️ **Nota di rigore.** Bitcoin non è "non tracciabile". È **pseudonimo**: tutte le transazioni sono pubbliche e analizzabili, ma gli indirizzi non sono legati direttamente a un'identità. Il punto è che non serve un intermediario autorizzato dallo Stato per spostare valore. È la *censorship resistance* del Capitolo 1 applicata al denaro.

### 3.4 Implicazioni

- Le cripto **non sono un investimento economicamente sicuro**, ma molti le percepiscono come bene rifugio rispetto alle banche.
- Esempi citati: **Argentina** e **Cipro**, dove le crisi bancarie hanno spinto le persone verso Bitcoin *(da verificare)*.

> ⚠️ **Nota** (sintesi mia). A Cipro nel 2013 c'è stato il prelievo forzoso sui depositi (*bail-in*), in concomitanza con la prima impennata di BTC. In Argentina i fattori sono stati inflazione, *corralito* e controlli sui cambi. Da confrontare con quanto detto in aula.

- 💡 **Punto su cui insiste il Prof.:** l'attenzione va spostata dal mercato finanziario al **valore sociale** di Bitcoin. La parte davvero interessante è il protocollo.
- **Impatto energetico**: crescita dei data center e della potenza di calcolo per il mining, con conseguente aumento del consumo di energia negli ultimi anni (vedi i Wh/tx nel Capitolo 2, §1.7).

---

## 4. Esempi e codice

### 4.1 UTXO: riproduzione dell'esempio delle slide

```python
utxo = {}                                   # (txid, indice) -> (importo, proprietario)

def tx(txid, inputs, outputs, firme):
    tot_in = 0
    for ref in inputs:                      # "previous checks"
        assert ref in utxo, f"{ref} speso o inesistente"
        importo, owner = utxo[ref]
        assert owner in firme, f"manca la firma di {owner}"
        tot_in += importo
    assert sum(a for a, _ in outputs) <= tot_in, "output > input"
    for ref in inputs:
        del utxo[ref]                       # spent
    for i, out in enumerate(outputs):
        utxo[(txid, i)] = out               # unspent

tx("tx1", [], [], set()); utxo[("tx1", 0)] = (5, "p1")      # output iniziale (es. coinbase)
tx("tx2", [("tx1", 0)], [(3, "p2"), (2, "p3")], {"p1"})
tx("tx3", [("tx2", 0)], [(1, "p4"), (2, "p5")], {"p2"})
tx("tx4", [("tx2", 1), ("tx3", 1)], [(4, "p6")], {"p3", "p5"})
print(utxo)   # {('tx3', 0): (1, 'p4'), ('tx4', 0): (4, 'p6')}
# tx("tx5", [("tx1", 0)], [(5, "p9")], {"p1"}) -> AssertionError: già speso
```

### 4.2 Account stateful: il contratto `acct3` con `lock()`

```python
state = {
    "acct2": {"wallet": {"T": 1, "T'": 3}},
    "acct3": {"wallet": {"T": 10}, "z": 1},
}

def pay(b, x):
    c = state["acct3"]
    if c["z"] == 0:
        raise RuntimeError("abort")
    assert c["wallet"]["T"] >= x
    c["wallet"]["T"] -= x
    state[b]["wallet"]["T"] += x

def lock(signer):
    if signer == "alice":
        state["acct3"]["z"] = 0

pay("acct2", 1)
print(state["acct3"]["wallet"], state["acct2"]["wallet"])  # {'T': 9} {'T': 2, "T'": 3}
lock("alice")
# pay("acct2", 1) -> RuntimeError: abort
```

---

## 5. Active Recall

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| **Tassonomia** | UTXO (Bitcoin, Cardano) vs account; account stateful (Ethereum, Avalanche, Hedera, Tezos, Algorand) vs stateless (Solana) |
| **UTXO** | Output non speso = token + condizione di spesa (script) |
| **Previous checks** | Per spendere: riferire un output, verificare che sia non speso, soddisfarne la condizione |
| **Spent / unspent** | Gli input vengono consumati per intero; si creano nuovi output (split, merge, resto) |
| **Conservazione** | Output ≤ input; la differenza è la fee |
| **Account-based** | Mappa indirizzo → account; aggiornamenti in place |
| **EOA vs contract account** | L'EOA firma e avvia le transazioni; il contratto reagisce alle chiamate |
| **Stateful** | Il contratto ha codice, stato e token propri (`acct3` con `z` e `lock()`) |
| **Stateless** | Il contratto ha solo codice; stato e token stanno in altri account (Solana) |
| **Trade-off** | UTXO: parallelismo, privacy, semplicità di verifica. Account: programmabilità, saldi espliciti, stato condiviso |
| **Bitcoin** | Moneta digitale, nessun emittente, P2P, tetto di 21 milioni, autore pseudonimo (Satoshi Nakamoto) |
| **Storia** | Whitepaper 2008, Genesis Block 2009, prima tx a Hal Finney, Pizza Day 22/05/2010, boom 2013 |
| **Rete Bitcoin** | P2P, ledger replicato, broadcast, validazione (firma, UTXO non spesi), accettazione solo in blocco, consenso globale |
| **Pseudonimato** | Transazioni pubbliche e analizzabili; indirizzi non legati direttamente all'identità |
| **Valore sociale** | Rimesse, unbanked, micropagamenti, resistenza al controllo dei capitali; il Prof. insiste sul protocollo più che sul mercato |
| **Wallet** | Interfaccia verso il protocollo (come il browser per HTTP); custodisce le chiavi, non i bitcoin |
| **Desktop wallet** | Il primo tipo (es. Electrum): autonomia e controllo, ma legato al dispositivo (perso → fondi persi) e a OS poco sicuri |
| **Web wallet** | Chiavi sul server di terzi (come la webmail): comodo, ma i furti sono avvenuti tutti lì (Mt.Gox) |
| **Hardware / paper wallet** | Cold wallet: chiavi offline su dispositivo dedicato o su carta |
| **Exchange centralizzati** | Order book + matching engine, commissioni, custodia delle chiavi; scambi interni non on-chain ma in un DB centrale |
| **Exchange decentralizzati** | Scambi on-chain tramite smart contract, senza intermediario; l'utente tiene le chiavi |
| **Limiti della volatilità** | Speculazione, rischio di cambio (stipendio in BTC?), difficile per prestiti e contratti; molti vogliono solo un registro anti-censura |
| **Stablecoin** | Valore agganciato a una valuta (≈ 1 USD); per il Prof. le cripto davvero utili come servizio sociale |
| **Tipi di stablecoin** | Fiat/asset, crypto-collateralized, non-collateralized (algoritmiche/ibride); lati: collateralized, capital-efficient, decentralized |

### 5.2 Domande e risposte

1. Descrivi la tassonomia delle piattaforme crypto e colloca Bitcoin, Ethereum, Cardano e Solana.
2. Cos'è un UTXO e da quali due elementi è composto?
3. Cosa significa "previous checks" e perché previene il double spending?
4. Perché nel modello UTXO un output si spende per intero? Come si gestisce il resto?
5. Ricostruisci l'esempio tx1–tx4: quale UTXO set rimane alla fine?
6. Come si calcola il saldo di un utente nel modello UTXO?
7. Che differenza c'è tra EOA e contract account?
8. Nell'esempio `acct3.pay(acct1, acct2, 1)` cosa cambia nello stato? Quale problema di sicurezza ha il codice?
9. Cosa significa che un contract account è stateful? Spiega il ruolo di `z` e `lock()`.
10. Cosa significa stateless nella tassonomia del corso? Perché Solana è in quella categoria?
11. Perché il modello UTXO si presta meglio al parallelismo?
12. Il modello UTXO implica l'assenza di smart contract? (Pensa a Cardano.)
13. Quali sono le quattro caratteristiche di alto livello di Bitcoin?
14. Quando una transazione Bitcoin si considera accettata? Cosa verificano i nodi?
15. Bitcoin è anonimo? Motiva.
16. Quali possibilità offre Bitcoin secondo le slide, e quali limiti pratici hanno?
17. Perché il Prof. insiste sul valore sociale più che sul mercato?
18. Che ruolo ha un wallet rispetto al protocollo Bitcoin? Cosa custodisce davvero?
19. Pro e contro di un desktop wallet.
20. Perché i web wallet sono il punto debole da cui sono stati rubati i bitcoin? Il protocollo è stato violato?
21. Che differenza c'è tra hot e cold wallet? Fai un esempio per tipo.
22. Come funziona un exchange centralizzato? Le transazioni tra utenti finiscono sulla blockchain?
23. Che differenza c'è tra exchange centralizzati e decentralizzati?
24. Quali sono i limiti delle criptovalute volatili secondo la slide?
25. Cos'è una stablecoin e perché il Prof. la considera utile come servizio sociale?
26. Descrivi i tre tipi di stablecoin e le proprietà sui lati del triangolo della slide.

<details>
<summary><b>Tracce di risposta</b></summary>

1. UTXO (Bitcoin, Cardano) vs account; account stateful (Ethereum…) vs stateless (Solana).
2. Un output di una transazione non ancora speso: token + condizione di spesa (script).
3. Per spendere si deve riferire un output precedente, verificare che sia ancora non speso e soddisfarne la condizione; un output speso esce dall'UTXO set e non si può riusare.
4. Gli output sono indivisibili: si consuma tutto e si crea un output di resto verso il mittente.
5. `1:T→p4` e `4:T→p6` (tx4 unisce `2:T→p3` e `2:T→p5`).
6. Sommando gli UTXO la cui condizione di spesa l'utente sa soddisfare; non è scritto da nessuna parte.
7. L'EOA è controllato da chiavi e può avviare transazioni; il contract account contiene codice e si attiva solo se chiamato.
8. acct1 da 5 a 4 T, acct2 da 1 a 2 T, il resto invariato. Manca il controllo che chi chiama sia autorizzato a spendere da acct1.
9. Ha codice, stato e token propri. `pay` trasferisce dal wallet del contratto se `z≠0`; `lock()`, se firmata da Alice, pone `z=0` e blocca i pagamenti.
10. Il contratto contiene solo codice; stato e token stanno in account separati passati alla chiamata. In Solana i programmi non hanno stato proprio.
11. Transazioni che consumano UTXO diversi non hanno dipendenze; negli account più transazioni toccano lo stesso saldo o le stesse variabili.
12. No: Cardano usa l'eUTXO con validatori Plutus molto espressivi; Bitcoin Script invece è volutamente limitato.
13. Completamente digitale; nessun governo la emette (tetto 21 milioni); nessuna banca, transazioni P2P validate da nodi e miner; inventore pseudonimo.
14. Solo quando compare in un blocco della blockchain. I nodi verificano firma, disponibilità dei fondi (input UTXO non spesi) e assenza di double spending. Per sicurezza si attendono circa 6 conferme.
15. No, è pseudonimo: le transazioni sono pubbliche e tracciabili, ma gli indirizzi non sono direttamente legati a un'identità.
16. Rimesse, bank the unbanked, micropagamenti. Limiti: fee e latenza sulla catena principale rendono poco praticabili i micropagamenti (da cui soluzioni di livello 2).
17. Perché l'innovazione sta nel protocollo: trasferire valore senza intermediari e senza poter essere bloccati, non nella speculazione sul prezzo.
18. È il client che "parla" il protocollo, come il browser per HTTP. Custodisce le chiavi private (i fondi sono UTXO sulla blockchain), calcola il saldo e firma le transazioni.
19. Pro: prima tipologia, ricca di funzioni, autonomia e controllo (es. Electrum). Contro: disponibile solo sul dispositivo (perso → chiavi e fondi persi) e gira su OS general purpose spesso insicuri.
20. Le chiavi di molti utenti stanno su un server di terzi (honeypot): gli hacker lo violano, prendono le chiavi e spostano i fondi. Il protocollo non è violato: per Bitcoin chi ha la chiave è il proprietario.
21. Hot = connesso (desktop, web wallet), comodo ma esposto. Cold = offline (hardware, paper wallet), più sicuro ma meno pratico.
22. Order book ordinato per prezzo, matching engine che abbina gli ordini, commissioni. Di solito no: l'exchange registra gli scambi in un database centrale; si va on-chain solo con depositi e prelievi.
23. CEX: intermediario, DB centrale, custodia delle chiavi, fiducia nell'exchange. DEX: scambi on-chain tramite smart contract, l'utente tiene le chiavi, fiducia nel codice e nel consenso.
24. La speculazione alimenta la volatilità; rischio di cambio (non si può pagare uno stipendio in BTC con serenità); prestiti, derivati e contratti richiedono stabilità; molti utenti vogliono solo conservare valore su un registro anti-censura, fuori dal sistema bancario.
25. Una cripto con valore agganciato a una valuta (≈ 1 USD). Toglie il rischio di cambio mantenendo i vantaggi della blockchain, quindi rende davvero praticabili rimesse, pagamenti e accesso per gli unbanked.
26. Tre tipi sul triangolo della slide: fiat/asset-collateralized (Tether, TrueUSD, Digix; fiducia nell'emittente), crypto-collateralized (MakerDAO, bitUSD; crollo del collaterale), non-collateralized/algoritmiche (Basis, Carbon, Terra; perdita del peg, Terra 2022). Lati: collateralized, capital-efficient, decentralized; nessun tipo li ha tutti e tre.

</details>

---

## 🚧 Da completare

**Riprendere dal minuto 55:41**, slide *Fiat-Asset Collateralized Currency* (schema banca–utente, dopo il deposito di USD) ([registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c71434dc-97a7-4bf1-9658-b4d700985bcb)). Restano da integrare il dettaglio sulle stablecoin e il resto della slide *03.01 – Cryptocurrencies*.

> Nota: nonce, privacy degli UTXO, eUTXO di Cardano, il modello a program/account di Solana, Lightning Network, la seed phrase, hot/cold wallet, i dettagli su Mt.Gox, Cipro e Argentina, i dettagli sulle stablecoin (sovra-collateralizzazione, collasso di Terra, Digix legata all'oro) vengono dalla letteratura generale, non dalle slide.

---

[← Indice](README.md)
