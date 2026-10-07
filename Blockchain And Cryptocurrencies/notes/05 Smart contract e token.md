# Capitolo 5 — Smart contract e token

| | |
|---|---|
| **Data** | Lunedì 05/10/2026 · Lezione 5 |
| **Macro tema** | Parte IV — Smart contract (e Parte III — Token) |
| **Slide** | 04.00 – Smart Contracts (Reduced) · 04.01 – Tokens · [registrazione Panopto](https://unibo.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3627f577-fbb1-4cb9-a36a-b4db0067f928) |

[← Indice](README.md)

Definizione molto generale degli smart contract (il codice Solidity si vede più avanti), poi i **token**, l'altro tema già anticipato nelle lezioni precedenti.

---

## 1. Fondamenti

### 1.1 L'idea di Szabo (1994) e il problema della fiducia

L'idea non è nuova: la propone **Nick Szabo** circa 30 anni fa, quando la blockchain non esisteva. Alcuni aspetti restano attuali.

<img width="40%" height="40%" alt="Szabo 1994" src="https://github.com/user-attachments/assets/5b22ad8a-36b3-41a2-b50b-2a47e087a591" />

Uno smart contract è un **protocollo di transazione computerizzato** che esegue i termini di un contratto.

- **Obiettivi generali:** soddisfare le condizioni contrattuali comuni (termini di pagamento, garanzie/*liens*, riservatezza, perfino l'*enforcement*), **minimizzare le eccezioni** malevole e accidentali, **minimizzare il bisogno di intermediari fidati**.
- **Obiettivi economici:** ridurre perdite da frode, costi di arbitrato ed enforcement, e in generale i costi di transazione.

**The same old problem… trust** (sequenza di slide):
1. Le persone fanno accordi (*"se ho più di 100 $, do 10 $ ad Alice"*)…
2. …e poi non li rispettano (*"Alice in fondo non se li merita"*).
3. Il software fa ciò per cui è programmato: `if (wallet.balance > 100) then wallet.send(Alice, 10)`.
4. **Ma se non sei tu il programmatore e l'esecutore?** Devi verificare che il software sia quello giusto.
5. **Trust with smart contracts:** il codice è **visibile e verificabile da chiunque**.

La fiducia si sposta dalla controparte/intermediario al **codice**, che esegue automaticamente quanto pattuito.

<img width="40%" height="40%" alt="Trust" src="https://github.com/user-attachments/assets/3c50f269-c90a-41b0-b069-314500e31351" />

### 1.2 Smart contract come programmi su blockchain

<img width="40%" height="40%" alt="Programmi su blockchain" src="https://github.com/user-attachments/assets/f8f4f252-7089-4f9b-bc03-941e729715ca" />

Le valute digitali sono **solo una** delle applicazioni della blockchain. Oggi gli smart contract sono **programmi definiti dall'utente che girano sopra una blockchain**:

- codice memorizzato **nella blockchain**, che funziona come **accordo**; permette di scambiare denaro, proprietà, azioni o qualsiasi cosa di valore **senza intermediario**;
- gli utenti interagiscono con i contratti scambiando **denaro** e **dati** (tramite transazioni);
- ogni contratto = **codice + storage** (stato persistente);
- esecuzione e stato sono garantiti dal **consenso decentralizzato**: nessuna parte singola può alterare il risultato.

Le due proprietà chiave della slide:

<img width="40%" height="40%" alt="Trasparenza" src="https://github.com/user-attachments/assets/9b2ddca9-73b3-444b-80a0-0a34644cd2d1" />

- **Trasparenza:** termini e condizioni sono **accessibili a tutte le parti** e, una volta stabilito il contratto, **non c'è modo di contestarlo**; **tutti i partecipanti eseguono lo stesso codice**, quindi ogni nodo può verificarne la logica. Rovescio: **la privacy può essere un problema**.

<img width="40%" height="40%" alt="Flessibilità" src="https://github.com/user-attachments/assets/9ebbd44e-a8b5-4aeb-8d84-c344695fd68c" />

- **Flessibilità:** il linguaggio può essere **Turing completo** (**non in Bitcoin**, dove Script è volutamente limitato; **sì in Ethereum**), quindi il contratto può fare *qualsiasi cosa* faccia un normale computer. **Ma si paga**: il codice è eseguito in parallelo da **tutti i nodi** della rete, ogni computazione ha un costo (anticipa il *gas*).

### 1.3 Contratti tradizionali vs smart contract

| | Tradizionali | Smart contract |
|---|---|---|
| Chi li scrive | Professionisti legali | Programmatori |
| Linguaggio | Legale, potenzialmente **ambiguo** | Codice di programmazione |
| Esecuzione | Se qualcosa va storto, si ricorre al **sistema giudiziario**: costoso e lento | Eseguiti da un **distributed ledger** |

### 1.4 Token

<img width="60%" height="60%" alt="Token" src="https://github.com/user-attachments/assets/eca7600e-51a3-4d12-8784-e68b961955a1" />

Con gli smart contract si costruiscono molte applicazioni, ma di solito prevedono qualcosa che gli utenti si scambiano: un **token**, cioè un **dato digitale che rappresenta un "fatto"** (un valore, un diritto, la proprietà di un bene). Cosa si può tokenizzare: **immobili, commodity, oggetti da collezione, titoli** (*securities*), valute, diritti d'accesso.

- Un token è **solo uno smart contract** che gira su una blockchain: **codice + database associato**. Il contratto tiene il registro di chi possiede quanti token e definisce le regole per trasferirli.
- Si ottengono **comprandoli** (su un exchange, in valuta fiat) o **guadagnandoli** svolgendo servizi per la rete (es. mining, ricompense).
- Il prezzo sale o scende con **domanda e offerta**, come le azioni: il token è sia la **valuta** per pagare i servizi della rete sia una forma di **partecipazione** (*equity*) alla rete stessa.
- **Token (actually…)** (slide BBS ICO): chi "compra token" da un contratto di ICO non riceve un oggetto, ma una riga nel registro del contratto, come per Alice, Bob e Charlie in slide.

| Tipo di token | Cosa rappresenta |
|---|---|
| **Currency token** | Una criptovaluta |
| **Utility token** | Accesso digitale a un'applicazione o a un servizio |
| **Security token** | Un titolo finanziario negoziabile, **pienamente regolato** in almeno una giurisdizione |

**Fungibile vs non fungibile.** **ERC-20** è il tipo per il **denaro** e ciò che si comporta come denaro: una banconota da 5 € vale esattamente quanto ogni altra (**fungibilità**). **ERC-721** è il tipo per **oggetti da collezione** e "cose": come le figurine di baseball; tante persone hanno un cane, ma *quel* cane è il loro e non lo scambierebbero con un altro, e con ERC-721 si possono rappresentare quei cani e la loro proprietà.

> 💡 **Regola pratica.** Se due unità sono intercambiabili → ERC-20; se conta *quale* unità possiedi → ERC-721.

---

## 2. Architettura

### 2.1 Applicazioni

<!-- screenshot "Smart Contract Applications" (elenco) da caricare -->

I contratti si usano per costruire: **valute**, **derivati finanziari**, **sistemi di voto**, **organizzazioni decentralizzate (DAO)**, ***data feeds*** (dati dal mondo esterno → oracoli), **registri di titoli/proprietà**…

<!-- screenshot "Smart contracts – simple to complex" (spettro PwC) da caricare -->

Spettro dal semplice al complesso (PwC):

| Livello | Esempio |
|---|---|
| Digital value exchange | Invio di bitcoin a un familiare |
| Smart right and obligation | Acquisto di uno stream di contenuti digitali |
| Basic smart contract | Il locatore blocca da remoto l'appartamento all'inquilino moroso |
| Multiparty smart contract | Prestito dal venditore all'acquirente per comprare casa |
| Distributed autonomous business unit | Unità aziendale che emette bond, pagamenti monitorati su ledger condiviso |
| Distributed autonomous organization | Camion a guida autonoma che fanno consegne P2P e pagano pedaggi/energia |
| Distributed autonomous government | Coloni di un'area disabitata che codificano servizi pubblici auto-applicanti |
| Distributed autonomous society | Gruppi di coloni che stabiliscono accordi commerciali auto-applicanti |

**CryptoKitties** (*digital marketplace*) <!-- screenshot CryptoKitties -->: gioco in cui gli utenti **collezionano e fanno riprodurre gattini virtuali** tramite smart contract su Ethereum, **comprandoli in ether**. Ogni gattino è unico e la proprietà è on-chain: è un **token ERC-721**. Anche il *breeding* è logica del contratto (il nuovo gattino eredita caratteristiche dai genitori).

### 2.2 Da smart contract a DApp

<!-- screenshot "Smart Contracts → Dapps" -->

- **Smart contract:** protocollo di transazione che esegue i termini di un contratto (Szabo).
- **DApp** (*Decentralized Application*): **contratto + interfaccia grafica** per eseguirlo. Smart contract **sulla blockchain** (logica e stato); user interface su un **file system decentralizzato** (es. IPFS).
- L'utente non chiama il contratto a mano: usa l'interfaccia, che costruisce e invia le transazioni. CryptoKitties è una DApp: contratto su Ethereum + sito per comprare e far riprodurre i gattini.

<!-- screenshot "Web site vs Dapp" -->

| | Catena | Chi controlla il back-end |
|---|---|---|
| **Sito convenzionale** | Front End → **API** → **Database** | Il gestore del sito (server e DB centralizzati) |
| **Sito "dApp empowered"** | Front End → **Smart Contract** → **Blockchain** | Nessun gestore unico: logica e dati on-chain |

Il front end resta simile, cambia ciò che sta dietro: lo **smart contract prende il posto delle API** (logica), la **blockchain prende il posto del database** (stato), con dati replicati, trasparenti e non modificabili dal singolo gestore. Prezzo: ogni scrittura è una transazione, quindi costa e non è istantanea.

<!-- screenshot "Web site vs Dapp" (architettura Web 2.0 / Web 3.0) -->

| Livello | Web 2.0 | ≈ | Web 3.0 |
|---|---|---|---|
| Client | Browser | | Browser + **Wallet** (es. MetaMask) |
| Frontend | HTML / JS / CSS | ≈ | HTML / JS / CSS |
| Accesso alla rete | — | | **Node provider** (Infura, QuickNode, Alchemy…) |
| Logica | Backend (Node, Python, Java, Ruby…) | ≈ | Smart contract (Solidity, Vyper, Rust…) |
| Dati | Storage (Mongo, Firebase…) | ≈ | Blockchain (Ethereum, Polygon, Solana…) |

*Fonte figura: Towards Data Science, "Decoding Ethereum smart contract data".*

- **Wallet:** custodisce le chiavi e **firma le transazioni**; l'identità è l'indirizzo, non username/password sul server.
- **Node provider:** il frontend non parla direttamente con la blockchain, ma con un nodo (gestito da un provider) che legge lo stato e inoltra le transazioni.

**Dapp projects:** portali simili a quelli delle ICO per esplorare le DApp (dappradar.com, dapp.review, dappt.io). Esempio in slide: **Upland**, compravendita immobiliare in un **metaverso** su blockchain.

### 2.3 Gli standard ERC

Gli **ERC** (*Ethereum Request for Comments*) definiscono interfacce comuni: chi sviluppa una DApp le segue perché il token funzioni senza problemi con **wallet, exchange e altri contratti**.

**ERC-20 (token fungibili).** Un insieme di **6 funzioni** riconoscibili da altri contratti, che realizzano 4 attività di base: ottenere la **supply totale**, il **saldo** di un account, **trasferire** token, **approvare** l'uso dei token da parte di altri.

```solidity
// https://github.com/ethereum/EIPs/issues/20  — interfaccia ERC-20 (slide)
pragma solidity ^0.4.0;
contract ERC20 {
    string public constant NAME = "Token Name";
    string public constant SYMBOL = "SYM";
    uint8 public constant DECIMALS = 18;   // numero di decimali più comune
    function totalSupply() constant returns (uint totalSupply);                    // supply totale
    function balanceOf(address _owner) constant returns (uint balance);            // saldo di _owner
    function transfer(address _to, uint _value) returns (bool success);            // invia _value a _to
    function transferFrom(address _from, address _to, uint _value) returns (bool success); // da _from a _to
    function approve(address _spender, uint _value) returns (bool success);        // delega fino a _value
    function allowance(address _owner, address _spender) constant returns (uint remaining); // delega residua
    event Transfer(address indexed _from, address indexed _to, uint _value);
    event Approval(address indexed _owner, address indexed _spender, uint _value);
}
```

`approve` permette a `_spender` di prelevare dal tuo account **più volte, fino a `_value`**; una nuova chiamata **sovrascrive** la delega corrente.

**Implementazione di base (estratto delle slide).** <!-- screenshot "ERC-20 Basic Implementation Excerpt" -->

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

- `balances`: il **registro dei saldi**, il cuore del token. Possedere token = avere un numero associato al proprio indirizzo in questa mappa.
- `allowed`: le **deleghe** (*allowance*): A autorizza B a spendere fino a N token suoi (usato da `approve` / `transferFrom`).
- `constructor`: eseguito una sola volta al deploy; `msg.sender` è chi pubblica il contratto e riceve tutta la supply iniziale.

```solidity
function balanceOf(address tokenOwner) public view returns (uint256) {
    return balances[tokenOwner];
}
```

Funzione `view`: **legge** lo stato senza modificarlo → non serve una transazione, non costa gas se chiamata dall'esterno.

```solidity
function transfer(address receiver, uint256 numTokens) public returns (bool) {
    require(numTokens <= balances[msg.sender]);
    balances[msg.sender] = balances[msg.sender] - numTokens;
    balances[receiver] = balances[receiver] + numTokens;
    emit Transfer(msg.sender, receiver, numTokens);
    return true;
}
```

1. `require`: controlla che il mittente abbia saldo sufficiente, altrimenti la transazione viene annullata (*revert*);
2. scala i token dal mittente;
3. li aggiunge al destinatario;
4. `emit Transfer`: emette un **evento**, registrato nei log della transazione, che wallet ed explorer usano per tracciare i trasferimenti.

Un "trasferimento di token" quindi non sposta nulla: **aggiorna due righe di una mappa** dentro il contratto.

```solidity
function approve(address delegate, uint256 numTokens) public returns (bool) {
    allowed[msg.sender][delegate] = numTokens;
    emit Approval(msg.sender, delegate, numTokens);
    return true;
}

function transferFrom(address owner, address buyer, uint256 numTokens) public returns (bool) {
    require(numTokens <= balances[owner]);
    require(numTokens <= allowed[owner][msg.sender]);
    balances[owner] = balances[owner] - numTokens;
    allowed[owner][msg.sender] = allowed[from][msg.sender] - numTokens;
    balances[buyer] = balances[buyer] + numTokens;
    emit Transfer(owner, buyer, numTokens);
    return true;
}
```

`transferFrom` è il "prelievo delegato": chi chiama (`msg.sender`) sposta token di `owner` verso `buyer`, entro la delega ricevuta.

> ⚠️ **Nota di rigore.** L'estratto è semplificato e non compilerebbe così com'è: `totalSupply_` è `constant` ma assegnata nel constructor, `_totalSupply` vs `totalSupply_`, `function constructor` è sintassi vecchia, e in `transferFrom` compare `allowed[from]` invece di `allowed[owner]`. Serve a capire la logica: una versione compilabile è nel §4.2.

**Implementazioni note.** <!-- screenshot "Famous Implementations" --> Gli smart contract si possono scrivere da zero, ma **una volta caricati non si possono modificare né cancellare**: un bug resta lì per sempre (e può costare soldi veri). Conviene partire da implementazioni note e verificate:
- **OpenZeppelin:** framework open source di contratti riutilizzabili per Ethereum e altre blockchain EVM; **orientato alla sicurezza** (pattern standard e best practice), **modulare** (codice semplice, solo l'essenziale); contiene l'implementazione di ERC-20 ed è di fatto il punto di partenza più usato;
- **ConsenSys:** altra implementazione di riferimento;
- tutorial su GitHub: *how to issue your own token on Ethereum in less than 20 minutes*.

**ERC-721 (NFT).** <!-- screenshot "ERC721 (NFT)" --> Proposto inizialmente per gestire **atti di proprietà** (*deeds*). **Non-fungible token**: ogni token è **unico e non intercambiabile**. Obiettivo: un'**interfaccia standard** per creare e scambiare token distinguibili che rappresentano beni digitali o fisici.

| | Fungibile (ERC-20) | Non fungibile (ERC-721) |
|---|---|---|
| Unità | Tutte uguali e intercambiabili | Ognuna unica (`tokenId`) |
| Cosa registra il contratto | Quanti token ha ogni indirizzo | Quale indirizzo possiede ogni token |
| Esempio | Valuta, punti fedeltà | Gattino CryptoKitties, opera digitale |

Esempi in slide:
- **CryptoKitties:** ogni gattino è un token ERC-721; momento di popolarità enorme, con un gattino venduto per **172.000 $** (CNET). Su OpenSea e sull'explorer NFT di blockchain.com si vedono i "supermercati" di NFT.
- **Beeple:** opere video vendute come NFT su Nifty Gateway e il collage *Everydays: The First 5000 Days*, venduto da Christie's per **69 milioni $** (marzo 2021).
- **Gucci's Ghost:** NFT su Nifty Gateway.
- **Game 5 Ball** (game5ball.com): altro progetto citato in slide.

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

- **Compatibili con ERC-20** (`name`, `symbol`, `totalSupply`, `balanceOf`): inviare token e controllare i saldi come per un token fungibile; `name`/`symbol` dicono a contratti e applicazioni esterne nome e sigla.
- **Proprietà:** si ragiona per **`tokenId`**, non per quantità. `ownerOf(tokenId)`: chi possiede quel token; `approve`: autorizza un altro a trasferire il token per conto del proprietario; `takeOwnership`: agisce come un **prelievo**, chi è stato approvato prende il token dal saldo altrui; `transfer(_to, _tokenId)`: trasferisce *quel* token; `tokenOfOwnerByIndex`: un proprietario può avere più token, recuperabili per indice.
- **Metadati:** ciò che rende unico un NFT sono i suoi attributi, ma salvarli on-chain è **molto costoso**: si salvano **riferimenti** (hash IPFS o link HTTPS), cioè *dati sui dati*. `tokenMetadata` restituisce quel riferimento; l'opera vera di solito **non sta on-chain**.
- **Eventi:** `Transfer` (il token cambia proprietario) e `Approval`, come in ERC-20 ma con `tokenId` al posto della quantità.

> ⚠️ **Nota di rigore.** È una versione semplificata/bozza: lo standard finale (EIP-721) usa `transferFrom`, `safeTransferFrom`, `setApprovalForAll` e `tokenURI`.

**NFT e IPFS.** <!-- screenshot "NFTs and IPFS" -->
1. **Crea l'artefatto** (immagine, video…);
2. **crea un contratto ERC-721** per coniare (*mint*) l'NFT, eventualmente più NFT;
3. **fai il pin dell'artefatto su IPFS**: resta disponibile finché qualche nodo lo mantiene (*pinning*);
4. **conia l'NFT**: nel contratto registri il **riferimento IPFS** all'artefatto (identificativo derivato dal contenuto).

```solidity
// NFT Contract (Simplified), dalle slide
contract MyNFTs is ERC721 {
    private uint256 _tokenIds;
    mapping (uint256 => string) private _tokenURIs;

    constructor() ERC721("MyNFT", "MNFT") {}
    function _setTokenURI(uint256 tokenId, string _tokenURI) {
        _tokenURIs[tokenId] = _tokenURI;
    }
    function tokenURI(uint256 tokenId) returns (string memory) {
        string memory _tokenURI = _tokenURIs[tokenId];
        return _tokenURI;
    }
    function mint(address recipient, string memory uri) returns (uint256) {
        _tokenIds += 1;
        uint256 newItemId = _tokenIds;
        _mint(recipient, newItemId);   // OpenZeppelin: conia e assegna a recipient
        _setTokenURI(newItemId, uri);
        return newItemId;
    }
}
```

Il punto chiave: **on-chain c'è solo il riferimento**, non l'opera. Costa molto meno, ma se nessuno mantiene il file su IPFS il token punta a qualcosa che non c'è più ([Capitolo 3](<03 Smart Transportation.md>), §2.3: persistenza).

Strumenti citati: **OpenSea** (*"the largest NFT marketplace"*), **NFT.Storage** (carica i file degli NFT su IPFS e restituisce le informazioni per recuperarli). Tutorial in slide: *Writing an NFT Collectible Smart Contract* (Medium, Scrappy Squirrels), guida QuickNode *Create and deploy an ERC-721* (contratto + contenuto su IPFS), *How to Build a Profitable NFT Marketplace with React, Solidity, and CometChat* (dev.to).

**ERC-1190 (royalty).** <!-- screenshot "Another Example: ERC-1190" e "Example" (oggetto di gioco) --> NFT per il **pagamento di royalty**: il creatore di un oggetto digitale unico (opera, oggetto di gioco) **guadagna automaticamente ogni volta che i diritti su quell'oggetto vengono usati**. Distingue la **licenza di proprietà** (*ownership license*) dalla **licenza creativa** (*creative license*). Tipi di transazione: vendita della licenza di proprietà, vendita della licenza creativa, **noleggio** dell'asset a terzi per un periodo fisso.

Esempio: un **oggetto di gioco** (es. una spada speciale); il creatore incorpora oggetto e informazioni di proprietà in un token ERC-1190.
- **Caso 1 — il creatore tiene la licenza creativa e vende quella di proprietà:** incassa tutta la prima vendita. Il giocatore usa l'oggetto quanto vuole; se l'oggetto diventa famoso e lo rivende, tiene la maggior parte del ricavo e una **quota fissa va automaticamente** al titolare della licenza creativa. Se lo noleggia, il creatore riceve una parte del noleggio; il proprietario decide in esclusiva e tiene la maggioranza dei ricavi.
- **Caso 2 — il creatore vende la licenza creativa:** il nuovo titolare riceve una quota di **tutte le royalty future** su qualsiasi transazione dell'asset.

**ERC-1155 (multi-token).** Combina i vantaggi di fungibili e non fungibili.
- ERC-721: **un contratto per token**; trasferire più NFT = più operazioni = costi alti. ERC-1155: **più token in un solo contratto**, con **trasferimenti in batch** → meno gas.
- Supporta token fungibili e non fungibili **nello stesso contratto** (nato in ambito gaming: monete del gioco accanto agli oggetti unici).
- **Semi-fungible token:** fungibili durante lo scambio, diventano NFT al **riscatto**. Esempio: un biglietto è fungibile prima del concerto e diventa un ricordo (*memorabilia*) dopo, perdendo valore di scambio.

### 2.4 Applicazioni basate su token: raccolta fondi e DAO

**ICO (Initial Coin Offering):** modo **non regolato** di raccogliere denaro emettendo token, detto anche *crowdsale*: i sostenitori comprano token in (cripto)valuta e possono avere un **ritorno sull'investimento** (diverso dal crowdfunding, dove si dona). Ethereum è la piattaforma più usata per le ICO.

**STO (Security Token Offering):** contratto di investimento su un **asset reale** sottostante (*security*: strumento finanziario fungibile e negoziabile con valore monetario); la proprietà è registrata on-chain come token e **rispetta la regolazione**: è un ibrido tra ICO e IPO tradizionale. **Regolazione:** la regolano USA (SEC), UK (FCA), Svizzera (FINMA), Singapore, Estonia, Malta…; l'hanno vietata Cina, Corea del Sud, Vietnam, India e altri.

| Metodo | Idea |
|---|---|
| **ICO** | Il progetto emette e vende token direttamente, senza regole |
| **STO** | Token che rappresentano titoli, nel rispetto della regolazione |
| **IEO** (*Initial Exchange Offering*) | Un **exchange** fa da intermediario: il team crea e promuove i token, l'exchange li lista e li distribuisce |
| **IDO** (*Initial DEX Offering*) | Basata su un **exchange decentralizzato** (smart contract), spesso con una **liquidity pool** |

**DAO (Decentralized Autonomous Organization).** Un'organizzazione decentralizzata (DO) è un insieme di persone che interagiscono secondo un **protocollo**; una DAO è una DO **sulla blockchain**: uno smart contract tiene il registro delle quote, il sistema di voto per board e dipendenti, la gestione delle proprietà.

| Elemento | Come funziona |
|---|---|
| **Token** | Proprietà interna di valore, usata per ricompensare attività |
| **Autonomia** | Una volta deployata è indipendente dai creatori; open source; regole e transazioni sulla blockchain |
| **Consenso** | Per spostare fondi serve l'accordo della **maggioranza degli stakeholder** |
| **Contractor** | La DAO non costruisce né scrive codice: nomina contractor tramite voto dei token holder |
| **Proposte e voto** | Le decisioni passano da proposte, con un **deposito** per evitare lo spam, poi si vota |

**TheDAO (2016):** il tentativo più noto; doveva finanziare progetti votati dai possessori di token DAO. **Fallisce in pochi mesi**: una vulnerabilità viene sfruttata per sottrarre **circa 1/3 dei fondi**, e la vicenda porta a un **hard fork** di Ethereum.

**Dash** (dash.org): criptovaluta P2P nata da un fork di Bitcoin, con transazioni più veloci e private, e **governance decentralizzata**: niente CEO, volontari da tutto il mondo.
- **Block reward:** in una blockchain tipica il 100% va ai miner; in Dash **45% ai miner** (*Proof-of-Work*), **45% ai masternode** (*Proof-of-Service*), **10% alla treasury** (budget di governance).
- **Treasury:** finanzia tutto ciò che serve alla rete (sviluppatori, auditor, marketing, traduttori) senza grant, donazioni o sponsor: la DAO è **indipendente**.
- **Masternode:** nodo che dimostra di possedere **almeno 1.000 DASH** (incentivato a decidere bene, perché ne trae profitto) e mantiene una copia della blockchain; **vota quali progetti finanziare**, pagati direttamente dalla blockchain a chi fa il lavoro.
- **Proposte:** pre-proposta sul forum, feedback, proposta on-chain con **fee di 5 DASH**, revisione e voto dei masternode, allocazione del budget; il finanziamento è **revocabile**.
- **Scalare la governance:** se i contractor crescono, i masternode non riescono a valutare tutto → nascono **organizzazioni di finanziamento** che distribuiscono fondi. Esempio: **Dash Watch**, finanziata da una proposta, controlla che i contractor rispettino tempi e budget e riferisce ai masternode.
- *Non trattati in slide:* InstantSend, PrivateSend, pagamenti bancari, semplificazioni d'uso.

---

## 3. Trade-off e attacchi

| Rischio / limite | Perché | Mitigazione |
|---|---|---|
| **Immutabilità del codice** | Un bug deployato resta per sempre | Librerie verificate (OpenZeppelin), audit, test; redeploy o proxy (Cap. 2, §1.3) |
| **Trasparenza vs privacy** | Tutti i nodi vedono stato e logica | Dati off-chain, cifratura (Cap. 2–3) |
| **Costo di esecuzione** | Ogni nodo riesegue tutto | Codice minimale, `view` per le letture, batch (ERC-1155) |
| **Tempo ed eventi esterni** | Il contratto non osserva il mondo | Oracoli; timestamp del blocco per le scadenze |
| **NFT off-chain** | On-chain c'è solo il riferimento | Pinning su IPFS, servizi di storage incentivati |
| **Centralizzazione di fatto** | Wallet e node provider sono spesso servizi centralizzati | Nodo proprio, provider multipli |
| **ICO non regolate** | Raccolte senza tutele | STO, regolazione |
| **Vulnerabilità nelle DAO** | TheDAO: furto di ~1/3 dei fondi | Audit, pattern sicuri (tema di *DeFi Security*) |

> ⚠️ **Nota di rigore (tempo ed eventi esterni).** Nell'esempio della licenza le parti delicate sono le **24 h** e il **"non ha pubblicato"**, e gli eventi **approvazione** e **commissione**. Il contratto non ha un orologio né vede il mondo: si eseguono solo quando arriva una transazione. Per le scadenze si confronta il **timestamp del blocco** con una deadline salvata; gli eventi esterni arrivano da un **oracolo** o da una transazione firmata da chi ne ha l'autorità.

> ⚠️ **Nota di rigore (DApp).** "UI su file system decentralizzato" è il modello delle slide: in pratica molte DApp servono il front end da server tradizionali e passano da wallet e node provider centralizzati, quindi non sono decentralizzate al 100%.

> ⚠️ **Nota di rigore (ERC-20 `approve`).** Poiché `approve` sovrascrive la delega, cambiarla da N a M può permettere allo spender di spendere N **prima** che il cambio venga minato e poi altri M (*front-running*). Si azzera prima la delega o si usano funzioni di incremento/decremento.

> 💡 **TheDAO (dalla letteratura).** Giugno 2016, attacco di **reentrancy** (il contratto inviava ether prima di aggiornare il saldo), circa 3,6 milioni di ETH. Il fork di luglio 2016 restituisce i fondi e divide la comunità: chi lo rifiuta continua con **Ethereum Classic**. Esempio da manuale di *code is law* messo in crisi.

---

## 4. Esempi e codice

### 4.1 Esempio: la licenza da contratto legale a macchina a stati

Esempio delle slide da Governatori et al. (2018). Spunto: Solidity come linguaggio per scrivere smart contract su Ethereum.

<img width="40%" height="40%" alt="Licenza" src="https://github.com/user-attachments/assets/2dfbfeaa-4831-4dc9-a947-5493481cc133" />

Licenza per la valutazione di un prodotto, 5 articoli:
1. Il licenziante concede al licenziatario la licenza di valutare il prodotto.
2. Vietato pubblicare i risultati senza approvazione preventiva; se pubblica senza approvazione ha **24 h per rimuovere**.
3. Vietato pubblicare commenti, a meno che non sia autorizzato a pubblicare i risultati.
4. Se è **commissionato** per una valutazione indipendente, ha l'**obbligo** di pubblicare.
5. La licenza termina automaticamente in caso di violazione.

<img width="40%" height="40%" alt="Licenza come macchina a stati" src="https://github.com/user-attachments/assets/a6ebec72-9815-4cdd-bafb-1b6e60b08713" />

| Stato | Significato |
|---|---|
| 1 | Iniziale, nessuna licenza |
| 2 | Licenza attiva (può solo usare) |
| 3 | Approvazione ottenuta: può usare, pubblicare, commentare, rimuovere |
| 4 | Commissionato: obbligo di pubblicare |
| 5 | Pubblicato senza approvazione: finestra per rimuovere |
| 6 | **Violazione → licenza terminata** (stato assorbente) |

Transizioni principali:
- 1 → 2 *has license*; 1 → 6 se usa/pubblica/commenta senza licenza
- 2 → 3 *has approval*; 2 → 4 *is commissioned*; 2 → 5 *publish*; 2 → 6 *comment*
- 5 → 2 *remove* (entro 24 h); 5 → 6 *no remove* o *comment*; 5 → 4 *is commissioned*
- 4 → 3 *publish*; 4 → 6 *no publish*
- 3 → 4 *is commissioned*

La slide successiva mostra la stessa licenza scritta come **smart contract**. In Python:

```python
T = {                                  # (stato, evento) -> nuovo stato
    (1, "has_license"): 2,   (1, "use"): 6, (1, "publish"): 6, (1, "comment"): 6,
    (2, "has_approval"): 3,  (2, "is_commissioned"): 4, (2, "publish"): 5, (2, "comment"): 6,
    (5, "remove"): 2,        (5, "no_remove"): 6, (5, "comment"): 6, (5, "is_commissioned"): 4,
    (4, "publish"): 3,       (4, "no_publish"): 6,
    (3, "is_commissioned"): 4,
}

def run(eventi, s=1):
    for e in eventi:
        s = T.get((s, e), s)           # evento non previsto: stato invariato
        if s == 6:
            return "6: licenza terminata"
    return s

print(run(["has_license", "publish", "remove"]))           # 2: rimosso entro 24 h
print(run(["has_license", "publish", "no_remove"]))        # 6: licenza terminata
print(run(["has_license", "is_commissioned", "publish"]))  # 3
```

Morale: un contratto legale si può formalizzare come macchina a stati, quindi come codice. Eventi come `no_remove` e `no_publish` sono **l'assenza di un'azione entro un tempo**: on-chain diventano un controllo sul timestamp (§3).

### 4.2 ERC-20 minimale e compilabile (Solidity 0.8)

Versione corretta dell'estratto delle slide (verificata con `solc` 0.8.26):

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MiniToken {
    string public constant name = "MiniToken";
    string public constant symbol = "MTK";
    uint8 public constant decimals = 18;
    uint256 public immutable totalSupply;                 // fissata al deploy

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 total) {
        totalSupply = total;
        balanceOf[msg.sender] = total;                    // tutta la supply al creatore
        emit Transfer(address(0), msg.sender, total);
    }

    function transfer(address to, uint256 value) external returns (bool) {
        require(balanceOf[msg.sender] >= value, "saldo insufficiente");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external returns (bool) {
        allowance[msg.sender][spender] = value;           // sovrascrive la delega
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(balanceOf[from] >= value, "saldo insufficiente");
        require(allowance[from][msg.sender] >= value, "delega insufficiente");
        allowance[from][msg.sender] -= value;
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
        return true;
    }
}
```

Le variabili `public` generano da sole i getter `balanceOf(addr)`, `allowance(a, b)` e `totalSupply()` richiesti dallo standard. Da Solidity 0.8 l'overflow fa *revert* da solo. In pratica: `import "@openzeppelin/contracts/token/ERC20/ERC20.sol";` e si eredita.

---

## 5. Quadro di riepilogo

> 💡 **Punti su cui insiste il Prof.** L'idea di smart contract non è nuova (Szabo 1994): la novità è eseguirli su un **consenso decentralizzato**. Obiettivo chiave: **ridurre il bisogno di intermediari fidati**. La Turing completezza (Ethereum vs Bitcoin) **ha un costo**: ogni nodo esegue tutto. Un contratto deployato non si può modificare né cancellare → usare **implementazioni note** (OpenZeppelin, ConsenSys).

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Szabo (1994) | Protocollo di transazione che esegue un contratto; meno eccezioni e intermediari |
| Trust | Il codice è visibile e verificabile da tutti: la fiducia passa al codice |
| Trasparenza / flessibilità | Stesso codice per tutti (privacy a rischio) / Turing completo ma ogni nodo paga l'esecuzione |
| DApp | Contratto sulla blockchain + UI su DFS; smart contract al posto delle API, blockchain al posto del DB |
| Web 3.0 | Wallet (chiavi, firme) e node provider come nuovi livelli |
| Token | Smart contract = codice + registro; currency, utility, security |
| ERC-20 | 6 funzioni; `balances` e `allowed`; trasferire = aggiornare due righe |
| ERC-721 | Token unici per `tokenId`; metadati off-chain (IPFS) |
| ERC-1190 / 1155 | Royalty con licenza di proprietà e creativa / multi-token, batch, semi-fungibili |
| ICO → STO → IEO → IDO | Da non regolata a regolata, via exchange, via DEX |
| DAO | Token, autonomia, voto degli stakeholder; TheDAO (2016); Dash (45/45/10, masternode) |

### 5.2 Parole chiave

`Szabo` · `computerized transaction protocol` · `trusted intermediary` · `trasparenza` · `Turing completo` · `gas` · `DApp` · `wallet` · `node provider` · `Web3` · `token` · `currency / utility / security token` · `ERC` · `ERC-20` · `balances` · `allowance` · `approve / transferFrom` · `event` · `view` · `OpenZeppelin` · `ERC-721` · `NFT` · `tokenId` · `metadati` · `pinning` · `mint` · `ERC-1190` · `royalty` · `ERC-1155` · `semi-fungible` · `ICO / STO / IEO / IDO` · `DAO` · `TheDAO` · `hard fork` · `Dash` · `masternode` · `treasury` · `macchina a stati`

### 5.3 Domande

1. Definizione di Szabo: obiettivi generali ed economici. Cosa cambia con la blockchain?
2. Spiega la sequenza "the same old problem… trust": perché serve che il codice sia verificabile?
3. Trasparenza e flessibilità: vantaggi e costi di ciascuna.
4. Differenze tra contratto tradizionale e smart contract.
5. Cos'è una DApp? Confronta sito convenzionale e "dApp empowered". Una DApp è davvero decentralizzata?
6. Cos'è un token? Distingui currency, utility e security token.
7. Elenca le funzioni di ERC-20 e spiega `balances`, `allowed`, `approve` e `transferFrom`.
8. Cosa succede davvero quando si "trasferisce" un token ERC-20?
9. ERC-20 vs ERC-721: quando si usa l'uno o l'altro? Dove stanno i dati di un NFT?
10. Come funziona ERC-1190 e cosa aggiunge ERC-1155 (inclusi i semi-fungibili)?
11. Confronta ICO, STO, IEO e IDO.
12. Come funziona una DAO? Cosa è successo a TheDAO? Come distribuisce il block reward Dash?
13. Come si traduce la licenza in macchina a stati e quali parti sono difficili da portare on-chain?

<details>
<summary><b>Tracce di risposta</b></summary>

1. Protocollo che esegue i termini di un contratto; meno eccezioni, meno intermediari, meno frodi e costi. Con la blockchain l'esecuzione è garantita dal consenso decentralizzato.
2. Le persone non rispettano gli accordi; il software sì, ma se non sei tu a scriverlo ed eseguirlo devi poterlo verificare: lo smart contract è pubblico e verificabile.
3. Trasparenza: termini accessibili, ogni nodo verifica, niente dispute; ma problemi di privacy. Flessibilità: Turing completo (Ethereum, non Bitcoin); ma si paga ogni nodo che esegue.
4. Legali, linguaggio ambiguo, tribunale lento e costoso vs programmatori, codice, esecuzione sul ledger.
5. Contratto + UI. API → smart contract, DB → blockchain. Non del tutto: UI, wallet e node provider spesso centralizzati.
6. Dato digitale che rappresenta un fatto, gestito da uno smart contract. Vedi tabella §1.4.
7. totalSupply, balanceOf, transfer, transferFrom, approve, allowance. `balances` = saldi; `allowed` = deleghe; `approve` imposta (sovrascrive) la delega; `transferFrom` è il prelievo delegato.
8. Nulla si sposta: due righe della mappa `balances` cambiano e si emette `Transfer`.
9. Intercambiabili → ERC-20; conta quale unità → ERC-721. On-chain solo il riferimento (IPFS), l'opera è off-chain.
10. Royalty automatiche al titolare della licenza creativa su vendite e noleggi. ERC-1155: più token in un contratto, batch, fungibili e non; semi-fungibili (biglietto → memorabilia).
11. Vedi tabella §2.4.
12. Token, autonomia, voto degli stakeholder, contractor, proposte con deposito. TheDAO: vulnerabilità, ~1/3 dei fondi rubati, hard fork. Dash: 45% miner, 45% masternode, 10% treasury.
13. Stati 1–6, violazione assorbente. Difficili tempo (24 h, "non ha pubblicato") ed eventi esterni (approvazione, commissione): timestamp e oracoli.

</details>

---

### Da verificare

- [ ] Caricare gli screenshot mancanti (applicazioni, PwC, CryptoKitties, DApp, Web site vs DApp, Web 2.0/3.0, ERC-20, implementazioni, ERC-721, NFT e IPFS, ERC-1190)
- [ ] Beeple: quale opera ha citato il Prof. a voce? Le slide linkano un video su Nifty Gateway e l'articolo su *Everydays* (69 mln $)
- [ ] Game 5 Ball: in slide c'è solo il link (game5ball.com); verificare il contesto citato a lezione
- [ ] ERC-1155, ICO/STO/IEO/IDO, DAO e Dash sono nelle slide 04.01: confermare quanto è stato spiegato in aula e quanto solo mostrato

---

> **Fonti e verifica.** Verificato su 04.00 – Smart Contracts (Reduced) e 04.01 – Tokens; la bozza originale (trascrizione da Panopto) è stata riorganizzata nel formato standard senza togliere contenuti. Risolti dalle slide: sezione *Trasparenza*, ERC-1190 (royalty, licenza di proprietà e creativa, noleggio), ERC-1155 e semi-fungibili, link ai tutorial NFT. Aggiunti dalle slide: sequenza *trust*, contratti tradizionali vs smart, tipi di token, interfaccia ERC-20 completa, `approve`/`transferFrom`, OpenZeppelin, contratto NFT, Upland, ICO/STO/IEO/IDO, DAO, TheDAO, Dash. Dalla letteratura (non in slide): dettagli su TheDAO (reentrancy, 3,6 mln ETH, Ethereum Classic), race condition di `approve`, data e cifra di *Everydays*, standard EIP-721 finale, codice §4.1 e §4.2. Riferimenti: Szabo, *Smart Contracts* (1994); Governatori et al., *On legal contracts, imperative and declarative smart contracts, and blockchain systems*, Artif Intell Law 26 (2018); EIP-20, EIP-721, EIP-1155.

[← Indice](README.md)
