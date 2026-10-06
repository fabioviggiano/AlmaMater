# Capitolo 3 — Smart Transportation: dati personali su DFS e DLT

| | |
|---|---|
| **Data** | Lunedì 28/09/2026 · Lezione 3 |
| **Macro tema** | Parte II — Applicazioni: architettura DFS + DLT + smart contract |
| **Slide** | 03.00 – The Use of Decentralized Systems to Develop Smart Transportation (Mobi talk 2021, Prof. Ferretti) · ripresa di supply chain da 02 |

[← Indice](README.md)

---

## 1. Fondamenti

### 1.1 Raccordo con la lezione precedente

La lezione riparte dalla tracciabilità di filiera ([Capitolo 2](<02 DLT, smart contract e use case.md>), §2.1–2.2) e dal principio **Garbage In, Garbage Out**: la blockchain garantisce l'immutabilità del registro, non la verità del dato fisico. Anche qui i dati sono prodotti da molti attori (i veicoli), ma sono **dati personali**: il problema si sposta dalla tracciabilità alla **sovranità del dato**.

### 1.2 Lo scenario: Intelligent Transportation Systems

I veicoli raccolgono **sensed data** (posizione, velocità, strada, meteo, incidenti) che, condivisi, abilitano **smart services**: safety (crash alert, incroci, contromano), informazione e ottimizzazione (traffico, percorsi, manutenzione, infotainment), veicoli come *(trusted) data mules* e *(crowd-)sensing as a service*.

La slide costruisce una tabella a tre livelli, chiave di tutta la lezione:

| Livello | Contenuto |
|---|---|
| **Desiderata** | Sharing · aggregation · trading |
| **Features** | Access control · authenticity · verifiability · immutability |
| **Technologies** | DLT · distributed storage · smart contracts · authorization |

Ma sono **personal data**: dove si conservano (*data storage*)?

### 1.3 Quattro opzioni

| Opzione | Pro | Contro |
|---|---|---|
| **Opt1** — entità centrale | Semplice | Gli utenti **perdono la sovranità**: il *data controller* ha tutti i dati, può alterarli, bisogna fidarsi di lui |
| **Opt2** — dati in locale, distribuiti su richiesta | Mantieni i tuoi dati | Poco pratico: devi essere sempre raggiungibile; servono storage, calcolo, banda |
| **Opt3** — dati registrati su un ledger | Abbastanza semplice, integrità, tracciabilità | Solo **dati piccoli**; **niente diritto all'oblio/rettifica**; **latenze** |
| **Opt4** — DFS per i dati crowdsourced | Scalabile, dati rimovibili | Bisogna garantire **integrità**, **controllo degli accessi**, **persistenza** |

> 💡 **Lettura da esame.** È il Capitolo 1 applicato: Opt1 = client/server (SPOF di controllo), Opt2 = P2P puro (churn), Opt3 = tutto on-chain (costo, GDPR), Opt4 = architettura ibrida. Il resto della lezione risolve i tre problemi di Opt4.

---

## 2. Architettura

### 2.1 Integrità: content addressing + hash pointer

- Sul DFS (**IPFS**, **Sia**) ogni chunk è identificato dall'**hash del contenuto** (*content based addressing instead of location based*): gli ID in slide (`QmW98pJ…`, `abc45j…`) sono di questo tipo.
- Sulla **DLT** si registrano solo gli **hash pointer**.
- Vantaggi (slide): **possibile rimuovere/modificare i dati**; **upload veloce** sul DFS; le **latenze per registrare gli hash** diventano **meno problematiche**.
- **Verifica:** chi scarica ricalcola l'hash e lo confronta con quello sul ledger (*tamper-evident*).

> ⚠️ **Nota di rigore.** Un chunk è già auto-verificabile rispetto al proprio CID. La DLT aggiunge **quale** CID è quello ufficiale, **chi** l'ha registrato (firma) e **quando** (ordine concordato). Inoltre "rimuovere" dal DFS significa smettere di ospitarlo (*unpin*): altri nodi possono averne copie. Per l'oblio si **cifra prima del caricamento** e si distrugge la chiave (*crypto-shredding*).

### 2.2 Controllo degli accessi: DFS + cifratura + autorizzazione

I dati sul DFS sono **cifrati**. Domanda della slide: **how to decrypt?**

- **Opt4.1 — server centrale di autorizzazione** che fornisce le chiavi a chi è nella sua ACL. Semplice, ma di nuovo **SPOF** e fiducia unica.
- **Secret sharing tra più server** (dal paper NCA 2020): la chiave è divisa con **Shamir (k, n)**; servono k quote, con k−1 non si ottiene nulla. Tollera fino a **k−1 server compromessi** e **n−k offline**.
- **Opt4.2 — security-by-contract su un ledger (privato):** la **ACL sta in uno smart contract**; gli *auth. servers* rilasciano la propria quota solo se il contratto conferma il permesso.

**Benefici di Opt4.2 (slide):**
- **decentralizzazione della custodia delle chiavi**: i server **non hanno i dati**, **nessun single point of failure**, **mitigazione della privacy leakage**;
- **trasparenza**: **auditability** dei permessi di accesso.

> ⚠️ **Nota di rigore.** La fiducia non sparisce: si distribuisce sui server (ipotesi: meno di k colludono) e su chi governa il ledger privato. Con la **Proxy Re-Encryption** un proxy può ricifrare il dato per il destinatario senza vederlo in chiaro. Questo tema (*Decentralized Authorization*) è tra le proposte di project work del gruppo AnaNSi.

### 2.3 Persistenza: incentivi a cooperare

Nessuno è obbligato a conservare i file altrui: la slide *"Data persistence: we'd like to avoid this"* mostra (Guo et al., 2007) come la disponibilità di un contenuto BitTorrent **decada nel tempo**. Soluzione: **incentivi con token su blockchain**, es. **Filecoin, Sia, Storj, Swarm (??)**. I nodi vengono pagati per conservare i dati e devono dimostrarlo (in Filecoin: *Proof-of-Replication*, *Proof-of-Spacetime*).

### 2.4 Il sistema complessivo

```
   DFS (IPFS, Sia)            dati cifrati, chunk con content addressing
        │ hash pointer
        ▼
   DLT "free, fast" (IOTA)    notarizzazione continua degli hash  → integrità
   DLT con smart contract     contratto ACL                       → autorizzazione
                              contratto/token di storage          → persistenza
```

> ⚠️ **Punto da esame: separazione delle responsabilità.** Nessuna DLT è buona per tutto: i dati grezzi su Ethereum costerebbero troppo; una DLT veloce e senza fee per l'IoT (IOTA all'epoca) non gestisce logica contrattuale. Si combinano DFS + DLT veloce + DLT programmabile, e **gli utenti mantengono la sovranità** sui dati.

---

## 3. Trade-off e risultati sperimentali

**"Does it work?" "Yes!" "Does it scale?" "…"** L'aspetto più critico è il **caricamento dei dati**. Test su un dataset reale: **tracce di mobilità degli autobus di Rio de Janeiro**.

- **Opt3 → DLT (IOTA):** con una **buona selezione dei full node** gli aggiornamenti del ledger sono **affidabili** (pochi errori), ma le **latenze misurate sono rilevanti**.
- **Opt4 → DFS (IPFS, Sia):** confronto tra JSON piccoli (~100 B: latitudine, longitudine, timestamp) e file da 1 MB.

**Conclusioni della slide:** DLT, DFS, smart contract e schemi di autorizzazione permettono servizi affidabili; architettura **a strati** DFS + DLT; utenti sovrani sui propri dati. Restano aperti **scalabilità/reattività (gestione del churn)** e il trattamento dei **dati sensibili**.

| Scelta | Guadagno | Costo |
|---|---|---|
| Tutto on-chain (Opt3) | Integrità, tracciabilità | Solo dati piccoli, niente oblio, latenza |
| DFS + hash on-chain (Opt4) | Scalabilità, dati cancellabili | Gestire accesso e persistenza |
| Server di autorizzazione centrale | Semplicità | SPOF, fiducia, privacy leakage |
| Secret sharing + ACL on-chain | Nessuno ha la chiave intera; permessi verificabili | Più componenti, latenza, coordinamento |
| Incentivi in token | Persistenza senza server centrale | Dipendenza dal valore del token |

---

## 4. Esempi e codice

### 4.1 Integrità: DFS simulato + hash sul ledger

```python
import hashlib
dfs, ledger = {}, set()

def upload(dato: bytes) -> str:
    cid = hashlib.sha256(dato).hexdigest()   # content addressing
    dfs[cid] = dato
    ledger.add(cid)                          # sulla DLT solo l'hash pointer
    return cid

def download(cid: str) -> bytes:
    dato = dfs[cid]
    assert cid in ledger, "CID non registrato"
    assert hashlib.sha256(dato).hexdigest() == cid, "dato manomesso"
    return dato

cid = upload(b'{"lat":-22.976509,"lon":-43.19902,"ts":"2020-04-05T14:54:11Z"}')
dfs[cid] = b'{"lat":0,"lon":0}'              # manomissione sul DFS
# download(cid) -> AssertionError: dato manomesso
```

### 4.2 Shamir (k, n), versione didattica

```python
import random
P = 2**127 - 1                                       # primo

def split(secret, k, n):
    coeffs = [secret] + [random.randrange(P) for _ in range(k - 1)]
    f = lambda x: sum(c * pow(x, i, P) for i, c in enumerate(coeffs)) % P
    return [(x, f(x)) for x in range(1, n + 1)]     # una quota per server

def combine(shares):                                 # Lagrange in x = 0
    s = 0
    for i, (xi, yi) in enumerate(shares):
        num = den = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num, den = num * -xj % P, den * (xi - xj) % P
        s = (s + yi * num * pow(den, -1, P)) % P
    return s

q = split(123456789, k=3, n=5)
print(combine(q[:3]) == 123456789, combine(q[:2]) == 123456789)   # True False
```

Il segreto è il termine noto di un polinomio di grado k−1: servono k punti per ricostruirlo.

---

## 5. Quadro di riepilogo

### 5.1 Concetti chiave

| Concetto | In sintesi |
|---|---|
| Desiderata → features → tecnologie | Sharing/aggregation/trading → access control, authenticity, verifiability, immutability → DLT, DFS, smart contract, authorization |
| Opt1–Opt4 | Centrale (perdi sovranità) · locale (sempre raggiungibile) · ledger (dati piccoli, niente oblio, latenze) · DFS (integrità, accessi, persistenza) |
| Integrità | Content addressing sul DFS + hash pointer sulla DLT |
| Accessi | Dati cifrati; Opt4.1 server centrale; Shamir tra più server; Opt4.2 ACL in smart contract |
| Persistenza | Token di incentivo (Filecoin, Sia, Storj) con prove di storage |
| Overall system | DFS + DLT veloce senza fee (IOTA) + DLT programmabile |
| Risultati | IOTA affidabile con buoni full node ma latenze rilevanti; aperti scalabilità e churn |

### 5.2 Parole chiave

`ITS` · `sensed data` · `data mules` · `crowdsensing` · `sovranità del dato` · `data controller` · `DFS` · `IPFS` · `Sia` · `content addressing` · `hash pointer` · `unpin` · `crypto-shredding` · `ACL` · `authorization server` · `Shamir (k, n)` · `security-by-contract` · `proxy re-encryption` · `data persistence` · `Filecoin` · `IOTA` · `separazione delle responsabilità`

### 5.3 Domande

1. Collega desiderata, features e tecnologie della tabella del Prof.
2. Pro e contro delle quattro opzioni di storage.
3. Perché Opt3 non è adatta ai dati personali dei veicoli?
4. Come si verifica l'integrità di un chunk e cosa aggiunge la DLT al solo content addressing?
5. "Rimuovere il dato dal DFS" basta per il diritto all'oblio?
6. Confronta Opt4.1 e Opt4.2 e indica i benefici della security-by-contract.
7. Come funziona Shamir (k, n)? Quanti server compromessi e offline tollera?
8. Perché serve un meccanismo di persistenza e come lo si ottiene?
9. Descrivi l'overall system: perché non si usa un'unica blockchain?
10. Cosa hanno mostrato i test con le tracce degli autobus di Rio?

<details>
<summary><b>Tracce di risposta</b></summary>

1. Per condividere, aggregare e vendere dati servono controllo accessi, autenticità, verificabilità, immutabilità, ottenuti con DLT, storage distribuito, smart contract, autorizzazione.
2. Vedi tabella §1.3.
3. Costi/dimensioni, latenze, e l'append-only impedisce oblio e rettifica.
4. Si ricalcola l'hash e lo si confronta col ledger. La DLT dice quale CID è ufficiale, chi l'ha registrato e quando.
5. No: altri nodi possono avere copie; si cifra e si distrugge la chiave.
6. 4.1: un server con ACL propria (SPOF, fiducia totale). 4.2: ACL nello smart contract, server con quote della chiave. Benefici: custodia decentralizzata, server senza dati, nessun SPOF, meno privacy leakage, permessi verificabili.
7. Chiave = termine noto di un polinomio di grado k−1; ogni server ha un punto. Tollera k−1 compromessi e n−k offline.
8. Senza incentivi i peer abbandonano i contenuti (Guo et al.); token di storage con prove crittografiche.
9. DFS per i dati, DLT veloce per gli hash, DLT programmabile per ACL e token: ogni piattaforma ottimizza cose diverse.
10. Aggiornamenti IOTA affidabili con buona scelta dei full node, ma latenze rilevanti; confronto DFS tra JSON da 100 B e file da 1 MB.

</details>

---

> **Fonti e verifica.** Verificato su 03.00 (Mobi talk 2021). Dalla letteratura (non in slide): unpin, crypto-shredding, PRE, soglie di tolleranza di Shamir, Proof-of-Replication/Spacetime, codice. Riferimenti: Zichichi, Ferretti, D'Angelo, *A Framework based on DLTs for Data Management and Services in ITS*, IEEE Access 2020; Zichichi et al., *Personal Data Access Control Through Distributed Authorization*, IEEE NCA 2020; Zichichi et al., *On the Efficiency of Decentralized File Storage for Personal Information Management Systems*, IEEE ISCC 2020; Guo et al., *A performance study of BitTorrent-like peer-to-peer systems*, IEEE JSAC 2007.

[← Indice](README.md)
