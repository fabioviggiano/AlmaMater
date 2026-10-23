# Capitolo 7 — Sidechain, rollup e bridge

| | |
|---|---|
| **Data** | Lunedì 19/10/2026 · Lezione 7 (da remoto) |
| **Macro tema** | Parte III–IV — Scalabilità Layer 2 e interoperabilità |
| **Slide** | 05.1 – Scalability (Layer 2) <!-- verificare nome file --> · <!-- link Panopto --> |

[← Indice](README.md)

Continua il Cap. 6.3. Lì il Layer 2 era rappresentato dagli state channel: veloci e sicuri, ma adatti solo a poche parti che interagiscono spesso. Qui si vedono le soluzioni L2 **general purpose**: **sidechain**, **Plasma** e soprattutto **rollup** (optimistic e zk). Poi si passa all'**interoperabilità**: i **bridge** che collegano blockchain indipendenti. La lezione è una **panoramica**: l'obiettivo è capire le idee, non i dettagli implementativi.

---

## 1. Fondamenti

### 1.1 La domanda di fondo: chi garantisce la sicurezza?

Tutte le soluzioni di questo capitolo spostano lavoro fuori da Ethereum (L1). Per confrontarle basta una domanda:

> **Frase chiave da esame:** se la catena secondaria mente, **chi se ne accorge e chi la corregge?** Se la risposta è "Ethereum", la soluzione eredita la sicurezza di L1 (rollup). Se la risposta è "i suoi validatori", ha una sicurezza propria e in genere minore (sidechain).

### 1.2 Sidechain

**Definizione.** Catena secondaria che opera **in parallelo** a una catena principale (*parent chain*) con un **proprio meccanismo di consenso** (es. Proof of Stake).

- **Collegamento:** un **bridge bidirezionale** (*two-way bridge*, o *two-way peg*) sposta asset tra parent chain e sidechain.
- **Vantaggio:** flessibilità per innovazione e prestazioni (blocchi più veloci, fee più basse, regole diverse).
- **Svantaggio:** la sicurezza **non** è garantita da L1, ma dai **validatori della sidechain**. Per questo è considerata **meno sicura**.

⚠️ **Nota di rigore.** Per la definizione stretta una sidechain non è un vero Layer 2, perché non eredita la sicurezza di L1. Le slide la presentano tra le soluzioni L2 come "strategia per aggiungere funzionalità".

**Esempio: Polygon** (PoS). È *"un protocollo e un framework per costruire e connettere reti compatibili con Ethereum"*:
- circa **10× più veloce** e **più di 10× più economico** di Ethereum;
- stessi strumenti, stesse conoscenze e **stessi smart contract** (compatibile EVM);
- per fare il deploy su Polygon basta **cambiare il nome della rete**.

### 1.3 Plasma

Idea (whitepaper di Poon e Buterin, 2017): **catene "figlie"** (*child chains*) agganciate alla catena principale di Ethereum.

- Le child chain hanno **meno nodi** e svolgono operazioni complesse con **interazione minima** con la main chain.
- A intervalli regolari inviano alla root chain uno **state commitment**: il **Merkle root** del loro stato.
- In questo modo **beneficiano della sicurezza della mainnet**: il commitment su L1 è la prova a cui appellarsi in caso di problemi.
- Ogni catena può avere a sua volta **sottocatene** (struttura ad albero). Le slide mostrano *plasma contract* per micropagamenti, blockchain private ed exchange decentralizzati.

```
Ethereum (root)   [■]←[■]←[■]←[■]←[■]     ogni blocco contiene i commitment certificati
                   ↑      ↓        ↓
Plasma contract   micro-  private  DEX
                  payments chain
                  [■]←[■]  [■]←[■]  [■]←[■]
```

Ci sono diverse implementazioni di Plasma. Dalla letteratura: il limite principale è che su L1 va **solo l'hash**, non i dati. Se l'operatore della child chain nasconde i dati (*data withholding*), gli utenti non possono dimostrare cosa possiedono e devono uscire in massa (*mass exit*). I rollup nascono per risolvere proprio questo.

### 1.4 Rollup

È la soluzione **più diffusa** oggi.

- Una **blockchain secondaria** ancorata (*pegged*) alla catena principale.
- L'**esecuzione** delle transazioni si sposta su **L2**, ma **tutti i dati** delle transazioni eseguite su L2 sono **pubblicati su L1**, insieme alle prove sui dati di L2.
- Questa **data availability** permette di **rieseguire tutte le transazioni** del sistema, se serve.

```
Layer 2   → S1 --{…, tx_i, …}--> S2 --{…, tx_j, …}--> Sn
             |                   |                    |
           rollup              rollup               rollup
             ↓                   ↓                    ↓
Layer 1   → B1 ----------------> B2 ----------------> Bn
```

A ogni "rollup" si scrive su L1 lo stato (il suo hash) della catena secondaria più i dati delle transazioni: una specie di **checkpoint certificato**.

### 1.5 Rollup vs sidechain vs state channel

È il punto che negli appunti risultava "non chiarissimo". La differenza sta in **cosa resta su Ethereum**:

| | **State channel** (Cap. 6.3) | **Rollup** | **Sidechain** |
|---|---|---|---|
| Dati delle tx | off-chain, tra le parti | **su L1** (compressi) | off-chain, sulla sidechain |
| Calcolo | off-chain | off-chain (L2) | off-chain (sidechain) |
| Chi può verificare | solo i partecipanti | **qualsiasi nodo Ethereum** | solo chi partecipa alla sidechain |
| Sicurezza | Ethereum | **Ethereum** | validatori propri (**minore**) |
| Campo d'uso | applicazioni specifiche, poche parti | **general purpose** | general purpose |

> 💡 **Il filo del corso.** Il rollup è la **soluzione di mezzo**: prende dagli state channel la sicurezza garantita da Ethereum e dalle sidechain l'uso general purpose. Il trucco sono i dati su L1: chiunque può rieseguire, quindi nessuno deve fidarsi dell'operatore, e si evita la centralizzazione.

---

## 2. Architettura

### 2.1 Optimistic rollup

Si chiama "ottimistico" perché **assume che le transazioni siano valide** e controlla solo se qualcuno contesta, tramite **fraud proof**. Esempi: **Optimism**, **Arbitrum**.

Il sistema è implementato con **smart contract su L1**. Due attori:

- **Aggregator**: raccoglie le tx degli utenti L2, le esegue e pubblica tramite lo smart contract i dati delle tx (*rollup data*) e gli **state root** risultanti.
- **Verifier**: ricontrolla i calcoli e, se serve, usa lo smart contract per **contestare** le transazioni.

```
Layer 2   User --TXN--> Aggregator --rollup data--┐
            ↑                                     ↓
Layer 1   User --funds--> Smart contract (rollup) --> registrato nel blocco B3
```

Funzionamento:
1. le transazioni vengono raggruppate in **batch**;
2. gli **state root** vengono pubblicati su L1;
3. si apre una **finestra per le fraud proof** (di solito **7 giorni**);
4. **chiunque** può contestare le transazioni non valide.

**Fase di disputa (*fraudulent rollups*).**
1. Un verifier non è d'accordo con i dati pubblicati e apre una **dispute phase**.
2. Sottomette al contratto una **fault proof** relativa a una transazione del batch.
3. Il contratto trova da solo la transazione fraudolenta **verificando le transizioni di stato una per una** per ogni tx del batch.
4. Se la frode esiste, la tx viene **invalidata insieme a tutte quelle successive** (che partivano da uno stato sbagliato) e l'**aggregator viene penalizzato**.
5. Se la contestazione fallisce, è il **verifier a essere penalizzato** (così nessuno contesta a vuoto).

**Le dispute richiedono tempo.** Bisogna lasciare al sistema il tempo di sottomettere le fraud proof prima di finalizzare il rollup. Arbitrum e altri richiedono **7 giorni** per la finalità sulla main chain: per ritirare fondi da L2 a L1 si aspetta una settimana.

```
Batch submission → Rollup contract → Challenge window ─┬─(nessuna contestazione)→ batch finale
                                                       └─ Fraud proof → batch corretto / rifiutato
```

### 2.2 Zero-knowledge rollup (zk-rollup)

Invece di presumere la validità, la **dimostrano crittograficamente**. Esempi: **zkSync**, **StarkNet**.

- Per ogni batch l'operatore genera una **validity proof** (**ZK-SNARK** o **ZK-STARK**).
- Un contratto su L1 (**proof verifier**) controlla la prova: se è valida **accetta il nuovo stato**, altrimenti **rifiuta il batch**.
- **Non serve un periodo di contestazione**: la finalità è immediata.

```
Batch submission → ZK proof → Proof verifier (L1) ─┬→ Accept state
                                                   └→ Reject batch
```

Il Prof. lo cita solo in breve: la matematica delle prove a conoscenza zero è complessa e fuori dagli obiettivi della lezione. Basta sapere che la prova è **piccola e veloce da verificare**, anche se il batch contiene migliaia di transazioni.

### 2.3 Optimistic vs zk: il confronto da esame

| | **Optimistic rollup** | **zk-rollup** |
|---|---|---|
| Ipotesi | Tx valide finché nessuno contesta | Validità dimostrata a ogni batch |
| Prova | **Fraud proof** (solo in caso di disputa) | **Validity proof** (SNARK/STARK, sempre) |
| Finalità / prelievi | **Lenta**: ~7 giorni di finestra | **Immediata**, prelievi veloci |
| Compatibilità EVM | **Sì**, più semplice | Possibili **problemi** di compatibilità |
| Implementazione | Più semplice, meno calcolo | Matematica complessa, **calcolo elevato** per generare le prove |
| Sicurezza | Serve almeno **un verifier onesto e attivo** | **Garanzie più forti** (crittografiche) |
| Privacy | — | Potenziale migliore |
| Svantaggio tipico | Fraud proof complesse, prelievi lunghi | Costo e complessità della prova |

### 2.4 Bridge: collegare le isole

Lo spazio blockchain è **frammentato** in tante reti indipendenti. Questo isolamento ostacola collaborazione, trasferimento di asset e innovazione. Un **bridge** collega due o più blockchain e permette di trasferire **token e/o dati** tra loro. Serve sia alla scalabilità (passare da L1 a un L2 o a una sidechain) sia all'**interoperabilità**.

**Tipi di bridge.**

| Tipo | Come funziona | Pro / contro | Esempi |
|---|---|---|---|
| **Centralizzato** | Un intermediario fidato o **custode** | Semplice, operato da entità note; rischio concentrato sul custode | Binance Bridge, **WBTC** |
| **Decentralizzato** | Smart contract + rete distribuita di **validatori** | Più complesso, ma più sicurezza e fiducia | Portal (**Wormhole**), Hop Protocol |
| **Relay chain** | Una blockchain separata fa da **hub** tra le catene collegate | Comunicazione nativa tra le catene dell'ecosistema | **Polkadot** |

### 2.5 Lock-and-mint

È il modo **tipico** di implementare un bridge: si **bloccano** gli asset su una catena e si **coniano** (*mint*) equivalenti **wrapped** sull'altra. Servono validatori o un custode, quindi funziona sia con bridge centralizzati sia decentralizzati.

1. **Initiation**: l'utente chiede di spostare token dalla Chain A alla Chain B.
2. **Locking**: i token vengono **bloccati** in uno smart contract sulla Chain A.
3. **Verification**: i **validatori** verificano la transazione di lock su A.
4. **Minting**: viene coniata su B una quantità equivalente di token **wrapped**, di solito ancorati **1:1** all'originale.
5. **Transfer**: l'utente riceve i token wrapped su B.
6. **Redemption**: per tornare indietro si inverte il processo. I wrapped su B vengono **bruciati** (*burn*) e gli originali su A **sbloccati**.

**Uso degli oracoli.** Le due catene non si vedono tra loro: un **oracolo** (Cap. 1) osserva una catena e agisce sull'altra.

```
User          BridgeSource (A)         Oracle              BridgeDestination (B)
 |--lockTokens(amount, dest)-->|                                   |
 |                             |--requestMint(user, amount, dest)->|
 |                             |                    |--mintTokens(user, amount)-->|
 |<----------------------------- Tokens minted ------------------------------------|
 |--unlockTokens(amount)------------------------------------------>|  (burn su B)
 |                             |                    |<--informUnlock(user, amount)--|
 |                             |<--releaseTokens(user, amount)--|                   |
 |<---- Tokens released -------|                                                   |
```

**Esempi di bridge:** Tezos Wrap Protocol (Tezos ↔ Ethereum), Binance Smart Chain Bridge (USDT, BUSD, ETH tra Binance Chain e BSC), Wormhole (Solana ↔ Ethereum), Polygon ↔ Ethereum, **WBTC** (Bitcoin ↔ Ethereum).

> 💡 **Per il project work.** Il Prof. segnala **Chainlink CCIP** (*Cross-Chain Interoperability Protocol*): su ciascuna catena un *Router* e un *OnRamp/OffRamp* con *Token Pool* (lock/burn e unlock/mint); in mezzo, off-chain, una *Committing DON* e una *Executing DON* (reti di oracoli decentralizzate) sorvegliate da una *Risk Management Network* indipendente.

---

## 3. Trade-off e attacchi

| Rischio / limite | Perché | Mitigazione |
|---|---|---|
| **Sicurezza della sidechain** | Dipende dai suoi validatori, non da Ethereum | Più validatori e stake; per asset di valore, preferire un rollup |
| **Data withholding** (Plasma) | Su L1 c'è solo il Merkle root: l'operatore può nascondere i dati | Exit games, mass exit; superato dai rollup (dati su L1) |
| **Aggregator disonesto** (optimistic) | Pubblica uno state root falso | Fraud proof: tx invalidata con le successive, aggregator penalizzato |
| **Contestazioni a vuoto** | Un verifier potrebbe bloccare il sistema con dispute false | Il verifier che sbaglia viene penalizzato |
| **Nessun verifier attivo** | La sicurezza optimistic richiede almeno un verifier onesto online | Incentivi per i verifier; chiunque può contestare |
| **Prelievi lenti** (optimistic) | Finestra di 7 giorni prima della finalità | zk-rollup; liquidity provider che anticipano i fondi a pagamento |
| **Complessità delle prove** (zk) | Matematica difficile, calcolo pesante, compatibilità EVM parziale | zkEVM; hardware dedicato per generare le prove |
| **Fiducia nel bridge** | Gli asset sono bloccati nel contratto: bisogna fidarsi di chi l'ha scritto o lo custodisce | Bridge decentralizzati, audit, codice verificato |
| **De-peg del wrapped** | In mercati volatili il prezzo del token wrapped può divergere dall'originale | Riserve verificabili; redemption sempre possibile |
| **Bug del bridge** | Vulnerabilità nell'implementazione: il contratto custodisce cifre enormi | Audit, limiti di prelievo, pause d'emergenza |
| **Scalabilità del bridge** | Le transazioni cross-chain crescono e il ponte diventa collo di bottiglia | Protocolli dedicati (es. CCIP), relay chain |

Dalla letteratura: i bridge sono stati il bersaglio dei furti più grandi della storia della DeFi, per esempio **Ronin** (circa 600 milioni di dollari, marzo 2022, chiavi di 5 validatori su 9 compromesse) e **Wormhole** (circa 320 milioni, febbraio 2022, bug nella verifica delle firme). Collegamento con le slide *DeFi Security* (9.1).

---

## 4. Esempi e codice

### 4.1 Optimistic rollup in Python: fraud proof e penalità

Simula la fase di disputa: un aggregator pubblica uno state root falso, un verifier lo contesta, il contratto ricontrolla le transizioni una per una.

```python
import hashlib, json

def root(state):                                   # "state root": hash dello stato (al posto del Merkle root)
    return hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()[:10]

def apply(state, tx):                              # funzione di transizione di stato
    s = dict(state)
    src, dst, amt = tx
    if s.get(src, 0) < amt:
        raise ValueError("saldo insufficiente")
    s[src] -= amt
    s[dst] = s.get(dst, 0) + amt
    return s

class RollupContract:                              # smart contract su L1
    WINDOW = 7                                     # finestra di contestazione (giorni)
    BOND = 10                                      # cauzione di aggregator e verifier
    def __init__(self, genesis):
        self.genesis, self.batches = genesis, []
    def submit(self, aggregator, txs, roots, day):  # dati delle tx + state root pubblicati su L1
        self.batches.append(dict(by=aggregator, txs=txs, roots=roots, day=day, ok=True))
    def dispute(self, verifier, b, i, day):         # fault proof sulla tx i del batch b
        B = self.batches[b]
        assert day < B["day"] + self.WINDOW, "finestra chiusa: batch già finale"
        state = self.genesis                        # data availability: il contratto può rieseguire
        for j, tx in enumerate(B["txs"]):           # verifica le transizioni una per una
            try:
                state = apply(state, tx)
                valid = root(state) == B["roots"][j]
            except ValueError:
                valid = False
            if not valid:
                B["txs"], B["roots"] = B["txs"][:j], B["roots"][:j]   # invalida j e le successive
                return f"frode alla tx {j}: {B['by']} perde {self.BOND}, {verifier} ne guadagna {self.BOND}"
        return f"nessuna frode: {verifier} perde {self.BOND}"

genesis = {"alice": 10, "bob": 5, "carol": 0}
txs = [("alice", "bob", 3), ("bob", "carol", 6), ("carol", "alice", 1)]

# L'aggregator onesto calcola gli state root; quello disonesto falsifica la tx 1 (si accredita 50)
state, roots = genesis, []
for tx in txs:
    state = apply(state, tx); roots.append(root(state))
fake = dict(apply(genesis, txs[0])); fake["bob"] += 50
bad_roots = [roots[0], root(fake), roots[2]]

L1 = RollupContract(genesis)
L1.submit("aggregator-onesto", txs, roots, day=0)
L1.submit("aggregator-ladro", txs, bad_roots, day=1)
print("batch 0:", L1.dispute("verifier", 0, 1, day=2))
print("batch 1:", L1.dispute("verifier", 1, 1, day=3))
print("tx rimaste nel batch 1:", L1.batches[1]["txs"])
try:
    L1.dispute("verifier", 1, 0, day=9)
except AssertionError as e:
    print("dispute al giorno 9:", e)
```

Output:

```
batch 0: nessuna frode: verifier perde 10
batch 1: frode alla tx 1: aggregator-ladro perde 10, verifier ne guadagna 10
tx rimaste nel batch 1: [('alice', 'bob', 3)]
dispute al giorno 9: finestra chiusa: batch già finale
```

Cosa osservare:
- Il contratto può rieseguire **solo perché le tx sono su L1**: è la data availability che distingue il rollup da Plasma.
- Nel batch 1 la tx 1 è falsa: vengono invalidate **lei e la tx 2**, che partiva da uno stato sbagliato.
- Contestare il batch onesto costa la cauzione al verifier.
- Dopo 7 giorni il batch è **finale**: se nessuno ha contestato in tempo, la frode passa. Per questo servono verifier attivi.
- Semplificazione: ogni batch riparte dal genesis; in un rollup reale riparte dallo state root finale del batch precedente.

### 4.2 Bridge lock-and-mint in Solidity

Due contratti su due catene diverse. L'oracolo è un indirizzo fidato (bridge **centralizzato**); in un bridge decentralizzato sarebbe una soglia di firme di validatori.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ---------- Chain A: il contratto che custodisce gli asset originali ----------
contract BridgeSource {
    address public immutable oracle;                 // validatore/custode del ponte
    mapping(address => uint256) public locked;

    event Locked(address indexed user, uint256 amount, address destination);

    constructor(address _oracle) { oracle = _oracle; }

    function lockTokens(address destination) external payable {      // Locking
        locked[msg.sender] += msg.value;
        emit Locked(msg.sender, msg.value, destination);              // l'oracolo ascolta questo evento
    }

    function releaseTokens(address payable user, uint256 amount) external {   // Redemption
        require(msg.sender == oracle, "solo l'oracolo");
        locked[user] -= amount;                      // revert automatico se amount > locked
        user.transfer(amount);
    }
}

// ---------- Chain B: il token "wrapped", ancorato 1:1 ----------
contract WrappedToken {
    string public constant name = "Wrapped ETH (bridge didattico)";
    address public immutable oracle;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;

    event Burned(address indexed user, uint256 amount);              // segnale per lo sblocco su A

    constructor(address _oracle) { oracle = _oracle; }

    function mint(address user, uint256 amount) external {           // Minting
        require(msg.sender == oracle, "solo l'oracolo");
        balanceOf[user] += amount;
        totalSupply += amount;
    }

    function transfer(address to, uint256 amount) external {         // uso del token su B
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
    }

    function burn(uint256 amount) external {                         // unlockTokens: si brucia su B
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;
        emit Burned(msg.sender, amount);
    }
}
```

Cosa osservare:
- **Invariante del ponte**: `WrappedToken.totalSupply` su B deve essere uguale all'ETH bloccato in `BridgeSource` su A. Se l'oracolo è compromesso, può coniare wrapped senza copertura o svuotare A: è il rischio "devi fidarti dei creatori".
- Le catene comunicano solo tramite **eventi** (`Locked`, `Burned`) letti dall'oracolo off-chain.
- Le sottrazioni (`-=`) vanno in revert se il saldo non basta, grazie ai controlli di overflow di Solidity 0.8.
- Codice didattico, non sicuro per la produzione: manca la protezione dal *replay* (un evento processato due volte).

---

## 5. Quadro di riepilogo

> 💡 **Punti su cui insiste il Prof.** Sidechain = consenso proprio, **meno sicura**. Rollup = esecuzione su L2 ma **dati su L1**, quindi rieseguibile da chiunque: è la soluzione di mezzo tra state channel e sidechain. **Optimistic** (fraud proof, 7 giorni) vs **zk** (validity proof, finalità immediata). Gli attori **aggregator/verifier** e la fase di disputa. Bridge: **lock-and-mint**, ruolo degli oracoli, contro. **CCIP** come spunto per il project work.

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Sidechain | Catena parallela con consenso proprio, collegata da un two-way bridge; sicurezza dei suoi validatori |
| Polygon | Sidechain/framework compatibile EVM: ~10× più veloce, >10× più economica, stessi contratti |
| Plasma | Child chain che inviano periodicamente Merkle root a Ethereum; solo commitment, non dati |
| Rollup | Esecuzione su L2, dati e state root su L1: chiunque può rieseguire |
| Optimistic rollup | Validità presunta; fraud proof entro ~7 giorni; aggregator e verifier |
| Fase di disputa | Verifica delle transizioni una per una; tx falsa e successive invalidate; chi sbaglia è penalizzato |
| zk-rollup | Validity proof (SNARK/STARK) per batch; nessuna finestra; finalità immediata |
| Bridge | Collega blockchain diverse: centralizzato, decentralizzato, relay chain |
| Lock-and-mint | Lock su A → verifica → mint wrapped 1:1 su B; ritorno con burn su B e unlock su A |
| Oracolo nel bridge | Osserva gli eventi di una catena e chiama i contratti dell'altra |

### 5.2 Parole chiave

`Layer 2` · `sidechain` · `parent chain` · `two-way bridge` · `two-way peg` · `Polygon` · `Plasma` · `child chain` · `state commitment` · `Merkle root` · `data withholding` · `rollup` · `data availability` · `state root` · `batch` · `optimistic rollup` · `fraud proof` · `fault proof` · `challenge window` · `aggregator` · `verifier` · `dispute phase` · `zk-rollup` · `validity proof` · `ZK-SNARK` · `ZK-STARK` · `Optimism` · `Arbitrum` · `zkSync` · `StarkNet` · `bridge` · `interoperabilità` · `relay chain` · `Polkadot` · `lock-and-mint` · `wrapped token` · `WBTC` · `burn` · `oracolo` · `Wormhole` · `Chainlink CCIP`

### 5.3 Domande

1. Cos'è una sidechain e perché è considerata meno sicura di un rollup?
2. Come funziona Plasma e qual è il suo limite principale?
3. Cosa significa che un rollup garantisce la data availability e perché è importante?
4. Confronta state channel, rollup e sidechain.
5. Descrivi i ruoli di aggregator e verifier in un optimistic rollup.
6. Descrivi la fase di disputa: cosa succede se la frode c'è e se non c'è?
7. Perché un optimistic rollup richiede 7 giorni per la finalità e uno zk-rollup no?
8. Elenca vantaggi e svantaggi di optimistic e zk-rollup.
9. Descrivi i passi del meccanismo lock-and-mint e il ruolo dell'oracolo.
10. Quali sono i rischi di un bridge?

<details>
<summary><b>Tracce di risposta</b></summary>

1. È una catena parallela con un proprio consenso, collegata alla parent chain da un bridge bidirezionale. La sua sicurezza dipende dai suoi validatori, non da Ethereum. Il rollup invece pubblica i dati su L1, quindi Ethereum può verificarlo.
2. Crea child chain agganciate a Ethereum che eseguono le operazioni e inviano periodicamente il Merkle root del loro stato. Limite: su L1 va solo l'hash, quindi se l'operatore nasconde i dati gli utenti non possono dimostrare i propri fondi.
3. Tutti i dati delle tx eseguite su L2 sono pubblicati su L1. Così chiunque può rieseguire le transazioni e verificare gli state root: nessuno deve fidarsi dell'operatore, e si evita la centralizzazione.
4. State channel: dati off-chain tra poche parti, sicurezza di Ethereum, uso specifico. Sidechain: tutto off-chain, general purpose, sicurezza propria. Rollup: calcolo off-chain ma dati su L1, general purpose e sicurezza di Ethereum. È la soluzione di mezzo.
5. L'aggregator raccoglie ed esegue le tx su L2, poi pubblica dati e state root tramite lo smart contract su L1. Il verifier ricontrolla i calcoli e, se trova un errore, apre una disputa con una fault proof.
6. Il contratto riverifica le transizioni di stato del batch una per una. Se trova la tx fraudolenta, la invalida con tutte le successive e penalizza l'aggregator. Se non la trova, penalizza il verifier.
7. L'optimistic presume la validità e deve lasciare tempo a chiunque di presentare una fraud proof prima di finalizzare. Lo zk dimostra la validità a ogni batch con una prova crittografica, quindi non c'è niente da contestare.
8. Optimistic: compatibile EVM, più semplice, meno calcolo; ma prelievi lunghi e fraud proof complesse. Zk: prelievi veloci, garanzie più forti, privacy migliore; ma matematica complessa, calcolo elevato e possibili problemi di compatibilità EVM.
9. Initiation, lock dei token in un contratto su A, verifica dei validatori, mint dei wrapped 1:1 su B, ricezione da parte dell'utente; per tornare, burn su B e unlock su A. L'oracolo osserva gli eventi di una catena e chiama mint o release sull'altra.
10. Si deve fidare di chi ha creato o custodisce il contratto; il token wrapped può perdere l'aggancio di prezzo in mercati volatili; i bug di implementazione espongono fondi enormi (Ronin, Wormhole); il ponte fatica a scalare con molte tx cross-chain.

</details>

---

### Da verificare

- [ ] **Ultimi ~30 minuti della registrazione ancora da ascoltare**: integrare il capitolo con quello che manca (e controllare se la parte su CCIP o sugli esempi continua)
- [ ] Nome del file di slide: negli appunti compare "05.1 Scalability (Layer 2)". Aggiungere il link Panopto
- [ ] La slide scrive "Arbitrium": il progetto si chiama **Arbitrum**
- [ ] Polygon: la slide lo presenta come sidechain ("10× più veloce"). Oggi l'ecosistema Polygon include anche zk-rollup (zkEVM, AggLayer): capire se il Prof. si riferisce solo a Polygon PoS
- [ ] Optimistic rollup: la slide parla di fault proof "per una singola transazione" e poi di verifica di tutte le transizioni del batch. Nei sistemi reali (Arbitrum) si usa una bisezione interattiva: chiedere quale versione serve all'esame
- [ ] Il Prof. ha dato indicazioni più precise su CCIP per il project work?

---

> **Fonti e verifica.** Slide del corso (Sidechains, Polygon, Plasma, Rollups, Rollups vs Sidechain, Optimistic Rollups, Zero-Knowledge Rollups, Fraudulent rollups, Disputes take time, The Need for Bridges, Types of Bridges, Lock-and-Mint, Use of Oracles, Some bridges, Chainlink CCIP, Cons) e appunti presi dalla videolezione del 19/10/2026 (parziali). Dalla letteratura (non in slide): whitepaper di Plasma (Poon, Buterin, 2017) e problema del data withholding, distinzione stretta sidechain/L2, attacchi Ronin e Wormhole (2022), dettagli dei componenti CCIP. Il codice Python è stato eseguito e i contratti Solidity compilano con solc 0.8.20; sono aggiunte didattiche, non presenti nelle slide.

[← Indice](README.md)
