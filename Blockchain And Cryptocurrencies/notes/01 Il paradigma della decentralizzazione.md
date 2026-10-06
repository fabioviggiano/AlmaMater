# Capitolo 1 — Il paradigma della decentralizzazione

| | |
|---|---|
| **Data** | Lunedì 21/09/2026 · Lezione 1 |
| **Macro tema** | Parte I — Problem statement e preliminari |
| **Slide** | 01 – Preliminaries · 02 – Introduction Blockchain (apertura) · 07.a – DHT short intro · 08 – Blockchain (rete P2P di Bitcoin) |

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Distribuito ≠ decentralizzato

Il corso tratta ciò che si vuole **decentralizzare**, *not only distribute*. È la distinzione su cui si regge tutto il resto.

- **Distribuito:** stato e calcolo ripartiti su più nodi per scalabilità e disponibilità. I nodi possono appartenere tutti allo stesso soggetto e fidarsi l'uno dell'altro (es. il database replicato di Google).
- **Decentralizzato:** **nessuna singola entità ha il controllo**. I partecipanti non si fidano tra loro e possono essere pseudonimi, malevoli o soggetti a churn: il problema è di **fiducia**, non solo tecnico.

In breve: la distribuzione riguarda *dove* stanno dati e calcolo, la decentralizzazione *chi* li controlla.

### 1.2 Fiducia senza terza parte

Nel modello classico la fiducia è delegata a una **Trusted Third Party (TTP)**: banca, notaio, piattaforma. Il desiderata delle slide è *"Users are able to build trust without involving a third party"*, con la provocazione: **"possiamo costruire Uber senza Uber, o Airbnb senza Airbnb?"**

**Consensus defines trust.** Senza TTP la fiducia non scompare, **si sposta dall'istituzione al protocollo**: l'algoritmo di consenso stabilisce lo stato "vero" (contenuto e ordine del ledger). Non ci si fida di un nodo, ma del fatto che la maggioranza segua le regole. **Maggioranza di cosa?** In un sistema permissionless contare le identità non ha senso (**Sybil attack**): si contano risorse, cioè potenza di calcolo (PoW) o stake (PoS).

### 1.3 Terminologia di base (*Preliminaries*)

| Termine | Definizione |
|---|---|
| **Scalability** | Mantenere le prestazioni al crescere del carico (orizzontale: più nodi; verticale: macchine più potenti) |
| **Availability** | Probabilità che il sistema sia operativo e raggiungibile quando serve |
| **SPOF** | Componente il cui guasto blocca tutto; può essere tecnico o **amministrativo** (chi può spegnere o censurare) |
| **Bottleneck** | Punto di congestione che limita il throughput complessivo |
| **Churn** | Arrivi e partenze indipendenti di molti peer; difficile da gestire |

> ⚠️ **Punto da esame.** Eliminare lo SPOF *tecnico* è una ragione per **distribuire** (basta replicare, restando sotto un unico gestore). La **decentralizzazione** elimina lo SPOF *di controllo e di fiducia*.

### 1.4 Cryptoeconomics

Le slide definiscono la *cryptoeconomics* come l'incontro di quattro discipline: **crittografia** (transazioni sicure e pseudo-anonime), **sistemi distribuiti** (molti host su Internet), **economia** (criptovalute e smart contract) e **teoria dei giochi** (incentivi basati su razionalità e interesse personale per validare le transazioni: sono i meccanismi di auto-regolazione). Le "economie digitali" risultanti richiedono politiche monetarie, fiscali, di privacy e una governance efficace.

### 1.5 Service Evolution

| Fase | Cosa cambia | Chi detiene dati e fiducia |
|---|---|---|
| **1. Communication** | Internet per comunicare (email, chat) | Provider |
| **2. Web 2.0** | Gli utenti producono contenuti | La piattaforma possiede i contenuti |
| **3. Share economy** | Piattaforme che mettono in contatto offerta e domanda (Uber, Airbnb) | La piattaforma come intermediario |
| **4. Decentralization** | Servizi *blockchain-based* | Protocollo + consenso |

Esempi di fase 4 nelle slide: **Steemit** (social), **Ripple** e **Circle** (pagamenti), **burstIQ** (dati sanitari), **Mediachain** (royalty agli artisti tramite smart contract, acquisita da Spotify nel 2017), **Propy** (registro immobiliare decentralizzato).

> 💡 **Punto su cui insiste il Prof.** *"Are we sure it is a sharing economy? It is rather a matching economy."* Uber non condivide nulla, **abbina** due utenti che vanno in posti vicini. Il matching è centralizzato, quindi chi lo controlla estrae rendita e dati. La fase 4 chiede se il matching possa farlo un protocollo.

### 1.6 Il registro pubblico (*The Public Ledger*)

Ogni nodo della rete P2P mantiene **una copia della stessa catena**; non esiste un DB centrale. Dalla slide: *nodes need to agree on the updates (additions) to the ledger → Consensus*.

1. **Append-only:** il ledger cambia solo per aggiunta (*additions*).
2. **Accordo:** senza autorità, i nodi devono concordare **quali** dati aggiungere e **in quale ordine**.
3. **Consenso:** decide come le transazioni sono **ricevute, ordinate, replicate e registrate in modo permanente** (*received → ordered → replicated → committed*, slide 08.00).

> 💡 **Perché conta l'ordine.** In un double spending una parte della rete vede A→B, un'altra A→C: entrambe valide da sole. Entra nel ledger solo la prima nell'ordine concordato.

> ⚠️ **Nota di rigore.** L'append-only è garantito da **catena di hash** (manomissione *evidente*) + **consenso** (riscrittura *troppo costosa*). In Bitcoin (PoW) i fork temporanei sono normali e la finalità è **probabilistica** (convenzione: ~6 conferme); in PBFT un blocco concordato è **subito finale**. *Il consenso non impedisce i fork, li risolve.*

**Anteprima (slide *How Many Blockchains?*):** *public/private* = chi **legge**; *permissionless/permissioned* = chi **scrive** (accetta aggiornamenti). Vedi [Capitolo 2](<02 DLT, smart contract e use case.md>).

---

## 2. Architettura

### 2.1 Client/server vs peer-to-peer

| Proprietà | Client/Server | Peer-to-Peer |
|---|---|---|
| **Ruoli** | Asimmetrici: il client chiede, il server risponde | Simmetrici: ogni peer è client e server (*servent*) |
| **SPOF** | Il server (anche amministrativo) | Nessun centro critico |
| **Scalabilità** | Il server è il collo di bottiglia | Ogni nuovo peer porta domanda **e** risorse |
| **Fiducia** | Nel gestore | In crittografia e consenso |
| **Punti forti** | Semplice, stato unico, query complesse facili | Robusto, difficile da censurare |
| **Punti deboli** | Censura, disponibilità del server | Churn, discovery, Sybil/Eclipse, consistenza |

Esempio canonico di client/server: **il Web**. Dalla slide sul P2P: *"P2P networks replace centralization and hierarchy with distribution and collaboration. At a philosophical level they replace centralized control with responsibility and freedom."*

> ⚠️ **Punto da esame.** Un server replicato su molti datacenter è **distribuito** ma **logicamente centralizzato**: un solo gestore, una sola fonte di fiducia.

**Problemi del centralizzato** (oltre allo SPOF tecnico):
1. **Information collected by big servers:** privacy e profilazione, *honeypot* (un breach espone tutti), lock-in.
2. **Censorship:** l'esempio è lo shutdown di Internet in **Egitto** (27–28 gennaio 2011, Primavera araba): il traffico verso il Paese crolla quasi a zero in una notte.

> ⚠️ **Sfumatura.** Lo shutdown egiziano è avvenuto a livello di **ISP e routing** (underlay): anche un overlay P2P su Internet sarebbe stato tagliato fuori. Un overlay protegge dalla censura *applicativa*; contro lo spegnimento dell'infrastruttura servono reti mesh indipendenti da Internet (FireChat).

### 2.2 Overlay network

Una rete P2P è una **rete logica a livello applicativo (L7)** sopra Internet; i link dell'overlay non coincidono con la topologia fisica. Aneddoto del Prof. sulla **trasparenza rispetto ai protocolli sottostanti**: Bram Cohen, inventore di BitTorrent, ha raccontato (keynote IEEE P2P 2012) di non sapere come funzionasse TCP mentre lo sviluppava.

### 2.3 Applicazioni P2P e spettro di decentralizzazione

| Gruppo | Esempi | Cosa resta centrale |
|---|---|---|
| **Ibridi** (P2P per efficienza) | Spotify (P2P tra client fino al 2014), Google Talk, SETI@home | Catalogo/login/distribuzione dei task |
| **P2P puri** (condivisione risorse) | BitTorrent, eMule, FireChat (mesh Bluetooth/Wi-Fi, proteste di Hong Kong 2014) | Nulla, ma non c'è accordo su uno stato comune |
| **Fiducia decentralizzata** | OpenBazaar, Bitcoin, Ethereum | Nulla: il P2P è affiancato dal **consenso** |

Solo l'ultimo gruppo è decentralizzazione nel senso pieno del corso.

### 2.4 Tassonomia P2P e confronto quantitativo (slide 07.a)

| Tipo | Idea | Esempio |
|---|---|---|
| Ibrido centralizzato | Indice centrale, trasferimento tra peer | Napster (chiuso per via legale: SPOF amministrativo) |
| Puro non strutturato | Ricerca per *flooding* con TTL | Gnutella 0.4 |
| Super-peer | Alcuni peer fanno da indice | Kazaa, Gnutella 0.6 |
| Strutturato (DHT) | Chiavi e nodi mappati via hash su uno spazio logico | Chord, Kademlia |

| Approccio | Memoria/nodo | Overhead | Query complesse | Falsi negativi evitati | Robustezza |
|---|---|---|---|---|---|
| Server centrale | O(N) | O(1) | ✔ | ✔ | ✘ |
| P2P puro (flooding) | O(1) | O(N²) | ✔ | ✘ (il TTL può non trovare la risorsa) | ✔ |
| DHT | O(log N) | O(log N) | ✘ (solo lookup esatto per chiave) | ✔ | ✔ |

Nessun approccio domina: tabella tipica da esame.

### 2.5 La rete P2P di Bitcoin (slide 08)

- Stack: **TCP/IP → rete P2P → consenso → ledger**.
- Rete **non strutturata**: il wallet invia la transazione a un nodo qualsiasi, che la propaga per **flooding** ai vicini.
- **Nessun leave esplicito:** un nodo non sentito da circa **3 ore** (valore hardcoded nei client) viene dimenticato.
- I nodi possono avere **pool di transazioni diversi** (A→B vs A→C): serve il consenso.
- Dimensione: fino a ~1M IP al mese, ma solo **~10K full node** permanentemente connessi (stima forse datata).

> 💡 **Il filo del corso.** Il P2P risolve la *comunicazione* senza un centro, non l'*accordo*. Il consenso aggiunge l'accordo sopra l'overlay.

### 2.6 Consenso, calcolo, storage

```
                 CONSENSUS  ← definisce la fiducia
          ┌──────────┴──────────┐
     COMPUTATION             STORAGE
 smart contract, off-chain,  DFS (IPFS), data availability
 verifiable computing, oracoli
   APPLICAZIONI: Finance · Identity · Governance · Learning · Sensing
```

- **Oracoli:** portano dati esterni on-chain, ma reintroducono un punto di fiducia.
- **Data availability:** il dato deve essere *ottenibile* da chi vuole verificare, non solo esistere.
- **Pattern ricorrente del Prof.:** dati sul **DFS**, hash e permessi (ACL) su **DLT + smart contract**, sovranità all'utente ([Capitolo 3](<03 Smart Transportation.md>)).

Roadmap **top-down**: problema → applicazioni → cripto → smart contract → internals → **consenso per ultimo** (finché non lo si studia, è una scatola nera affidabile).

---

## 3. Trade-off e attacchi

**Costi della decentralizzazione:** replicazione (throughput basso), latenza di finalità, costi economici (fee, energia PoW, capitale PoS), codice immutabile. Da qui il **trilemma** decentralizzazione–sicurezza–scalabilità (formulazione resa popolare da Buterin).

> ⚠️ **Nota di rigore.** "Il P2P scala con i partecipanti" vale per file sharing e DHT. In una blockchain a replicazione totale ogni nodo valida tutto: più nodi = più resilienza, **non** più throughput.

**Quando non decentralizzare:** serve una DLT solo se (1) più parti scrivono uno stato condiviso, (2) non si fidano tra loro, (3) una TTP non esiste o non è desiderabile. Flowchart completo nel [Capitolo 2](<02 DLT, smart contract e use case.md>).

| Attacco / rischio | Idea |
|---|---|
| **Sybil** | Molte identità controllate da un solo attore |
| **51%** | Chi ha la maggioranza della risorsa riscrive la storia |
| **Eclipse** | Un nodo isolato e circondato da peer malevoli |
| **Oracle manipulation** | Dato esterno falso eseguito fedelmente dal contratto |
| **Data withholding** | Hash pubblicato, dato non disponibile |
| **Centralizzazione di fatto** | Pochi pool o validatori: architetturalmente distribuito, politicamente centralizzato |

---

## 4. Esempi e codice

### 4.1 Ledger append-only con catena di hash

```python
import hashlib, json

def h(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def append(chain, txs):
    prev = h(chain[-1]) if chain else "0" * 64
    chain.append({"prev": prev, "txs": txs})      # unica operazione ammessa

def verify(chain):
    return all(chain[i]["prev"] == h(chain[i-1]) for i in range(1, len(chain)))

ledger = []
for txs in (["genesis"], ["A->B 5"], ["B->C 2"]):
    append(ledger, txs)
print(verify(ledger))          # True
ledger[1]["txs"] = ["A->M 5"]  # riscrittura della storia
print(verify(ledger))          # False
```

Chi riscrive può però **ricalcolare tutti gli hash successivi**: la catena rende la manomissione *evidente*, il consenso (in Bitcoin, rifare il PoW) la rende *impraticabile*.

### 4.2 Quorum BFT: il consenso "definisce" la verità

```python
from collections import Counter

def consensus(votes, f):
    n = len(votes)
    assert n >= 3*f + 1, "troppi nodi bizantini"
    value, count = Counter(votes).most_common(1)[0]
    return value if count >= 2*f + 1 else None

print(consensus(["tx_A"]*5 + ["tx_FAKE"]*2, f=2))   # tx_A
```

Con identità note vale **n ≥ 3f+1**. Nel permissionless n non è noto e le identità costano zero: per questo Bitcoin conta il lavoro, non i voti.

---

## 5. Quadro di riepilogo

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Distribuito vs decentralizzato | *Dove* stanno i dati vs *chi* li controlla |
| Consensus defines trust | La fiducia passa dalla TTP al protocollo; si contano risorse, non identità |
| SPOF tecnico vs di controllo | Il primo si elimina replicando, il secondo solo decentralizzando |
| Cryptoeconomics | Crittografia + sistemi distribuiti + economia + teoria dei giochi |
| Service Evolution | Communication → Web 2.0 → share (*matching*) economy → decentralization |
| Public ledger | Append-only, replicato; consenso su contenuto **e ordine** |
| Finalità | PoW probabilistica (~6 conferme); PBFT immediata |
| Client/server vs P2P | Ruoli asimmetrici e SPOF vs *servent* su overlay con churn |
| Server / flooding / DHT | O(N)/O(1) · O(1)/O(N²) · O(log N)/O(log N) |
| Rete Bitcoin | Non strutturata, flooding, oblio dopo 3 h, ~10K full node |

### 5.2 Parole chiave

`decentralizzazione` · `TTP` · `consensus defines trust` · `Sybil` · `SPOF` · `churn` · `bottleneck` · `cryptoeconomics` · `matching economy` · `append-only` · `finalità probabilistica` · `client/server` · `servent` · `overlay` · `flooding` · `DHT` · `censura` · `underlay` · `oracolo` · `data availability` · `trilemma`

### 5.3 Domande

1. Distribuito vs decentralizzato: fai un esempio di sistema distribuito ma non decentralizzato.
2. Cosa significa *consensus defines trust*? Perché nel permissionless non si contano i nodi?
3. Perché eliminare lo SPOF tecnico non basta?
4. Quali discipline compongono la cryptoeconomics e che ruolo ha la teoria dei giochi?
5. Perché per il Prof. la sharing economy è una *matching economy*?
6. Perché i nodi devono accordarsi anche sull'**ordine** delle transazioni?
7. In Bitcoin un blocco appena aggiunto è definitivo? Confronta con PBFT.
8. Confronta client/server e P2P per ruoli, SPOF, scalabilità e fiducia.
9. Un overlay P2P avrebbe resistito allo shutdown egiziano del 2011?
10. Confronta server, flooding e DHT per memoria, overhead, query complesse e falsi negativi.
11. Come gestisce Bitcoin il churn e la propagazione delle transazioni?
12. Perché una rete P2P da sola non basta a costruire una criptovaluta?

<details>
<summary><b>Tracce di risposta</b></summary>

1. Ripartizione vs assenza di controllo unico; es. DB replicato aziendale.
2. La fiducia passa al protocollo e al quorum onesto; le identità sono gratis (Sybil), quindi si contano hash power o stake.
3. Si può replicare tutto restando sotto un'unica entità: lo SPOF di controllo rimane.
4. Crittografia, sistemi distribuiti, economia, teoria dei giochi; quest'ultima progetta incentivi razionali per validare le transazioni.
5. Uber abbina domanda e offerta; il matcher centrale estrae rendita e dati.
6. Due transazioni in conflitto sono valide singolarmente: vince la prima nell'ordine concordato.
7. No: reorg possibili, finalità probabilistica (~6 conferme). In PBFT è subito finale.
8. Vedi tabella §2.1.
9. No: il taglio era nell'underlay; avrebbe resistito solo una mesh indipendente (FireChat).
10. Vedi tabella §2.4: il flooding con TTL può dare falsi negativi, la DHT non fa query complesse.
11. Flooding ai vicini; nessun leave esplicito, nodi dimenticati dopo ~3 ore.
12. Fornisce comunicazione, non accordo: i pool divergono e permettono il double spending.

</details>

---

> **Fonti e verifica.** Verificato su 01 – Preliminaries, 02, 07.a e 08 – Blockchain. Dalla letteratura (non in slide): esempi Napster/Gnutella/Kazaa/Kademlia, dettagli su Spotify, FireChat e shutdown egiziano, reorg e convenzione delle 6 conferme, trilemma di Buterin, codice. Testo di riferimento: Narayanan et al., *Bitcoin and Cryptocurrency Technologies* (2016). Altri: Nakamoto (2008); Lamport et al., *Byzantine Generals* (1982); Stoica et al., *Chord* (SIGCOMM 2001); Wüst & Gervais, *Do you need a Blockchain?* (2018).

[← Indice](README.md)
