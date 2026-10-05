# Capitolo 4 — Modelli di stato (UTXO vs account) e Bitcoin

*Lezione 4 (02/10/2026) · Slide "03.01 – Cryptocurrencies": sezione "Taxonomy of Crypto Platforms" (slide 3–13, anticipata a fine della lezione precedente) e prima parte su Bitcoin. [Registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c71434dc-97a7-4bf1-9658-b4d700985bcb)*

> 🚧 **Capitolo in corso.** Copre la lezione fino alla sezione *Wallets* esclusa. Vedi la nota in fondo.

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

</details>

---

## 🚧 Da completare

**La lezione prosegue dalla sezione *Wallets*, al minuto 33:36 della [registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c71434dc-97a7-4bf1-9658-b4d700985bcb).** Restano da integrare wallet, exchange e stablecoin (resto della slide *03.01 – Cryptocurrencies*).

> Nota: nonce, privacy degli UTXO, eUTXO di Cardano, il modello a program/account di Solana, Lightning Network e i dettagli su Cipro e Argentina vengono dalla letteratura generale, non dalle slide.

---

[← Indice](README.md)
