# Capitolo 3 — Smart Transportation: dati personali su DFS e DLT

*Lezione 3 (28/09/2026) · Slide "03.00 – The Use of Decentralized Systems to Develop Smart Transportation" (Mobi talk 2021, Prof. S. Ferretti), con i lavori Zichichi–Ferretti–D'Angelo del gruppo AnaNSi.*

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Lo scenario: Intelligent Transportation Systems (ITS)

I veicoli raccolgono continuamente **dati sensoriali** (*sensed data*): posizione, velocità, condizioni della strada, meteo, incidenti. Questi dati, condivisi, abilitano **servizi smart**, che le slide raggruppano in tre famiglie:

| Famiglia | Esempi dalla slide |
|---|---|
| **Safety** | Crash alert, sicurezza agli incroci, contrasto alla guida contromano, allerte meteo stradali |
| **Info e ottimizzazione** | Analisi del traffico, ottimizzazione dei percorsi, manutenzione, PoI e infotainment |
| **Trasporto per servizi smart** | Veicoli come *(trusted) data mules* (trasportano dati per altri), *(Crowd-)Sensing as a Service* |

### 1.2 Desiderata, proprietà, tecnologie

La slide costruisce una tabella a tre livelli, che è la chiave di lettura dell'intera lezione:

| Livello | Contenuto |
|---|---|
| **Desiderata** (cosa si vuole fare con i dati) | **Sharing**, **aggregation**, **trading** |
| **Features** (proprietà necessarie) | **Access control**, **authenticity**, **verifiability**, **immutability** |
| **Technologies** (con cosa si ottengono) | **DLT**, **distributed storage**, **smart contract**, **authorization** |

Il problema di fondo: sono **dati personali** (dove sono stato, quando, come guido). Chi li conserva?

### 1.3 Quattro opzioni per conservare i dati

**Opt1 — Un'entità centrale conserva i dati crowdsourced.** Gli utenti **perdono la sovranità** sui propri dati:

- il titolare (*data controller*) ottiene tutti i dati;
- può alterarli;
- gli utenti devono fidarsi di lui.

**Opt2 — Ognuno tiene i dati in locale e li distribuisce su richiesta.**

- **Pro:** mantieni i tuoi dati.
- **Contro:** poco pratico, devi essere sempre raggiungibile; servono capacità di storage, calcolo e comunicazione sul dispositivo.

**Opt3 — Registrare i dati su un ledger.**

- **Pro:** abbastanza semplice; integrità dei dati; tracciabilità.
- **Contro:** va bene **solo per dati piccoli**; **niente diritto all'oblio né alla rettifica**; **latenze**.

**Opt4 — Usare un file system decentralizzato (DFS) per i dati.** Resta da risolvere come:

1. garantire l'**integrità** dei dati (§2.1);
2. controllare **chi può accedervi** (§2.2);
3. garantire la **persistenza** dei dati (§2.3).

> 💡 **Lettura da esame.** Le quattro opzioni sono lo stesso ragionamento del Capitolo 1 applicato a un caso concreto: Opt1 = client/server (SPOF di controllo), Opt2 = P2P puro (churn e disponibilità), Opt3 = tutto on-chain (costo, GDPR), Opt4 = architettura ibrida. Il resto della lezione risolve i tre problemi di Opt4.

---

## 2. Architettura

### 2.1 Integrità: content-based addressing e hash pointer

- Sul DFS (es. **IPFS**, **Sia**) i dati sono suddivisi in chunk, ciascuno identificato dall'**hash del suo contenuto** (*content-based addressing*, invece di *location-based*: vedi Capitolo 2, §1.3). Gli identificatori nella slide (`QmW98pJ…`, `abc45j…`) sono di questo tipo.
- Sulla **DLT** si registrano solo gli **hash pointer**, non i dati.

Vantaggi indicati nella slide:

- è **possibile rimuovere o modificare i dati** sul DFS (a differenza di Opt3);
- il **caricamento sul DFS è veloce**;
- le **latenze per registrare gli hash** sulla DLT diventano **meno problematiche**, perché si scrive poco e non serve attendere per usare il dato.

**Verifica dell'integrità.** Chi scarica un chunk ricalcola l'hash e lo confronta con quello registrato sul ledger: se anche un bit è cambiato, i valori non coincidono.

> ⚠️ **Nota di rigore** (sintesi mia). Con il content addressing un chunk è già auto-verificabile rispetto al proprio CID. La DLT aggiunge ciò che il DFS da solo non dà: **quale** CID è quello "ufficiale", **chi** l'ha registrato (firma) e **quando** (ordine e timestamp concordati dal consenso).

> ⚠️ **Nota di rigore sulla cancellazione.** "Rimuovere il dato dal DFS" significa smettere di ospitarlo (*unpin*) sui propri nodi; non si può obbligare gli altri nodi che ne hanno una copia a cancellarla. Per questo i dati si **cifrano prima del caricamento**: distruggendo la chiave (*crypto-shredding*) il dato diventa illeggibile ovunque si trovi. Il riferimento on-chain resta, ma punta a un contenuto inutilizzabile.

### 2.2 Controllo degli accessi: DFS + cifratura + autorizzazione

Sul DFS i dati sono **cifrati**; il problema diventa: **come ottiene la chiave per decifrarli chi è autorizzato?**

```
[ Veicolo ] ──(dato cifrato)──▶ [ DFS (IPFS/Sia) ]
      │
      └──(hash / digest)──────▶ [ DLT ]
```

**Opt4.1 — Server centrale di autorizzazione.** Un server consulta la propria ACL e, se l'utente è autorizzato, gli fornisce la chiave. Semplice, ma è di nuovo **SPOF** e punto di fiducia unico: il server vede tutte le chiavi.

**Passaggio intermedio — più server con secret sharing** (dal lavoro *Personal Data Access Control Through Distributed Authorization*, 2020). La chiave è divisa con **Shamir (k, n)** tra n server di autorizzazione: nessuno la conosce per intero. L'utente contatta almeno k server; ognuno verifica l'autorizzazione e restituisce la propria quota; con k quote il client ricompone la chiave. Con meno di k quote non si ottiene nulla.

**Opt4.2 — Security-by-contract su un ledger (privato).** La **ACL sta in uno smart contract**. I server di autorizzazione (*Auth. servers*) interrogano il contratto prima di rilasciare la propria parte di chiave.

Benefici elencati nella slide:

- **decentralizzazione della custodia delle chiavi**:
  - i server **non hanno i dati** (stanno sul DFS);
  - si **mitiga la fuga di informazioni** (*privacy leakage*);
- **trasparenza**: i permessi di accesso ai dati sono **verificabili** (*auditability*), perché la ACL sta sul ledger.

> 💡 **Collegamento.** È la **Decentralized Authorization** proposta come tema di progetto nel [Capitolo 1](<01 Il paradigma della decentralizzazione.md>) (§0.4). Con la **Proxy Re-Encryption** il proxy può ricifrare il dato per il destinatario senza vederlo in chiaro, evitando di distribuire la chiave originale.

### 2.3 Persistenza: incentivi a cooperare

In una rete P2P nessuno è obbligato a conservare i file altrui. La slide *"Data persistence: we'd like to avoid this"* mostra lo studio di Guo et al. (2007) su BitTorrent: la disponibilità di un contenuto **decade nel tempo** quando i peer se ne vanno (churn, Capitolo 1).

**Soluzione: incentivi economici tramite token su blockchain.** Esempi della slide: **Filecoin, Sia, Storj** (e Swarm, con un punto interrogativo). I nodi di storage vengono pagati in token per conservare i dati e devono **dimostrare** di farlo (in Filecoin: *Proof-of-Replication* e *Proof-of-Spacetime*).

### 2.4 Il sistema complessivo (*The overall system*)

```
            ┌───────────────────────────┐
            │   DFS (IPFS, Sia)         │  dati cifrati, chunk con content addressing
            └────────────┬──────────────┘
                         │ hash pointer
                         ▼
            ┌───────────────────────────┐
            │   DLT "free, fast"        │  registrazione continua degli hash (integrità)
            │   (es. IOTA)              │
            └───────────────────────────┘
            ┌───────────────────────────┐
            │   DLT con smart contract  │  • smart contract ACL (autorizzazione)
            │   (es. Ethereum)          │  • smart contract per i token (persistenza)
            └───────────────────────────┘
```

| Strato | Tecnologia | Proprietà garantita |
|---|---|---|
| **Storage** | DFS (IPFS, Sia) | Dati voluminosi e cifrati fuori dalla catena; cancellabili |
| **Integrità** | DLT veloce e senza fee (IOTA) | Notarizzazione continua degli hash dei flussi dei veicoli |
| **Autorizzazione** | Smart contract ACL + auth server | Chi può leggere cosa, in modo verificabile |
| **Persistenza** | Smart contract / token di storage | Incentivi a conservare i dati nel tempo |

> ⚠️ **Punto da esame: separazione delle responsabilità.** Non esiste una DLT buona per tutto. I dati grezzi su Ethereum costerebbero troppo; una DLT pensata per micro-transazioni IoT senza fee (IOTA nella versione dell'epoca) non gestisce logica contrattuale complessa. Si combinano: DFS per lo storage, DLT veloce per gli hash, DLT programmabile per ACL e incentivi. **Gli utenti mantengono la sovranità sui propri dati.**

---

## 3. Trade-off e risultati sperimentali

### 3.1 "Does it work?" "Yes!" "Does it scale?" "…"

Il Prof. ammette che l'aspetto più critico è la **scalabilità del caricamento dei dati** nel sistema decentralizzato. Test su un dataset reale: **tracce di mobilità degli autobus di Rio de Janeiro**.

**Cosa è stato testato**

- **Opt3 → DLT:** IOTA (in questo contesto dovrebbe andare meglio delle blockchain tradizionali).
- **Opt4 → DFS:** IPFS e Sia.

**Risultati**

- **IOTA:** scegliendo bene i full node a cui inviare le transazioni si ottengono aggiornamenti del ledger **affidabili** (pochi errori), ma le **latenze misurate sono rilevanti**.
- **DFS:** confronto tra dati piccoli (JSON di circa 100 B con latitudine, longitudine, timestamp) e file più grandi (1 MB).

### 3.2 Conclusioni della slide

- DLT, DFS, smart contract e schemi di autorizzazione permettono di costruire servizi di smart transportation affidabili.
- Architettura **a strati** DFS + DLT.
- Gli utenti **mantengono la sovranità** sui propri dati.
- **Criticità:**
  - scalabilità e reattività: serve migliorare la **gestione del churn**;
  - attenzione nel trattare **dati sensibili**.

### 3.3 Tabella dei trade-off

| Scelta | Guadagno | Costo |
|---|---|---|
| Tutto on-chain (Opt3) | Semplicità, integrità, tracciabilità | Solo dati piccoli, niente oblio/rettifica, latenza |
| DFS + hash on-chain (Opt4) | Scalabilità, dati cancellabili | Serve gestire accesso e persistenza |
| Server di autorizzazione centrale | Semplice | SPOF, fiducia, privacy leakage |
| Secret sharing + ACL on-chain | Nessuno ha la chiave intera, permessi verificabili | Più componenti, latenza, coordinamento dei server |
| Incentivi in token | Persistenza senza server centrale | Dipendenza da un'economia di token e dal suo valore |

---

## 4. Esempi e codice

### 4.1 Integrità: DFS simulato + hash registrato

```python
import hashlib

dfs, ledger = {}, []

def upload(dato: bytes) -> str:
    cid = hashlib.sha256(dato).hexdigest()   # content-based addressing
    dfs[cid] = dato
    ledger.append(cid)                       # sulla DLT solo l'hash pointer
    return cid

def download_e_verifica(cid: str) -> bytes:
    dato = dfs[cid]
    assert cid in ledger, "CID non registrato sul ledger"
    assert hashlib.sha256(dato).hexdigest() == cid, "dato manomesso"
    return dato

cid = upload(b'{"lat":-22.976509,"lon":-43.19902,"ts":"2020-04-05T14:54:11Z"}')
print(download_e_verifica(cid))
dfs[cid] = b'{"lat":0,"lon":0}'              # manomissione sul DFS
# download_e_verifica(cid) -> AssertionError: dato manomesso
```

### 4.2 Secret sharing (k, n) di Shamir, versione didattica

```python
import random
P = 2**127 - 1                                      # primo (campo finito)

def split(secret, k, n):
    coeffs = [secret] + [random.randrange(P) for _ in range(k - 1)]
    f = lambda x: sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P
    return [(x, f(x)) for x in range(1, n + 1)]    # una quota per server

def combine(shares):                                # interpolazione di Lagrange in x = 0
    s = 0
    for i, (xi, yi) in enumerate(shares):
        num = den = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = num * -xj % P
                den = den * (xi - xj) % P
        s = (s + yi * num * pow(den, -1, P)) % P
    return s

chiave = 123456789
quote = split(chiave, k=3, n=5)
print(combine(quote[:3]) == chiave)                 # True: 3 quote bastano
print(combine(quote[:2]) == chiave)                 # False: 2 quote non bastano
```

Il segreto è il termine noto di un polinomio di grado k−1; servono k punti per ricostruirlo. Con k−1 punti qualunque valore del segreto è ugualmente possibile.

---

## 5. Quadro sintetico

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| **ITS** | Veicoli che producono dati per servizi di safety, ottimizzazione e sensing |
| **Desiderata → features → tecnologie** | Sharing/aggregation/trading → access control, authenticity, verifiability, immutability → DLT, DFS, smart contract, authorization |
| **Opt1** | Entità centrale: gli utenti perdono la sovranità sui dati |
| **Opt2** | Dati in locale: sovranità, ma bisogna essere sempre raggiungibili |
| **Opt3** | Tutto sul ledger: integrità, ma solo dati piccoli, niente oblio, latenze |
| **Opt4** | DFS + hash sulla DLT; restano integrità, accesso, persistenza |
| **Integrità** | Content addressing + hash pointer sul ledger; verifica ricalcolando l'hash |
| **Accesso** | Dati cifrati; Opt4.1 server centrale; Opt4.2 ACL in smart contract + server di autorizzazione con quote della chiave |
| **Persistenza** | Incentivi in token (Filecoin, Sia, Storj) con prove di storage |
| **Overall system** | DFS + DLT veloce senza fee (IOTA) + DLT programmabile (Ethereum) |
| **Risultati** | IOTA affidabile con buona scelta dei nodi ma con latenze rilevanti; problema aperto: scalabilità e churn |

### 5.2 Domande e risposte

1. Quali famiglie di servizi abilitano i dati dei veicoli?
2. Collega desiderata, features e tecnologie della tabella del Prof.
3. Quali sono le quattro opzioni per conservare i dati? Pro e contro di ciascuna.
4. Perché Opt3 (tutto sul ledger) non è adatta ai dati personali dei veicoli?
5. Come si verifica che un chunk scaricato dal DFS non sia stato alterato?
6. Cosa aggiunge la DLT rispetto al solo content addressing?
7. "Rimuovere il dato dal DFS" basta per il diritto all'oblio?
8. Confronta Opt4.1 e Opt4.2 per il controllo degli accessi.
9. Come funziona lo schema (k, n) di Shamir e perché elimina lo SPOF sulla chiave?
10. Quali benefici elenca la slide per la security-by-contract?
11. Perché serve un meccanismo di persistenza in un DFS? Come lo si ottiene?
12. Descrivi l'overall system e il ruolo di ciascuno strato.
13. Perché non si usa un'unica blockchain per tutto?
14. Cosa hanno mostrato i test su IOTA con le tracce degli autobus di Rio?
15. Quali criticità restano aperte secondo le conclusioni?

<details>
<summary><b>Tracce di risposta</b></summary>

1. Safety (crash alert, incroci, contromano, meteo), info e ottimizzazione (traffico, percorsi, manutenzione, infotainment), trasporto per servizi (data mules, crowd-sensing as a service).
2. Per condividere, aggregare e vendere dati servono controllo degli accessi, autenticità, verificabilità e immutabilità, ottenuti con DLT, storage distribuito, smart contract e schemi di autorizzazione.
3. Opt1 centrale (perdita di sovranità); Opt2 locale (sempre raggiungibili, risorse sul dispositivo); Opt3 ledger (solo dati piccoli, niente oblio, latenze); Opt4 DFS (da risolvere integrità, accesso, persistenza).
4. Costi e dimensioni, latenze, e l'append-only impedisce cancellazione e rettifica (GDPR).
5. Si ricalcola l'hash del chunk e lo si confronta con l'hash registrato sulla DLT.
6. Quale CID è quello valido, chi l'ha registrato e quando, con ordine concordato dal consenso.
7. No: altri nodi possono averne copie. Si cifra il dato e si distrugge la chiave (crypto-shredding).
8. 4.1: un server con ACL propria fornisce le chiavi (SPOF, fiducia totale). 4.2: ACL nello smart contract, più server di autorizzazione che rilasciano quote della chiave solo se il contratto conferma i permessi.
9. La chiave è il termine noto di un polinomio di grado k−1; ogni server ha un punto. Servono k punti per ricostruirla, con meno non si ottiene nulla. Nessun server ha la chiave intera.
10. Custodia decentralizzata delle chiavi (i server non hanno i dati, meno privacy leakage) e trasparenza (permessi verificabili).
11. Senza obblighi i nodi abbandonano i contenuti (studio su BitTorrent). Si pagano i nodi in token (Filecoin, Sia, Storj) chiedendo prove crittografiche di conservazione.
12. DFS per i dati cifrati; DLT veloce senza fee per gli hash; DLT con smart contract per ACL e token.
13. Ogni piattaforma ottimizza cose diverse: separazione delle responsabilità.
14. Aggiornamenti affidabili con una buona scelta dei full node, ma latenze rilevanti.
15. Scalabilità e reattività (gestione del churn) e trattamento dei dati sensibili.

</details>

---

## Riferimenti di approfondimento

- Zichichi, Ferretti, D'Angelo, *A Framework based on Distributed Ledger Technologies for Data Management and Services in Intelligent Transportation Systems*, IEEE Access, vol. 8 (2020)
- Zichichi, Ferretti, D'Angelo, Rodríguez-Doncel, *Personal Data Access Control Through Distributed Authorization*, IEEE NCA (2020)
- Zichichi, Ferretti, D'Angelo, *Are Distributed Ledger Technologies Ready for Intelligent Transportation Systems?*, CryBlock @ MobiCom (2020)
- Zichichi, Ferretti, D'Angelo, *On the Efficiency of Decentralized File Storage for Personal Information Management Systems*, ISCC (2020)
- Guo et al., *A performance study of BitTorrent-like peer-to-peer systems*, IEEE JSAC 25 (2007)

> Nota: Proof-of-Replication e Proof-of-Spacetime, la precisazione su unpin e crypto-shredding e il codice di Shamir vengono dalla letteratura generale, non dalle slide.

---

[← Indice](README.md)
