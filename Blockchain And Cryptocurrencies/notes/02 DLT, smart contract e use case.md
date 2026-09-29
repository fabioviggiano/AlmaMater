# Capitolo 2 — DLT, smart contract e casi d'uso

*Lezione 2 (parti 2.1 e 2.2, 25/09/2026) · Slide "02 – Introduction Blockchain": Public Ledger, The Code → Smart Contracts, How Many Blockchains?, DLT/IOTA, Not Only DLTs (IPFS), Hybrid Blockchain, Execution Costs, Performance, Environmental Impact, Use cases (Traceability, Blockchain and Supply Chain), GDPR & Blockchain, Sensitive Data, Hype cycle, "But when I need a blockchain?".*

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Dal ledger pubblico alle sue proprietà

Il capitolo riparte dal *Public Ledger* del [Capitolo 1](<01 Il paradigma della decentralizzazione.md>) (§1.6) e ne esplicita le proprietà, seguendo la sequenza delle slide.

- **Pseudo-anonimato.** Ogni partecipante è identificato da una coppia di chiavi (**S** = chiave segreta, **P** = chiave pubblica). Non serve sapere *chi* sei (*"Chi siete?"*): basta verificare che una firma corrisponda a una chiave pubblica.
- **Ridondanza.** Tutti i nodi mantengono una copia dello stesso **append-only log**.
- **Ridondanza + non manomissibilità** danno tre proprietà: **authenticity** (so chi ha scritto, grazie alla firma), **verifiability** (chiunque può controllare), **immutability** (ciò che è scritto non si cambia).
- **Consenso.** I nodi devono accordarsi sulle aggiunte al ledger (vedi Capitolo 1).

> 💡 **Nota della slide.** Sotto il disegno del ledger il Prof. scrive *"not always a blockchain"*: il registro può avere strutture diverse da una catena lineare (§1.2).

### 1.2 DLT vs blockchain

- **DLT (*Distributed Ledger Technology*)** è la categoria generale: registri condivisi e sincronizzati tra nodi, senza un gestore centrale.
- La **blockchain** è un caso particolare di DLT: i dati sono raggruppati in **blocchi** collegati da hash in una catena lineare.
- **Tutte le blockchain sono DLT, non tutte le DLT sono blockchain.** Esempio del corso: **IOTA**, il cui ledger è un **DAG** (*Tangle*) invece di una catena. Nelle slide IOTA è presentata con: scalabilità, bassi requisiti di risorse, **transazioni zero-fee**, **nessuno smart contract**.

> ⚠️ **Nota di rigore** (sintesi mia). Le proprietà di IOTA indicate nella slide si riferiscono alle versioni storiche del protocollo. IOTA ha cambiato architettura più volte e le versioni recenti supportano smart contract (infatti nella slide *Smart Contract based* IOTA compare tra le piattaforme con smart contract). All'esame conviene citare IOTA come **esempio di DLT a DAG**, specificando che le caratteristiche dipendono dalla versione.

### 1.3 Non solo DLT: i file system decentralizzati (IPFS)

Le DLT oggi si usano insieme a **file system decentralizzati (DFS)**. Esempio: **IPFS** (*InterPlanetary File System*), un protocollo per memorizzare contenuti in un file system P2P distribuito.

- **Content-based addressing**: un file non si identifica con *dove* sta (URL, server) ma con *cosa* contiene. L'identificatore (**CID**) deriva dall'hash del contenuto: se il file cambia, cambia l'indirizzo.
- Da qui il pattern che torna in tutto il corso: **il dato sta sul DFS, l'hash sta sulla DLT** (vedi §2.5 e [Capitolo 3](<03 Smart Transportation.md>)).

### 1.4 Dalle transazioni agli smart contract (*The Code*)

Una transazione non è solo un dato: è **codice**. La slide mostra una transazione come un piccolo programma:

```
transaction t : {
  a = address of <mittente>;
  b = address of <destinatario>;
  amountToTransfer = 2;
  transfer(a, b, amountToTransfer);
}
```

Se nei blocchi posso mettere codice, posso metterci **programmi più complessi**: la blockchain diventa una **piattaforma che offre servizi certificati alle applicazioni**, cioè gli **smart contract**.

Esempio della slide (Solidity):

```solidity
pragma solidity ^0.4.0;
contract SimpleStorage {
    uint storedData;
    function set(uint x) public { storedData = x; }
    function get() public view returns (uint) { return storedData; }
}
```

Caratteristiche chiave dalla slide: accordo (consenso) sull'**esecuzione** di programmi che vivono sulla blockchain; il codice **non può essere modificato** ed è **eseguito automaticamente**.

> 💡 **Legalese vs computer code.** Il Prof. cita Philip Boucher: il codice come legge in sé, *self-contained, self-performed, self-enforced*. È la versione accademica di *"code is law"*.

**Deploy e redeploy.** Una volta pubblicato (*deployed*), il codice di un contratto non si modifica sul posto. Per correggere un bug o aggiungere funzioni:

- si pubblica una **nuova versione a un nuovo indirizzo**, migrando lo stato se serve;
- oppure si usa il pattern **proxy**: un contratto di facciata, con indirizzo stabile, inoltra le chiamate a un contratto di implementazione che può essere sostituito.

> ⚠️ **Nota di rigore.** Il proxy rende il contratto *aggiornabile*, e quindi reintroduce fiducia in chi controlla l'aggiornamento. Immutabilità e aggiornabilità sono in tensione: è un trade-off, non un dettaglio tecnico.

### 1.5 Tassonomia: lettura e scrittura (*How Many Blockchains?*)

Due dimensioni indipendenti:

1. **Accesso in lettura** (*access to the ledger*)
   - **Public**: chiunque può leggere l'intera storia (gli indirizzi sono pseudonimi, ma la lettura è aperta).
   - **Private**: leggono solo i partecipanti autorizzati.
2. **Diritto di modifica** (*right to modify the ledger*, cioè *right to accept updates*)
   - **Permissionless**: chiunque può partecipare alla validazione e proporre blocchi.
   - **Permissioned**: valida solo un insieme autorizzato di nodi.

| | **Public** | **Private** |
|---|---|---|
| **Permissionless** | Bitcoin, Ethereum | **Rara** (lo dice la slide): chi può leggere è limitato, ma chiunque potrebbe validare. Combinazione poco sensata |
| **Permissioned** | Ledger leggibile da tutti, validatori selezionati (es. reti consortili con audit pubblico) | Reti enterprise chiuse (es. Hyperledger Fabric) |

> ⚠️ **Nota** (sintesi mia). La slide segna solo la cella *private/permissionless* come rara; gli esempi nelle altre celle vengono dalla letteratura. Ripple e Stellar sono spesso citati come *public permissioned* (lettura aperta, validatori su liste di fiducia), ma la classificazione è discussa: meglio usarli come esempi con cautela.

### 1.6 Smart contract based vs no smart contract

Dalla slide:

| Smart contract based | No smart contract |
|---|---|
| Ethereum, Cardano, Solana, Polkadot, Avalanche, IOTA, Hyperledger (Fabric, Besu), Algorand, Sui | Bitcoin, Litecoin, Ripple |

- **Bitcoin** ha comunque un linguaggio di script (**Bitcoin Script**), ma è volutamente **non Turing-completo**: serve a esprimere condizioni di spesa, non programmi arbitrari (vedi [Capitolo 4](<04 Modelli di stato UTXO e account.md>)).
- Le piattaforme smart contract eseguono codice deterministico su una macchina virtuale replicata (es. **EVM** di Ethereum con **Solidity**; Solana con programmi tipicamente in **Rust**). Dettagli nelle prossime lezioni.

### 1.7 Metriche di confronto (slide *Execution Costs, Performance, Environmental Impact*)

**Definizioni**

- **Throughput**: transazioni al secondo (tx/s).
- **Latenza**: tempo tra l'invio di una transazione e la sua conferma o finalità; dipende dal block time e dalle conferme richieste.
- **Fee (USD/tx)**: costo pagato ai validatori; varia con congestione e prezzo del token.
- **Impatto ambientale (Wh/tx)**: dipende soprattutto dal **meccanismo di consenso** (PoW molto energivoro, PoS no).

**Valori delle slide** (ordini di grandezza, datati; `*` = stima teorica)

| Piattaforma | Throughput (tx/s) | Latenza | Fee (USD/tx) | Emissioni (Wh/tx) |
|---|---|---|---|---|
| Bitcoin | 3–7 | 1 h | 1–2 | 360·10³ – 3700·10³ |
| Ethereum | 10–100 | > 13 s | 1,5–10 | 18 – 557 |
| Cardano | 17–20 | 2 min | < 0,25 | 12 – 378 |
| Tezos | 180* | 30 h | < 0,01 | 0,36 – 11 |
| Hedera | 400.000* | 10–20 s | 0,0001 | 0,02 – 0,04 |
| Algorand | 6.000 | 4 s | 0,0003 | 0,17 – 5,34 |
| Solana | 4.000 | 1–3 s | 0,0002 | 0,166 |
| Avalanche | 260–7.000 | < 1 s | 0,03 | 4,76 |

*Fonti citate nella slide: Platt et al. (2021); Gallersdörfer et al. (2022).*

> ⚠️ **Correzione rispetto agli appunti.** La vecchia tabella riportava per Ethereum PoS "< 0,1 Wh/tx" e includeva Ripple, Stellar e Hyperledger con valori non presenti nelle slide. I valori corretti da studiare sono quelli sopra: per Ethereum la slide dà **18–557 Wh/tx**, e Bitcoin è a **360–3.700 kWh/tx**, cioè **quattro-cinque ordini di grandezza** sopra le piattaforme PoS. Il passaggio di Ethereum a PoS (*The Merge*, 2022) ha ridotto il consumo complessivo di circa il 99,9%.

> 💡 **Lettura da esame.** Latenza "1 h" per Bitcoin = circa 6 conferme da ~10 minuti (Capitolo 1, §1.6). I numeri marcati `*` sono teorici: il throughput reale è molto più basso. Nessuna piattaforma vince su tutte le metriche: è il trilemma.

---

## 2. Architettura: casi d'uso e pattern

### 2.1 Tracciabilità e supply chain: il problema

In una filiera tradizionale ogni attore (produttore, trasformatore, vettore, dogana, distributore) usa il proprio sistema informativo. Ne derivano:

- **visibilità limitata** ai partner diretti (un passo a monte, uno a valle);
- **registri manomissibili** a posteriori da chi amministra il database;
- **attriti nelle dispute** (legali, doganali, contrattuali), perché ognuno ha la propria versione dei fatti.

Una DLT offre un registro **condiviso, append-only e verificabile**, in cui ogni evento è firmato da chi lo scrive.

### 2.2 Casi reali

- **TradeLens (IBM + Maersk).** Digitalizzazione dei documenti e degli eventi del trasporto container (polizze di carico, sdoganamento, carico e scarico) su un registro consortile *permissioned*. **Chiuso** (annuncio a fine 2022, dismissione nel 2023) per insufficiente adesione degli altri operatori: la tecnologia funzionava, il consorzio no.
- **IBM Food Trust.** Tracciabilità agroalimentare dal campo allo scaffale. Il consumatore scansiona un **QR code** e vede la storia del lotto (origine, lavorazioni, catena del freddo). Nelle slide è l'esempio di **Hybrid Blockchain** (§2.4).
- **Esempi italiani citati in slide:** Carrefour (filiere tracciate), Riseria Campanini ([agrichain](https://agrichain.riseriacampanini.it/bio/)), mantenimento della **catena del freddo** (*cold chain*).
- **Prototipi didattici:**
  - [AgroChain](https://github.com/Kerala-Blockchain-Academy/AgroChain): DApp di supply chain agricola con microfinanza;
  - [Hackinators-Farming-Dapp](https://github.com/ShubhamKarala/Hackinators-Farming-Dapp): prototipo molto essenziale (*"very basic"*, dice la slide) per scambi agricoltore/acquirente.

### 2.3 Il caso guida del Prof.: componenti prodotti in fabbriche diverse

**Scenario.**

- **A** progetta il prodotto;
- **B1, B2, B3** producono i componenti;
- **C** è il vettore che li trasporta;
- **A1** è lo stabilimento di A dove i componenti vengono assemblati.

**Tentativo 1: un unico DB.** Le domande della slide mostrano perché non funziona:

- *Chi lo gestisce?*
- *Come sono sicuro che i dati non vengano manomessi?*
- *Posso accedere anche se sono poco coinvolto con A?*
- *Se cambio partner, come gli revoco l'accesso?*
- *Internamente uso un altro sistema: possiamo passare a quello?*

**Tentativo 2: tanti DB, uno per attore.** Le domande peggiorano: *come leggo gli altri DB? Come so che i dati sono affidabili? Posso fare audit quando voglio?*

**Tentativo 3: la blockchain.**

1. **Chiavi.** Ogni attore X ha una coppia (S<sub>x</sub>, P<sub>x</sub>). Dalla slide: S<sub>a</sub> è *usata da A per scrivere dati* (e garantire che solo A li abbia scritti); P<sub>a</sub> è *usata dagli altri per leggere i dati scritti da A* (e verificare che li abbia scritti A).
2. **A authorizes others.** A, come radice delle autorizzazioni, concede sulla blockchain i permessi di scrittura ad A1, B1, B2, B3, C.
3. **Everyone writes their activities.** Ognuno registra solo le proprie attività, firmandole con la propria chiave.
4. **Even products can write.** Se hanno sufficiente "intelligenza" (capacità di calcolo), anche i prodotti hanno una propria coppia di chiavi (S<sub>i</sub>) e registrano **statistiche, anomalie**, e **notificano attività di manutenzione**.
5. **Revoke permissions.** *In ogni momento A può revocare l'accesso in scrittura a qualcuno* (esempio della slide: il permesso di C viene revocato). È la risposta diretta alla domanda "se cambio partner?".

> ⚠️ **Nota di rigore** (sintesi mia). Firmare con S<sub>x</sub> garantisce **autenticità e non ripudio**. Il ruolo di "radice" di A mostra che la rete è **permissioned** e che A mantiene un potere di governance (concedere e revocare). Il sistema è quindi decentralizzato nella *scrittura* e nella *verifica*, ma non nella *governance* dei permessi.

**Estensione: Digital Product Passport** (sintesi mia, non in slide). Il prodotto finito espone, via QR o NFC, la storia certificata dei componenti: provenienza da B1–B3, trasporto di C, assemblaggio in A1, eventi registrati dal prodotto in esercizio. È la stessa idea del QR di Food Trust applicata alla distinta base (BOM).

> 💡 **Punto del Prof.: Garbage In, Garbage Out.** La blockchain **non certifica che il dato fisico sia vero**: se un fornitore scrive una temperatura falsa, il registro rende immutabile quella falsità. La DLT risolve la **falsificazione a posteriori**, non l'errore a monte. In cambio garantisce **chi** ha scritto cosa (firma, non ripudio), quindi un audit trail per individuare il responsabile. Il punto di contatto tra mondo fisico e ledger è il problema degli **oracoli** (Capitolo 1, §2.2).

### 2.4 Hybrid blockchain

Dalla slide, in sintesi:

- **public + private** blockchain insieme;
- **le prove vanno sul pubblico** (*proofs go public*);
- **i dati restano privati** (*data go private*).

Esempio: **IBM Food Trust**. È lo stesso principio del §2.5: sul ledger condiviso va solo ciò che serve a dimostrare, non il dato.

### 2.5 Blockchain e GDPR

Il **GDPR** (Reg. UE 2016/679) si applica dentro e fuori l'UE a chi tratta dati di persone nell'UE; è in vigore dal 2016 e applicabile, con sanzioni, dal 25 maggio 2018. Nasce pensando a un **modello centralizzato** di gestione dei dati (c'è un titolare del trattamento identificabile).

La slide si concentra su tre diritti:

- **Diritto di accesso** (art. 15);
- **Diritto di rettifica** (art. 16);
- **Diritto alla cancellazione / all'oblio** (art. 17).

> Per completezza (non in slide), gli altri diritti dell'interessato sono: informazione (artt. 13–14), limitazione del trattamento (art. 18), portabilità (art. 20), opposizione (art. 21), tutele sulle decisioni automatizzate e sulla profilazione (art. 22).

**Il conflitto.**

- **Append-only vs art. 17**: un dato scritto in un blocco non si può cancellare.
- **Append-only vs art. 16**: un errore non si corregge sovrascrivendo; si può solo aggiungere una transazione correttiva, e l'originale resta nello storico.
- **Chiavi pubbliche e indirizzi** possono essere **dati personali pseudonimi** se collegabili a una persona (posizione espressa anche dall'EDPB nelle linee guida sulla blockchain).

Conclusione della slide: **need to use off-chain data**.

**La soluzione tipica (slide *Example* e *Sensitive Data*)**

```
[ Dato sensibile ] ──────────────▶ [ Storage off-chain protetto ]  (cancellabile, rettificabile)
        │
        ▼
[ Funzione hash crittografica ]
        │
        ▼
     [ digest ] ─────────────────▶ [ Blocco sulla blockchain ]     (prova di esistenza e integrità)
```

1. **Dati sensibili off-chain**, in uno storage protetto (cifratura, controllo accessi). Se l'interessato chiede la cancellazione, il dato si elimina lì.
2. **Sul ledger solo il digest** (hash): prova che il dato esisteva in quella forma a quel momento (*proof of existence*) e permette di verificarne l'integrità, senza esporlo.
3. **Lo smart contract controlla l'accesso** ai dati off-chain:
   - **fornisce le chiavi** per decifrarli agli autorizzati;
   - **concede e revoca** l'accesso;
   - **registra ogni operazione → accountability**.

> ⚠️ **Nota di rigore** (sintesi mia). Cancellare il dato off-chain **non** rende automaticamente anonimo il digest rimasto on-chain:
> - se il dato ha poca entropia (un codice fiscale, una data di nascita), l'hash si può **invertire per forza bruta** provando tutti i valori possibili. Per questo si usa un hash con **salt** o un *commitment*, e si cancella anche il salt;
> - dal punto di vista giuridico, il fatto che un hash sia ancora "dato personale" è **discusso**: la posizione prudente è trattarlo come dato pseudonimo.
>
> Alternativa diffusa: cifrare il dato e, per "cancellarlo", distruggere la chiave (*crypto-shredding*).

### 2.6 Blockchain Hype Cycle

La slide usa il **Gartner Hype Cycle** (visibilità nel tempo):

```
VISIBILITÀ
  ▲        Peak of Inflated Expectations
  │            ╭──╮
  │           ╱    ╲                              Plateau of Productivity
  │          ╱      ╲                         ╭──────────────────────
  │         ╱        ╲                    ╭──╯
  │        ╱          ╲   Slope of    ╭──╯
  │       ╱            ╲ Enlightenment
  │      ╱              ╰──╮      ╭──╯
  │     ╱         Trough of ╰────╯
  │    ╱         Disillusionment
  └──┴──────────────────────────────────────────────────────▶ TEMPO
   Technology Trigger
```

- **Technology Trigger**: Bitcoin (2009), poi Ethereum e gli smart contract.
- **Peak of Inflated Expectations**: "blockchain per tutto"; nascono molti progetti spinti dal clamore.
- **Trough of Disillusionment**: emergono costi, scalabilità limitata, conflitti con il GDPR, difficoltà a far collaborare concorrenti. Esempio: la chiusura di TradeLens.
- **Slope of Enlightenment**: si capisce dove la blockchain serve davvero: non sostituisce i database, fa da strato di **certificazione e coordinamento** tra parti che non si fidano.
- **Plateau of Productivity**: architetture ibride on-chain/off-chain, usate in modo pragmatico.

### 2.7 Quando serve davvero una blockchain? (flowchart)

Il flowchart della slide riprende Wüst & Gervais (*Do you need a Blockchain?*, 2018), con l'aggiunta del ramo **Auditing**.

```
Serve uno store di dati condiviso e consistente? ── NO ──▶ DB
        │ SÌ
        ▼
Più di un'entità contribuisce ai dati? ── NO ──▶ DB   (ma se serve AUDITING → si prosegue)
        │ SÌ
        ▼
Esiste una terza parte fidata (TTP)? ── SÌ ──▶ DB
        │ NO
        ▼
Gli scrittori sono tutti noti? ── NO ──▶ PERMISSIONLESS blockchain
        │ SÌ
        ▼
Gli scrittori sono tutti fidati? ── SÌ ──▶ DB
        │ NO
        ▼
Serve verificabilità pubblica (public auditing)?
        ├── NO ──▶ PRIVATE PERMISSIONED blockchain
        └── SÌ ──▶ PUBLIC PERMISSIONED blockchain
```

**I passaggi in parole.**

1. **Store condiviso e consistente?** Se no, basta un DB.
2. **Più entità scrivono?** Se ne scrive una sola non c'è contesa: DB. Eccezione (ramo *Auditing*): se terzi devono poter **verificare** i dati di un singolo scrittore, può servire comunque una DLT come strato di certificazione.
3. **Esiste una TTP accettata da tutti?** Se sì, le si affida un DB centralizzato: più economico e veloce.
4. **Scrittori noti?** Se no (chiunque deve poter scrivere): **permissionless**.
5. **Scrittori fidati?** Se sono noti e si fidano tra loro: basta un DB condiviso.
6. **Serve audit pubblico?** Se no: **private permissioned** (es. consorzio di filiera chiuso, Hyperledger Fabric). Se sì: **public permissioned** (scrivono solo gli autorizzati, ma chiunque può verificare).

> ⚠️ **Correzione rispetto agli appunti.** IBM Food Trust era citato come esempio di *public permissioned*. Nelle slide è invece l'esempio di **hybrid blockchain**: il ledger è permissioned (su Hyperledger Fabric) e il consumatore non legge il ledger direttamente, ma vede i dati tramite l'app. Come esempio di public permissioned è più corretto uno scenario con lettura aperta a tutti e validatori selezionati.

### 2.8 Architettura di una DApp di filiera

*Sezione troncata negli appunti originali: completata da me.*

1. **Front-end**: app web/mobile, terminali di fabbrica, lettori QR/RFID/NFC per inserire e consultare gli eventi.
2. **Middleware e gateway**: collegano ERP aziendali e sensori IoT (temperatura, GPS) alla rete tramite API e nodi RPC; qui stanno anche gli **oracoli**.
3. **Smart contract**: codificano le regole (chi può scrivere quali eventi, permessi, revoche) e sono il back-end "autoritativo".
4. **Storage off-chain**: documenti e dati sensibili su DB o DFS, con il solo hash on-chain (§2.5).

---

## 3. Trade-off e attacchi

| Rischio / limite | Spiegazione | Mitigazione tipica |
|---|---|---|
| **Garbage In, Garbage Out** | Il ledger rende immutabile anche un dato falso | Firme, audit trail, sensori certificati, oracoli affidabili |
| **Conflitto con il GDPR** | Append-only vs cancellazione e rettifica | Dati off-chain, hash salati, crypto-shredding |
| **Hash invertibili** | Hash di dati a bassa entropia forzabili con brute force | Salt / commitment |
| **Governance centralizzata** | In una rete permissioned chi concede i permessi (A) ha potere di controllo | Governance consortile, regole on-chain |
| **Adesione del consorzio** | Senza partecipanti la rete non ha valore (TradeLens) | Incentivi, neutralità dell'operatore |
| **Aggiornabilità dei contratti** | Il proxy reintroduce fiducia in chi aggiorna | Timelock, governance multi-firma |
| **Costi e prestazioni** | Fee, latenza, energia (tabelle §1.7) | Scegliere la piattaforma in base al caso; architetture ibride |
| **Hype** | Usare la blockchain dove basta un DB | Flowchart §2.7 |

---

## 4. Esempi e codice

### 4.1 Notarizzazione di un dato sensibile (hash salato)

```python
import hashlib, os

def commit(dato: bytes):
    salt = os.urandom(16)                        # conservato off-chain insieme al dato
    digest = hashlib.sha256(salt + dato).hexdigest()
    return salt, digest                          # il digest va on-chain

def verifica(dato: bytes, salt: bytes, digest_onchain: str) -> bool:
    return hashlib.sha256(salt + dato).hexdigest() == digest_onchain

salt, d = commit(b"lotto 42: 4 gradi C")
print(verifica(b"lotto 42: 4 gradi C", salt, d))   # True
print(verifica(b"lotto 42: 9 gradi C", salt, d))   # False: dato alterato
# "Oblio": si cancellano dato e salt off-chain; il digest on-chain non è più verificabile né invertibile
```

### 4.2 Permessi di scrittura in stile "A authorizes others"

```python
class RegistroFiliera:
    def __init__(self, owner):
        self.owner, self.writers, self.log = owner, set(), []

    def grant(self, caller, x):
        assert caller == self.owner, "solo A concede permessi"
        self.writers.add(x)

    def revoke(self, caller, x):
        assert caller == self.owner, "solo A revoca permessi"
        self.writers.discard(x)

    def write(self, caller, evento):
        assert caller in self.writers, f"{caller} non autorizzato"
        self.log.append((caller, evento))       # append-only; in una DLT reale l'evento è firmato con S_caller

r = RegistroFiliera("A")
for x in ["A1", "B1", "B2", "B3", "C"]:
    r.grant("A", x)
r.write("C", "ritirati componenti da B1")
r.revoke("A", "C")                              # slide "Revoke permissions"
# r.write("C", "...")  -> AssertionError: C non autorizzato
```

In un vero smart contract `caller` corrisponde a `msg.sender`, cioè l'indirizzo derivato dalla chiave che ha firmato la transazione.

---

## 5. Quadro sintetico

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| **Proprietà del ledger** | Pseudo-anonimato (chiavi S/P), ridondanza, authenticity, verifiability, immutability |
| **DLT vs blockchain** | Ogni blockchain è una DLT; non ogni DLT è una catena (IOTA = DAG) |
| **Content-based addressing** | Il file si identifica con l'hash del contenuto (IPFS, CID) |
| **Smart contract** | Codice sul ledger, immutabile ed eseguito automaticamente; "code as law" (Boucher) |
| **Redeploy / proxy** | Non si modifica sul posto: nuovo indirizzo o proxy aggiornabile (che reintroduce fiducia) |
| **Public/private vs permissionless/permissioned** | Lettura vs scrittura; private + permissionless è rara |
| **Smart contract vs no SC** | Ethereum, Cardano, Solana… vs Bitcoin, Litecoin, Ripple; Bitcoin Script non è Turing-completo |
| **Metriche** | Throughput, latenza, fee, Wh/tx; Bitcoin PoW ordini di grandezza sopra i PoS |
| **Supply chain A/B/C/A1** | Un DB unico o tanti DB non funzionano; blockchain permissioned con firme, grant e revoca da parte di A |
| **Even products can write** | Dispositivi con chiavi proprie registrano statistiche, anomalie, manutenzione |
| **GIGO** | La blockchain non certifica la verità del dato fisico, solo chi l'ha scritto e che non è cambiato |
| **Hybrid blockchain** | Prove sul pubblico, dati nel privato (IBM Food Trust) |
| **GDPR** | Artt. 15, 16, 17 in conflitto con l'append-only → dati off-chain, hash on-chain, smart contract per l'accesso |
| **Hype cycle** | Dal "blockchain per tutto" all'uso mirato in architetture ibride; TradeLens come caso di disillusione |
| **Flowchart** | Store condiviso → più scrittori → TTP → scrittori noti → fidati → audit pubblico |

### 5.2 Domande e risposte

1. Che differenza c'è tra DLT e blockchain? Fai un esempio di DLT che non è una blockchain.
2. Quali proprietà derivano da ridondanza e non manomissibilità del ledger?
3. Che cos'è il content-based addressing e perché si sposa bene con una DLT?
4. Perché una transazione può essere vista come codice, e come si arriva agli smart contract?
5. Cosa significa che uno smart contract è immutabile? Come si corregge un bug?
6. Quale rischio introduce il pattern proxy?
7. Spiega le due dimensioni public/private e permissionless/permissioned. Quale combinazione è rara e perché?
8. Bitcoin ha smart contract? Motiva.
9. Perché Bitcoin consuma migliaia di volte più energia per transazione di una piattaforma PoS?
10. Cosa significa la latenza "1 h" di Bitcoin nella tabella?
11. Nel caso A/B/C/A1, perché un unico DB condiviso non basta? E tanti DB separati?
12. A cosa servono S<sub>x</sub> e P<sub>x</sub> nello schema della supply chain?
13. Chi concede e revoca i permessi di scrittura? Che conseguenza ha sulla decentralizzazione?
14. Cosa significa "even products can write"?
15. Spiega il principio Garbage In, Garbage Out.
16. Cos'è una hybrid blockchain? Fai un esempio.
17. Quali diritti GDPR entrano in conflitto con una blockchain e perché?
18. Descrivi la soluzione tipica per i dati sensibili. Che ruolo ha lo smart contract?
19. Cancellare il dato off-chain basta a rendere innocuo il digest on-chain?
20. Descrivi le fasi dell'Hype Cycle applicate alla blockchain.
21. Ripercorri il flowchart "do you need a blockchain?". Cosa rappresenta il ramo Auditing?
22. In quale caso il flowchart porta a una blockchain permissionless?

<details>
<summary><b>Tracce di risposta</b></summary>

1. DLT è la categoria generale di registri distribuiti; la blockchain è una DLT organizzata in blocchi concatenati. Esempio: IOTA (Tangle, DAG).
2. Authenticity, verifiability, immutability.
3. Il file è identificato dall'hash del suo contenuto: sulla DLT basta salvare l'hash per certificare il file e verificarne l'integrità.
4. Anche un trasferimento è un'istruzione eseguita (`transfer(a, b, 2)`); se il ledger ospita codice, può ospitare programmi arbitrari certificati dal consenso.
5. Il codice pubblicato non si modifica. Si pubblica una nuova versione a un nuovo indirizzo (migrando lo stato) o si usa un proxy.
6. Chi controlla l'aggiornamento può cambiare la logica: si reintroduce un punto di fiducia.
7. Public/private = chi legge; permissionless/permissioned = chi scrive e valida. Private + permissionless è rara: non ha senso aprire la validazione a tutti tenendo chiusa la lettura.
8. No: ha Bitcoin Script, non Turing-completo, per esprimere condizioni di spesa, non logica applicativa generale.
9. Il PoW richiede calcolo continuo dei miner; il PoS no. Slide: Bitcoin 360–3.700 kWh/tx, Ethereum PoS 18–557 Wh/tx.
10. Il tempo per considerare una transazione sicura: circa 6 blocchi da ~10 minuti.
11. DB unico: chi lo gestisce, manomissione, accesso dei partner marginali, revoca, sistemi diversi. Tanti DB: non si leggono tra loro, non ci si fida dei dati, audit difficile.
12. S<sub>x</sub> per firmare ciò che X scrive (solo X può averlo scritto); P<sub>x</sub> per verificare la firma.
13. A, che concede i permessi ad A1, B1–B3, C e può revocarli in ogni momento. La scrittura è distribuita, ma la governance resta in mano ad A: rete permissioned.
14. Prodotti con capacità di calcolo hanno una propria coppia di chiavi e registrano statistiche, anomalie e richieste di manutenzione.
15. Il ledger rende immutabile anche un dato falso: garantisce chi ha scritto e che il dato non è cambiato, non che fosse vero.
16. Prove sul registro pubblico, dati sul privato. Esempio: IBM Food Trust.
17. Accesso (15), rettifica (16), cancellazione (17): l'append-only impedisce di modificare o cancellare.
18. Dati off-chain, digest on-chain come prova di esistenza e integrità; lo smart contract fornisce le chiavi, concede e revoca l'accesso e registra ogni operazione (accountability).
19. Non necessariamente: un hash di un dato a bassa entropia si può forzare; serve un salt (da cancellare anch'esso) o il crypto-shredding. Giuridicamente il digest può restare dato pseudonimo.
20. Trigger (Bitcoin, Ethereum) → picco ("blockchain per tutto") → disillusione (costi, GDPR, TradeLens) → consapevolezza (strato di certificazione) → produttività (architetture ibride).
21. Vedi §2.7. Il ramo Auditing: anche con un solo scrittore può servire una DLT se terzi devono poter verificare i dati.
22. Store condiviso, più scrittori, nessuna TTP, scrittori non noti a priori.

</details>

---

## Riferimenti di approfondimento

- Wüst, Gervais, *Do you need a Blockchain?*, CVCBT (2018)
- Boucher, *How blockchain technology could change our lives*, European Parliamentary Research Service (2017) — citazione "code as law"
- Platt et al., *The Energy Footprint of Blockchain Consensus Mechanisms Beyond Proof of Work* (2021)
- Gallersdörfer et al., *Energy Efficiency and Carbon Footprint of PoS Blockchain Protocols* (2022)
- Regolamento (UE) 2016/679 (GDPR), artt. 13–22
- EDPB, *Guidelines 02/2025 on processing of personal data through blockchain technologies*

> Nota: la chiusura di TradeLens, gli articoli GDPR diversi da 15–17, le linee guida EDPB, il pattern proxy, il crypto-shredding, gli hash salati e il Digital Product Passport vengono dalla letteratura generale, non dalle slide. Il titolo esatto del documento Boucher va verificato prima di citarlo.

---

[← Indice](README.md)
