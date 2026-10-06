# Capitolo 2 — DLT, smart contract e casi d'uso

| | |
|---|---|
| **Data** | Venerdì 25/09/2026 · Lezione 2 (parti 2.1 e 2.2) |
| **Macro tema** | Parte I–II — Introduzione alla blockchain e prime applicazioni |
| **Slide** | 02 – Introduction Blockchain (Public Ledger, The Code, How Many Blockchains?, DLT/IOTA, IPFS, Hybrid Blockchain, Costs/Performance/Environmental Impact, Traceability, GDPR, Hype cycle, "When I need a blockchain?") |

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Proprietà del ledger pubblico

- **Pseudo-anonimato:** ogni partecipante è una coppia di chiavi (**S** segreta, **P** pubblica). Non serve sapere *chi sei* ("Chi siete?"): basta verificare che la firma corrisponda a P.
- **Ridondanza:** tutti i nodi hanno una copia dello stesso **append-only log**.
- **Ridondanza + non manomissibilità →** **authenticity** (chi ha scritto, grazie alla firma), **verifiability** (chiunque controlla), **immutability**.
- **Consenso** sulle aggiunte ([Capitolo 1](<01 Il paradigma della decentralizzazione.md>), §1.6). Nota della slide: il ledger è *"not always a blockchain"*.

### 1.2 DLT vs blockchain e DFS

- **DLT** è la categoria generale; la **blockchain** è la DLT a blocchi concatenati da hash. *Not all blockchains are "chains of blocks"*: **IOTA** usa un **DAG** (*Tangle*). Slide: scalabilità, bassi requisiti, **zero-fee**, **nessuno smart contract**.

> ⚠️ **Nota di rigore.** Le proprietà di IOTA si riferiscono alle versioni storiche: le versioni recenti supportano smart contract (infatti IOTA compare anche nell'elenco *Smart Contract based* della stessa slide). All'esame: IOTA come **esempio di DLT a DAG**.

- **Not only DLTs:** le DLT si usano con **file system decentralizzati**, es. **IPFS**, protocollo P2P per ipermedia con **content addressing**: il file è identificato dall'hash del contenuto (CID), non dalla posizione. Pattern che torna sempre: **dato sul DFS, hash sulla DLT**.

### 1.3 Dalla transazione allo smart contract (*The Code*)

Una transazione è già codice (`transfer(a, b, 2)`). Se nei blocchi posso mettere codice, posso metterci programmi: la blockchain diventa una **piattaforma di servizi certificati**. Esempio della slide:

```solidity
pragma solidity ^0.4.0;
contract SimpleStorage {
    uint storedData;
    function set(uint x) public { storedData = x; }
    function get() public view returns (uint) { return storedData; }
}
```

Caratteristiche: consenso sull'**esecuzione**, codice che **non può essere modificato** ed è **eseguito automaticamente**. Philip Boucher: *"the code as the law itself: self-contained, self-performed and self-enforced"* (Legalese vs Computer Code).

**Correggere un bug:** si fa **redeploy** a un nuovo indirizzo (migrando lo stato) oppure si usa un **proxy** con indirizzo stabile che punta a un'implementazione sostituibile.

> ⚠️ **Trade-off.** Il proxy rende il contratto aggiornabile e quindi **reintroduce fiducia** in chi controlla l'aggiornamento.

### 1.4 Tassonomia (*How Many Blockchains?*)

| | **Public** (tutti leggono) | **Private** (solo autorizzati leggono) |
|---|---|---|
| **Permissionless** (tutti validano) | Bitcoin, Ethereum | **Rara** (lo dice la slide) |
| **Permissioned** (validano solo autorizzati) | Validatori selezionati, audit pubblico | Reti enterprise (es. Hyperledger Fabric) |

| Smart contract based | No smart contract |
|---|---|
| Ethereum, Cardano, Solana, Polkadot, Avalanche, IOTA, Hyperledger (Fabric, Besu), Algorand, Sui | Bitcoin, Litecoin, Ripple |

Bitcoin ha **Bitcoin Script**, volutamente **non Turing-completo**: esprime condizioni di spesa, non programmi arbitrari.

### 1.5 Metriche di confronto (valori delle slide, `*` = stima teorica)

| Piattaforma | tx/s | Latenza | Fee (USD/tx) | Wh/tx |
|---|---|---|---|---|
| Bitcoin | 3–7 | 1 h | 1–2 | 360·10³ – 3700·10³ |
| Ethereum | 10–100 | > 13 s | 1,5–10 | 18 – 557 |
| Cardano | 17–20 | 2 min | < 0,25 | 12 – 378 |
| Tezos | 180* | 30 h | < 0,01 | 0,36 – 11 |
| Hedera | 400.000* | 10–20 s | 0,0001 | 0,02 – 0,04 |
| Algorand | 6.000 | 4 s | 0,0003 | 0,17 – 5,34 |
| Solana | 4.000 | 1–3 s | 0,0002 | 0,166 |
| Avalanche | 260–7.000 | < 1 s | 0,03 | 4,76 |

*Fonti in slide: Platt et al. (2021); Gallersdörfer et al. (2022), anche sul Merge di Ethereum.*

> 💡 **Lettura da esame.** "1 h" di Bitcoin ≈ 6 conferme da ~10 min. Bitcoin (PoW) consuma **4–5 ordini di grandezza** in più dei PoS; il passaggio di Ethereum a PoS (*The Merge*, settembre 2022) ha ridotto il consumo di circa il 99,9%. Nessuna piattaforma vince ovunque: è il trilemma.

---

## 2. Architettura: casi d'uso e pattern

### 2.1 Tracciabilità e supply chain

In filiera ogni attore usa sistemi chiusi (*silos*): visibilità limitata, registri manomissibili, dispute. Una DLT offre un registro **condiviso, append-only e verificabile**, con eventi firmati da chi li scrive.

**Casi in slide:** AgroChain (DApp agricola con micro-finanza), Hackinators Farming DApp (*very basic*), **Carrefour**, **Riseria Campanini** (agrichain), **cold chain**, **IBM Food Trust** (esempio di *hybrid blockchain*). Caso noto dalla letteratura: **TradeLens** (IBM + Maersk), chiuso tra fine 2022 e inizio 2023 per scarsa adesione: la tecnologia funzionava, il consorzio no.

### 2.2 Il caso guida del Prof.: A, B1–B3, C, A1

**A** progetta, **B1–B3** producono componenti, **C** trasporta, **A1** assembla.

- **Un unico DB?** *Chi lo gestisce? Come so che i dati non vengono manomessi? Posso accedere se sono poco coinvolto? Come revoco l'accesso a un ex partner? Uso un altro sistema interno.* → problemi di **neutralità, accessi, eterogeneità**.
- **Tanti DB?** *Come leggo gli altri? Sono affidabili? Posso fare audit quando voglio?*
- **Blockchain:**
  1. ogni attore X ha (S<sub>x</sub>, P<sub>x</sub>): S<sub>x</sub> per scrivere (firmare), P<sub>x</sub> per far verificare agli altri;
  2. **A authorizes others** (concede scrittura ad A1, B1–B3, C);
  3. **everyone writes their activities**, firmandole;
  4. **even products can write**: componenti con capacità di calcolo hanno chiavi proprie e registrano statistiche, anomalie, manutenzione;
  5. **revoke permissions**: *in ogni momento A può revocare l'accesso in scrittura* (es. a C).

> ⚠️ **Nota di rigore.** La rete è **permissioned** e A resta radice dei permessi: scrittura e verifica sono decentralizzate, la **governance** no.

> 💡 **Garbage In, Garbage Out.** La blockchain non certifica che il dato fisico sia vero: un dato falso diventa un falso immutabile. Garantisce **chi** ha scritto e che il dato **non è cambiato**. Il contatto mondo fisico–ledger è il problema degli **oracoli**.

### 2.3 Hybrid blockchain

*Public + private* insieme: **proofs go public, data go private**. Esempio: IBM Food Trust.

### 2.4 Blockchain e GDPR

GDPR (Reg. UE 2016/679): *self-executing*, applicabile anche fuori UE, in vigore dal 2016 con sanzioni dal 2018, pensato per un **modello centralizzato** (c'è un titolare). Diritti in slide: **accesso (art. 15)**, **rettifica (art. 16)**, **cancellazione/oblio (art. 17)**. L'append-only li contraddice → **need to use off-chain data**.

```
[dato sensibile] ──▶ storage off-chain protetto (cancellabile, rettificabile)
       │
   hash crittografico ──▶ digest on-chain (prova di esistenza e integrità)
```

Lo **smart contract controlla l'accesso** ai dati off-chain: fornisce le chiavi, concede e revoca, **registra ogni operazione → accountability**.

> ⚠️ **Nota di rigore.** Cancellare il dato off-chain non rende innocuo il digest: un hash di un dato a bassa entropia (es. codice fiscale) si inverte per forza bruta. Si usa un **hash con salt** (cancellando anche il salt) o si cifra il dato e si distrugge la chiave (*crypto-shredding*). Per l'EDPB (Linee guida 02/2025 sulla blockchain) anche chiavi pubbliche e hash possono essere dati personali pseudonimi.

### 2.5 Hype cycle e "quando serve una blockchain?"

**Hype cycle (Gartner):** trigger (Bitcoin, Ethereum) → picco ("blockchain per tutto") → disillusione (costi, GDPR, TradeLens) → consapevolezza (strato di certificazione tra parti che non si fidano) → produttività (architetture ibride).

**Flowchart (da Wüst & Gervais, 2018, con il ramo Auditing):**

```
Serve uno store condiviso e consistente? ── NO ──▶ DB
  │ SÌ
Più di un'entità contribuisce? ── NO ──▶ DB  (se serve AUDITING → si prosegue)
  │ SÌ
Esiste una TTP? ── SÌ ──▶ DB
  │ NO
Scrittori noti? ── NO ──▶ PERMISSIONLESS blockchain
  │ SÌ
Scrittori fidati? ── SÌ ──▶ DB
  │ NO
Serve verificabilità pubblica? ── NO ──▶ PRIVATE PERMISSIONED
                               └─ SÌ ──▶ PUBLIC PERMISSIONED
```

---

## 3. Trade-off e attacchi

| Rischio / limite | Mitigazione tipica |
|---|---|
| **GIGO**: il ledger rende immutabile anche il falso | Firme, audit trail, sensori certificati, oracoli affidabili |
| **GDPR**: append-only vs oblio e rettifica | Dati off-chain, hash salati, crypto-shredding |
| **Governance** permissioned in mano ad A | Governance consortile, regole on-chain |
| **Adesione** del consorzio (TradeLens) | Incentivi, operatore neutrale |
| **Aggiornabilità** (proxy) | Timelock, multi-firma |
| **Costi e prestazioni** (§1.5) | Scegliere la piattaforma per caso d'uso; ibrido |
| **Hype** | Flowchart §2.5 |

---

## 4. Esempi e codice

### 4.1 Notarizzazione con hash salato

```python
import hashlib, os

def commit(dato: bytes):
    salt = os.urandom(16)                              # resta off-chain
    return salt, hashlib.sha256(salt + dato).hexdigest()   # il digest va on-chain

def verifica(dato, salt, digest):
    return hashlib.sha256(salt + dato).hexdigest() == digest

salt, d = commit(b"lotto 42: 4 gradi C")
print(verifica(b"lotto 42: 4 gradi C", salt, d))   # True
print(verifica(b"lotto 42: 9 gradi C", salt, d))   # False
# Oblio: si cancellano dato e salt; il digest on-chain non è più invertibile
```

### 4.2 "A authorizes others" in Solidity (schema)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RegistroFiliera {
    address public owner;                   // A
    mapping(address => bool) public writer;
    event Evento(address indexed autore, string descrizione);

    constructor() { owner = msg.sender; }
    modifier onlyOwner() { require(msg.sender == owner, "solo A"); _; }

    function grant(address x)  external onlyOwner { writer[x] = true; }
    function revoke(address x) external onlyOwner { writer[x] = false; }

    function write(string calldata e) external {
        require(writer[msg.sender], "non autorizzato");
        emit Evento(msg.sender, e);          // firmato dalla chiave di chi invia la tx
    }
}
```

`msg.sender` è l'indirizzo derivato dalla chiave che ha firmato la transazione: è la firma con S<sub>x</sub> della slide.

---

## 5. Quadro di riepilogo

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Proprietà del ledger | Pseudo-anonimato (S/P), ridondanza → authenticity, verifiability, immutability |
| DLT vs blockchain | Ogni blockchain è DLT, non viceversa (IOTA = DAG) |
| Content addressing | Il file si identifica con l'hash del contenuto (IPFS) |
| Smart contract | Codice immutabile ed eseguito automaticamente; "code as law" (Boucher) |
| Tassonomia | Public/private = lettura; permissionless/permissioned = scrittura; private+permissionless rara |
| Metriche | tx/s, latenza, fee, Wh/tx; PoW ordini di grandezza sopra PoS |
| Caso A/B/C/A1 | Permissioned: firme, grant e revoca da parte di A; *even products can write* |
| GIGO | Si garantisce chi ha scritto, non che il dato sia vero |
| Hybrid | Proofs go public, data go private (IBM Food Trust) |
| GDPR | Artt. 15–17 vs append-only → off-chain + digest + smart contract per l'accesso |
| Flowchart | Store condiviso → più scrittori → TTP → noti → fidati → audit pubblico |

### 5.2 Parole chiave

`DLT` · `blockchain` · `DAG / Tangle` · `IPFS` · `content addressing` · `CID` · `smart contract` · `code is law` · `redeploy` · `proxy` · `public / private` · `permissionless / permissioned` · `Bitcoin Script` · `throughput` · `latenza` · `Wh/tx` · `supply chain` · `GIGO` · `oracolo` · `hybrid blockchain` · `GDPR` · `off-chain` · `digest` · `salt` · `crypto-shredding` · `hype cycle`

### 5.3 Domande

1. Differenza tra DLT e blockchain, con un esempio di DLT non a catena.
2. Quali proprietà derivano da ridondanza e non manomissibilità?
3. Come si arriva dalla transazione allo smart contract? Come si corregge un bug in un contratto immutabile e che rischio introduce il proxy?
4. Spiega public/private e permissionless/permissioned. Quale combinazione è rara e perché?
5. Bitcoin ha smart contract?
6. Perché Bitcoin consuma migliaia di volte più energia per transazione di una piattaforma PoS? Cosa significa la latenza "1 h"?
7. Nel caso A/B/C/A1 perché non bastano un DB unico o tanti DB? Che ruolo hanno S<sub>x</sub> e P<sub>x</sub>?
8. La rete del caso A/B/C/A1 è davvero decentralizzata?
9. Spiega Garbage In, Garbage Out.
10. Quali diritti GDPR sono in conflitto con la blockchain e qual è la soluzione tipica?
11. Cancellare il dato off-chain basta a rendere innocuo il digest?
12. Ripercorri il flowchart; cosa rappresenta il ramo Auditing?

<details>
<summary><b>Tracce di risposta</b></summary>

1. DLT = registri distribuiti in generale; blockchain = DLT a blocchi concatenati. IOTA (DAG).
2. Authenticity, verifiability, immutability.
3. Se il ledger ospita codice, ospita programmi certificati dal consenso. Redeploy a nuovo indirizzo o proxy; il proxy reintroduce fiducia in chi aggiorna.
4. Lettura vs scrittura/validazione. Private + permissionless: aprire la validazione e chiudere la lettura non ha senso.
5. No: Bitcoin Script non è Turing-completo, esprime solo condizioni di spesa.
6. PoW = calcolo continuo dei miner. "1 h" ≈ 6 conferme da ~10 min.
7. DB unico: gestore, manomissione, accessi, revoca, eterogeneità. Tanti DB: lettura reciproca, affidabilità, audit. S<sub>x</sub> firma, P<sub>x</sub> verifica.
8. Scrittura e verifica sì, governance no: A concede e revoca (permissioned).
9. Il ledger rende immutabile anche il dato falso; garantisce autore e integrità, non verità.
10. Artt. 15, 16, 17. Dati off-chain, digest on-chain, smart contract che dà chiavi, concede/revoca e registra (accountability).
11. No: dati a bassa entropia si forzano; serve salt (da cancellare) o crypto-shredding.
12. Vedi §2.5. Auditing: anche con un solo scrittore può servire una DLT se terzi devono verificare.

</details>

---

> **Fonti e verifica.** Verificato su 02 – Introduction Blockchain (tabelle, tassonomia, GDPR, flowchart). Dalla letteratura (non in slide): chiusura di TradeLens, pattern proxy, hash salati, crypto-shredding, Linee guida EDPB 02/2025, dato del −99,9% del Merge, codice Solidity del §4.2. Riferimenti: Wüst & Gervais, *Do you need a Blockchain?*, CVCBT 2018; Boucher, *How blockchain technology could change our lives*, EPRS 2017; Platt et al. 2021; Gallersdörfer et al. 2022.

[← Indice](README.md)
