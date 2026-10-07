# Lezione 5 — Smart contracts e token

[Lezione del 5 ottobre 2026 – Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3627f577-fbb1-4cb9-a36a-b4db0067f928)

*Slide di riferimento: Smart contracts*

---

## Smart contract: inquadramento

Definizione molto generale, il codice per ora non lo vediamo. Presentazione breve, dopodiché si passa ai **token**, l'altro aspetto importante già menzionato nelle lezioni precedenti.

L'idea non è nuova: è stata proposta circa 30 anni fa da **Nick Szabo** (1994). Il concetto di un programma che si comporta come una sorta di contratto era però introdotto in un contesto diverso (non esisteva la blockchain); alcuni aspetti restano comunque attuali.

### Szabo (1994): computerized transaction protocol

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/5b22ad8a-36b3-41a2-b50b-2a47e087a591" />

Uno smart contract è un **protocollo di transazione computerizzato** che esegue i termini di un contratto.

- **Obiettivi generali**
  - soddisfare le condizioni contrattuali comuni: termini di pagamento, garanzie (*liens*), riservatezza, perfino l'*enforcement*
  - **minimizzare le eccezioni**, sia malevole sia accidentali
  - **minimizzare il bisogno di intermediari fidati**
- **Obiettivi economici**: ridurre perdite da frode, costi di arbitrato ed enforcement, e in generale i costi di transazione

Il problema principale resta la fiducia (*trust*): l'idea è spostarla dalla controparte/intermediario al codice, che esegue automaticamente quanto pattuito.

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/3c50f269-c90a-41b0-b069-314500e31351" />

### Smart contract come programmi su blockchain

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/f8f4f252-7089-4f9b-bc03-941e729715ca" />

Oggi: **programmi definiti dall'utente che girano sopra una blockchain**.

- Gli utenti interagiscono con i contratti scambiando **denaro** e **dati** (tramite transazioni)
- Ogni contratto = **codice + storage** (stato persistente)
- Esecuzione e stato sono garantiti dal **consenso decentralizzato**: nessuna parte singola può alterare il risultato

### Flessibilità

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/9ebbd44e-a8b5-4aeb-8d84-c344695fd68c" />

- Uno smart contract può essere scritto in un linguaggio **Turing completo**
  - **Non in Bitcoin** (Script volutamente limitato)
  - **Ethereum** sì
- Può fare *qualsiasi cosa* faccia un normale computer
- **Ma si paga**: il codice viene eseguito in parallelo da **tutti i nodi** della rete → ogni computazione ha un costo (anticipa il concetto di *gas*)

### Trasparenza

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/9b2ddca9-73b3-444b-80a0-0a34644cd2d1" />

- <!-- da completare con il contenuto della slide -->

### Applicazioni

<!-- screenshot "Smart Contract Applications" (elenco) da caricare -->

I contratti si possono usare per costruire:

- valute
- derivati finanziari
- sistemi di voto
- organizzazioni decentralizzate (DAO)
- *data feeds* (dati dal mondo esterno → oracoli)
- registri di titoli/proprietà
- ...

<!-- screenshot "Smart contracts – simple to complex" (spettro PwC) da caricare -->

Spettro dal semplice al complesso:

| Livello | Esempio |
|---|---|
| Digital value exchange | invio di bitcoin a un familiare |
| Smart right and obligation | acquisto di uno stream di contenuti digitali |
| Basic smart contract | il locatore blocca da remoto l'appartamento all'inquilino moroso |
| Multiparty smart contract | prestito dal venditore all'acquirente per comprare casa |
| Distributed autonomous business unit | unità aziendale che emette bond, pagamenti monitorati su ledger condiviso |
| Distributed autonomous organization | camion a guida autonoma che fanno consegne P2P e pagano pedaggi/energia |
| Distributed autonomous government | coloni di un'area disabitata che codificano servizi pubblici auto-applicanti |
| Distributed autonomous society | gruppi di coloni che stabiliscono accordi commerciali auto-applicanti |

### Esempio: CryptoKitties (digital marketplace)

<!-- screenshot CryptoKitties -->

- Gioco in cui gli utenti **collezionano e fanno riprodurre gattini virtuali** tramite smart contract su Ethereum
- I gattini si **comprano pagando in ether**
- Ogni gattino è unico e la sua proprietà è registrata on-chain: è un **token non fungibile** (ERC-721, vedi [sezione NFT](#erc-721-nft))
- Anche la riproduzione (*breeding*) è logica del contratto: il nuovo gattino eredita caratteristiche dai genitori

### Da smart contract a DApp

<!-- screenshot "Smart Contracts → Dapps" -->

- **Smart contract**: protocollo di transazione che esegue i termini di un contratto (la definizione di Szabo)
- **DApp** (*Decentralized Application*): **contratto + interfaccia grafica** per eseguirlo
  - **Smart contract** → memorizzati **sulla blockchain** (logica e stato)
  - **User interface** → memorizzata su un **file system decentralizzato** (es. IPFS)
- L'utente finale non chiama il contratto a mano: usa l'interfaccia, che costruisce e invia le transazioni al contratto
- CryptoKitties è un esempio di DApp: contratto su Ethereum + sito web per comprare e far riprodurre i gattini

### Web site vs DApp

<!-- screenshot "Web site vs Dapp" -->

| | Catena | Chi controlla il back-end |
|---|---|---|
| **Sito convenzionale** | Front End → **API** → **Database** | il gestore del sito (server e DB centralizzati) |
| **Sito "dApp empowered"** | Front End → **Smart Contract** → **Blockchain** | nessun gestore unico: logica e dati sono on-chain |

- Il front end resta simile: cambia ciò che c'è dietro
- Lo **smart contract prende il posto delle API** (la logica applicativa)
- La **blockchain prende il posto del database** (lo stato), con dati replicati, trasparenti e non modificabili dal singolo gestore
- Prezzo da pagare: ogni scrittura è una transazione, quindi costa e non è istantanea

### Architettura Web 2.0 vs Web 3.0

<!-- screenshot "Web site vs Dapp" (architettura Web 2.0 / Web 3.0) -->

| Livello | Web 2.0 | ≈ | Web 3.0 |
|---|---|---|---|
| Client | Browser | | Browser + **Wallet** (es. MetaMask) |
| Frontend | HTML / JS / CSS | ≈ | HTML / JS / CSS |
| Accesso alla rete | — | | **Node provider** (Infura, QuickNode, Alchemy, ...) |
| Logica | Backend (Node, Python, Java, Ruby, ...) | ≈ | Smart contract (Solidity, Vyper, Rust, ...) |
| Dati | Storage (Mongo, Firebase, ...) | ≈ | Blockchain (Ethereum, Polygon, Solana, ...) |

Due elementi nuovi rispetto al Web 2.0:

- **Wallet**: custodisce le chiavi dell'utente e **firma le transazioni**; l'identità è l'indirizzo, non un account username/password sul server
- **Node provider**: il frontend non parla direttamente con la blockchain, ma passa da un nodo (gestito da un provider) che legge lo stato e inoltra le transazioni

> Attenzione: wallet e node provider sono spesso servizi centralizzati, quindi nella pratica una DApp non è decentralizzata al 100%.

*Fonte figura: Towards Data Science, "Decoding Ethereum smart contract data"*

### Esempio: licenza (contratto legale)

Spunto: Solidity come linguaggio per scrivere smart contract su Ethereum.

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/2dfbfeaa-4831-4dc9-a947-5493481cc133" />

Licenza per la valutazione di un prodotto, 5 articoli:

1. Il licenziante concede al licenziatario la licenza di valutare il prodotto
2. Vietato pubblicare i risultati senza approvazione preventiva; se pubblica senza approvazione ha **24 h per rimuovere**
3. Vietato pubblicare commenti, a meno che non sia autorizzato a pubblicare i risultati
4. Se è **commissionato** per una valutazione indipendente, ha l'**obbligo** di pubblicare
5. La licenza termina automaticamente in caso di violazione

### Esempio: licenza come macchina a stati

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/a6ebec72-9815-4cdd-bafb-1b6e60b08713" />

Lo stesso contratto tradotto in un automa a stati finiti:

| Stato | Significato |
|---|---|
| 1 | iniziale, nessuna licenza |
| 2 | licenza attiva (può solo usare) |
| 3 | approvazione ottenuta: può usare, pubblicare, commentare, rimuovere |
| 4 | commissionato: obbligo di pubblicare |
| 5 | pubblicato senza approvazione: finestra per rimuovere |
| 6 | **violazione → licenza terminata** (stato assorbente) |

Transizioni principali:

- 1 → 2 *has license*; 1 → 6 se usa/pubblica/commenta senza licenza
- 2 → 3 *has approval*; 2 → 4 *is commissioned*; 2 → 5 *publish*; 2 → 6 *comment*
- 5 → 2 *remove* (entro 24 h); 5 → 6 *no remove* o *comment*; 5 → 4 *is commissioned*
- 4 → 3 *publish*; 4 → 6 *no publish*
- 3 → 4 *is commissioned*

Morale: un contratto legale si può formalizzare come macchina a stati, quindi come codice. Le parti delicate sono quelle legate al **tempo** (24 h, "non ha pubblicato") e agli **eventi esterni** (approvazione, commissione), che il contratto on-chain non osserva da solo.

---

## Tokens

Con gli smart contract si possono sviluppare molte applicazioni diverse, ma di solito prevedono qualcosa che gli utenti possono scambiare: in genere parliamo di **token**.

<img width="60%" height="60%" alt="image" src="https://github.com/user-attachments/assets/eca7600e-51a3-4d12-8784-e68b961955a1" />

Un token è un **dato digitale che rappresenta un "fatto"**: un valore, un diritto, la proprietà di un bene. Cosa si può tokenizzare? Immobili, valute, opere, diritti d'accesso, ecc.

Nel nostro scenario un token è **gestito da uno smart contract** che gira sopra una blockchain: il contratto tiene il registro di chi possiede quanti token e definisce le regole per trasferirli.

I token si possono ottenere:
- **comprandoli**
- **guadagnandoli** svolgendo determinate attività (es. come ricompensa per un servizio)

Il prezzo di un token sale o scende in base a **domanda e offerta**.

### ERC-20: implementazione di base

<!-- screenshot "ERC-20 Basic Implementation Excerpt" (variabili + constructor) -->

Stato del contratto:

```solidity
contract ERC20 {
    uint256 constant totalSupply_;                                    // numero totale di token
    mapping(address => uint256) balances;                             // saldo di ogni indirizzo
    mapping(address => mapping (address => uint256)) allowed;         // quanto un indirizzo può spendere per conto di un altro

    // crea i token, tutti assegnati al creatore
    function constructor(uint256 total) public {
        totalSupply_ = total;
        balances[msg.sender] = _totalSupply;
    }
}
```

- `balances`: è il **registro dei saldi**, il cuore del token. Possedere token = avere un numero associato al proprio indirizzo in questa mappa
- `allowed`: gestisce le **deleghe** (*allowance*): A autorizza B a spendere fino a N token suoi (usato da `approve` / `transferFrom`)
- `constructor`: eseguito una sola volta al deploy; `msg.sender` è chi pubblica il contratto e riceve tutta la supply iniziale

<!-- screenshot "ERC-20 Basic Implementation Excerpt" (balanceOf) -->

```solidity
function balanceOf(address tokenOwner) public view returns (uint256) {
    return balances[tokenOwner];
}
```

- Funzione `view`: **legge** lo stato senza modificarlo → non serve una transazione, non costa gas se chiamata dall'esterno

<!-- screenshot "ERC-20 Basic Implementation Excerpt" (transfer) -->

```solidity
function transfer(address receiver, uint256 numTokens) public returns (bool) {
    require(numTokens <= balances[msg.sender]);
    balances[msg.sender] = balances[msg.sender] - numTokens;
    balances[receiver] = balances[receiver] + numTokens;
    emit Transfer(msg.sender, receiver, numTokens);
    return true;
}
```

1. `require`: controlla che il mittente abbia saldo sufficiente, altrimenti la transazione viene annullata (*revert*)
2. scala i token dal mittente
3. li aggiunge al destinatario
4. `emit Transfer`: emette un **evento**, registrato nei log della transazione, che wallet ed explorer usano per tracciare i trasferimenti

Un "trasferimento di token" quindi non sposta nulla: **aggiorna due righe di una mappa** dentro il contratto.

> Nota: l'estratto è semplificato e non compilerebbe così com'è (`totalSupply_` dichiarata `constant` ma assegnata nel constructor, `_totalSupply` vs `totalSupply_`, `function constructor` è sintassi vecchia). Serve a capire la logica, non come codice reale.

### Implementazioni note

<!-- screenshot "Famous Implementations" -->

Gli smart contract si possono scrivere da zero, ma **una volta caricati sulla blockchain non si possono modificare né cancellare**: un bug resta lì per sempre (e può costare soldi veri). Per questo conviene partire da implementazioni già note e verificate:

- **OpenZeppelin**: libreria open source (repository su GitHub) di contratti standard e controllati, tra cui l'implementazione di ERC-20; di fatto il punto di partenza più usato
- **ConsenSys**: altra implementazione di riferimento
- Tutorial con codice su GitHub: *how to issue your own token on Ethereum in less than 20 minutes*

### ERC-721 (NFT)

<!-- screenshot "ERC721 (NFT)" -->

- Proposto inizialmente per gestire **atti di proprietà** (*deeds*)
- **Non-fungible token**: ogni token è **unico e non intercambiabile** con gli altri
- Obiettivo: un'**interfaccia standard** per creare e scambiare token distinguibili che rappresentano beni digitali o fisici (es. figurine da collezione, come nella slide)

| | Fungibile (ERC-20) | Non fungibile (ERC-721) |
|---|---|---|
| Unità | tutte uguali e intercambiabili | ognuna unica (`tokenId`) |
| Cosa registra il contratto | quanti token ha ogni indirizzo | quale indirizzo possiede ogni token |
| Esempio | valuta, punti fedeltà | gattino CryptoKitties, opera digitale |

Esempi:

- **CryptoKitties** (token ERC-721): hanno avuto un momento di popolarità enorme, con gattini scambiati a valutazioni altissime
- **Beeple**: opere video vendute come NFT a cifre milionarie
- **Game 5 Ball**: altro esempio citato <!-- verificare -->

### ERC-721: interfaccia (semplificata)

<!-- screenshot "ERC721 Token interface" -->

```solidity
contract ERC721 {
    // funzioni compatibili con ERC-20
    function name() constant returns (string name);
    function symbol() constant returns (string symbol);
    function totalSupply() constant returns (uint totalSupply);
    function balanceOf(address _owner) constant returns (uint balance);
    // funzioni che definiscono la proprietà
    function ownerOf(uint _tokenId) constant returns (address _owner);
    function approve(address _to, uint _tokenId);
    function takeOwnership(uint _tokenId);
    function transfer(address _to, uint _tokenId) returns (bool success);
    function tokenOfOwnerByIndex(address _owner, uint _index) constant returns (uint tokenId);
    // metadati del token
    function tokenMetadata(uint _tokenId) constant returns (string infoUrl);
    // eventi
    event Transfer(address indexed _from, address indexed _to, uint _tokenId);
    event Approval(address indexed _owner, address indexed _spender, uint _tokenId);
}
```

- **Funzioni compatibili con ERC-20** (`name`, `symbol`, `totalSupply`, `balanceOf`): permettono di inviare token e controllare i saldi come per un token fungibile
- **Proprietà**: la differenza chiave è che si ragiona per **`tokenId`**, non per quantità
  - `ownerOf(tokenId)`: chi possiede quel token specifico
  - `approve` + `takeOwnership`: il proprietario autorizza qualcuno, che poi prende il token
  - `transfer(_to, _tokenId)`: trasferisce *quel* token, non "N token"
  - `tokenOfOwnerByIndex`: elenca i token di un proprietario
- **Metadati**: `tokenMetadata` restituisce un URL con le informazioni sul bene (immagine, descrizione). L'opera vera e propria di solito **non sta on-chain**, ci sta solo il riferimento
- **Eventi**: `Transfer` e `Approval`, come in ERC-20 ma con `tokenId` al posto della quantità

> Nota: è una versione semplificata/bozza; lo standard finale usa `transferFrom`, `safeTransferFrom`, `setApprovalForAll` e `tokenURI`.

### ERC-20 vs ERC-721

<!-- screenshot "ERC20 vs ERC721" -->

- **ERC-20** → token per il **denaro** e ciò che si comporta come denaro
  - una banconota da 5 € vale esattamente quanto qualsiasi altra banconota da 5 € (**fungibilità**)
- **ERC-721** → token per **oggetti da collezione** e "cose" in generale
  - equivalente alle figurine di baseball
  - tante persone hanno un cane, ma *quel* cane è il loro e non lo scambierebbero con un altro: con ERC-721 si possono rappresentare quei cani e la loro proprietà

Regola pratica: se due unità sono intercambiabili → ERC-20; se conta *quale* unità possiedi → ERC-721.

### NFT e IPFS

<!-- screenshot "NFTs and IPFS" -->

Come si crea un NFT:

1. **Crea l'artefatto** (immagine, video, ...)
2. **Crea un contratto ERC-721** per coniare (*mint*) l'NFT, eventualmente più NFT
3. **Fai il pin dell'artefatto su IPFS**: il file viene salvato sul file system decentralizzato e resta disponibile finché qualche nodo lo mantiene (*pinning*)
4. **Conia l'NFT**: nel contratto registri il **riferimento IPFS** all'artefatto (il suo identificativo, derivato dal contenuto)

Il punto chiave: **on-chain c'è solo il riferimento**, non l'opera. Costa molto meno, ma se nessuno mantiene il file su IPFS il token punta a qualcosa che non c'è più.

Strumenti citati:

- **OpenSea**: marketplace per comprare e vendere NFT
- **NFT.Storage**: servizio per salvare i file degli NFT su IPFS
- Tutorial NFT per chi è interessato: <!-- link dalla slide -->

### Altro esempio: ERC-1190

<!-- screenshot "Another Example: ERC-1190" -->
<!-- screenshot "Example" (oggetto di gioco) -->

Esempio di chiusura: un **oggetto di gioco** (es. una spada con caratteristiche speciali).

- Il creatore dell'oggetto **incorpora l'oggetto e le informazioni sulla sua proprietà** in un token ERC-1190
- Idea dello standard: gestire **licenze** sugli asset digitali, distinguendo chi **possiede** l'oggetto da chi ne detiene i **diritti creativi** (il creatore può continuare a guadagnare quando l'oggetto viene usato o rivenduto)

### ERC-1155 (multi-token)

- Standard **multi-token**: un solo contratto gestisce sia token **fungibili** sia **non fungibili**
- Nato in ambito gaming: nello stesso contratto possono stare le monete del gioco (fungibili) e gli oggetti unici (non fungibili)
- Permette trasferimenti **in batch** (più token in una sola transazione) → meno gas rispetto a usare contratti ERC-20 e ERC-721 separati

<!-- lezione in corso: aggiungere qui le slide successive -->

---

## Punti su cui insiste il Prof.

> L'idea di smart contract non è nuova (Szabo 1994): la novità è eseguirli su un consenso decentralizzato.
> Obiettivo chiave: ridurre il bisogno di intermediari fidati.
> Turing completezza (Ethereum vs Bitcoin) ha un costo: ogni nodo esegue tutto.
> Un contratto deployato non si può modificare né cancellare → usare implementazioni note (OpenZeppelin, ConsenSys).

## Dubbi da verificare

- [ ] Caricare gli screenshot mancanti (applicazioni, PwC, CryptoKitties, DApp, Web site vs DApp, ERC-20, implementazioni, ERC-721)
- [ ] Completare la sezione *Trasparenza*
- [ ] Beeple: quale opera ha citato il Prof.? (video *Crossroad* o *Everydays: The First 5000 Days*?)
- [ ] "Game 5 Ball": verificare nome e contesto dell'esempio
- [ ] ERC-1190: confermare che il Prof. lo abbia presentato come standard di licenza (proprietà vs diritti creativi)
- [ ] ERC-1155: il Prof. l'ha spiegato o solo nominato?
- [ ] Recuperare il link al tutorial NFT dalla slide
- [ ] Come si gestiscono tempo (24 h) ed eventi esterni in uno smart contract? → oracoli / timestamp del blocco
- [ ] La UI di una DApp è davvero sempre su file system decentralizzato? (spesso in pratica è su server tradizionali)

---

*Lezione in corso di trascrizione: da completare.*
