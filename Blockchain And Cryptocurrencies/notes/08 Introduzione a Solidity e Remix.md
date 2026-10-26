# Capitolo 8 — Introduzione a Solidity e Remix

| | |
|---|---|
| **Data** | Lunedì 26/10/2026 · Lezione 8 |
| **Macro tema** | Parte IV — Smart contract: Solidity, Remix IDE, EVM |
| **Slide** | 06.01 – Solidity · <!-- link Panopto --> |

[← Indice](README.md)

> **Nota:** le lezioni della settimana (incluso venerdì 30/10) sono annullate per le sedute di laurea. Si riprende a novembre.
>
> ⚠️ **Registrazione incompleta:** manca l'ultima mezz'ora circa. L'audio si interrompe durante i tipi di dato base (`bool`, `uint256`). Vedi § 6.

---

## 1. Fondamenti

**Solidity** è il linguaggio di riferimento per gli smart contract su Ethereum: è ad alto livello, **a tipizzazione statica** e **orientato agli oggetti**, con una sintassi che ricorda JavaScript/C++/Java. Supporta ereditarietà, variabili di stato, funzioni, modifier, eventi, struct ed enum.

- **Analogia EVM ↔ JVM:** come Java viene compilato in bytecode per la JVM, Solidity viene compilato in **bytecode EVM**. È la EVM di ogni nodo a eseguirlo.
- **Determinismo:** ogni transazione che modifica lo stato viene rieseguita da **tutti i nodi**, che devono arrivare allo stesso stato per mantenere consenso e finalità. Ne segue che stesso codice + stesso input devono dare lo stesso stato, e quindi **non esistono primitive non deterministiche native** (niente vero generatore di numeri casuali).
- **Immutabilità:** una volta deployato, il bytecode di un contratto **non si può modificare** (*code is law*).

## 2. Architettura: dal sorgente alla chain

```
.sol ──compilatore solc──► bytecode EVM ──deploy (tx)──► contratto @ indirizzo
                      └──► ABI (JSON) ──► usata dalle dApp per chiamare le funzioni
```

- **Bytecode:** ciò che viene effettivamente salvato ed eseguito on-chain.
- **ABI (Application Binary Interface):** descrive funzioni, firme, parametri e tipi di ritorno. È l'"interfaccia" che le dApp usano per costruire le chiamate al contratto.
- **Deploy:** è una transazione. Viene minata in un blocco, consuma gas e assegna al contratto un **indirizzo**.
- **Aggiornare un contratto = deployarne uno nuovo.** Il nuovo contratto ha un **nuovo indirizzo**, mentre il vecchio **resta attivo** (a lezione: indirizzi che finivano in `…138` e `…E07`). Sta alla dApp migrare al nuovo.
- **Transazione vs chiamata:**
  - le funzioni che **modificano lo stato** (`store`) generano una transazione minata, con hash, numero di blocco e costo in gas a carico del chiamante;
  - le funzioni **`view`** (`retrieve`) leggono lo stato e restituiscono l'output decodificato, senza nuova transazione se chiamate dall'esterno.

## 3. Trade-off e attacchi

| Rischio | Perché | Mitigazione |
|---|---|---|
| Bug in mainnet | Il codice è immutabile: il bug resta finché la dApp non migra a un nuovo contratto | Test approfonditi in locale (Remix VM, Hardhat, Foundry) e su testnet prima del deploy; librerie verificate (OpenZeppelin) |
| Contratti "vecchi" ancora attivi | Il redeploy non cancella il contratto precedente | Gestire la migrazione lato dApp e comunicare il nuovo indirizzo |
| Randomness on-chain | Il determinismo impedisce un vero random nativo; valori "pseudo-casuali" derivati dal blocco sono prevedibili | Non affidarsi a random on-chain *(per soluzioni come oracoli/commit-reveal vedi § 7)* |
| Costo e scalabilità | Ogni transazione viene rieseguita da tutti i nodi, e ogni operazione consuma gas | Codice e strutture dati efficienti; usare `view` per le letture |
| Tooling obsoleto | Truffle non è più mantenuto e ha problemi di sicurezza | Usare Hardhat o Foundry |

## 4. Esempi e codice

### Contratto `Storage` (demo di lezione)

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract Storage {
    uint256 number;                       // variabile di stato: persiste on-chain

    function store(uint256 num) public {  // modifica lo stato → transazione + gas
        number = num;
    }

    function retrieve() public view returns (uint256) { // sola lettura
        return number;
    }
}
```

A lezione è stato deployato anche **`Storage Two`** (funzioni `store2` / `retrieve2`) **sulla stessa chain locale**: sono due contratti indipendenti con indirizzi diversi.

### Workflow su Remix (da saper rifare all'esame)

1. **Editor:** apri o crea il `.sol` nel file explorer.
2. **Compile:** scegli la versione del compilatore e compila. Si ottengono bytecode e ABI.
3. **Deploy:** ambiente **Remix VM**, cioè una chain locale con **15 account di test da 100 ETH finti**. Il deploy viene minato nel *Block 1* e il saldo dell'Account 1 scende (es. a 99,9… ETH) per il gas.
4. **Interazione:** chiama `store(150)` da un account e `store(76)` da un altro (a lezione Account 3 e Account 7). Ogni chiamata è una tx con hash, blocco e gas, e scala il saldo del chiamante.
5. **Lettura:** `retrieve()` restituisce l'ultimo valore salvato (150, poi 76).
6. **Log:** nel terminale controlla hash, numero di blocco, gas usato e output decodificato.

### Variabili globali e tipi base

| Costrutto | Significato |
|---|---|
| `msg.sender` | indirizzo (account o contratto) che invoca la funzione |
| `msg.value` | ether (in wei) inviati con la chiamata |
| `block.*` | informazioni sul blocco corrente |
| `bool` | `true` / `false` |
| `int` / `uint` (es. `uint256`) | interi con/senza segno, a dimensione fissa |

### Ecosistema e risorse

- **Hardhat**, **Foundry:** framework standard per compilazione, script e test.
- **Truffle:** legacy, sconsigliato.
- **OpenZeppelin:** libreria di contratti sicuri e riutilizzabili.
- **Per imparare:** W3Schools (Solidity), assistente AI di Remix, CryptoZombies.

## 5. Quadro di riepilogo

**Concetti chiave**
- Solidity → bytecode EVM + ABI.
- Contratti immutabili: ogni aggiornamento è un nuovo deploy a un nuovo indirizzo, e il vecchio resta attivo.
- Esecuzione deterministica su tutti i nodi, quindi niente random nativo.
- Le tx che modificano lo stato costano gas, le letture `view` no (se chiamate dall'esterno).
- Testare in locale prima del mainnet, perché lì vale *code is law*.

**Parole chiave:** Solidity · EVM · bytecode · ABI · Remix VM · deploy · gas · immutabilità · determinismo · `view` · `msg.sender` · `msg.value` · Hardhat · Foundry · OpenZeppelin

**Domande d'esame**

<details>
<summary>1. Cosa produce la compilazione di un contratto Solidity e a cosa serve ciascun output?</summary>

Bytecode EVM, salvato on-chain ed eseguito dalla EVM di ogni nodo, e ABI, la descrizione in JSON di funzioni, parametri e tipi di ritorno, che le dApp usano per codificare le chiamate e decodificare i risultati.
</details>

<details>
<summary>2. Ho deployato un contratto con un bug: posso correggerlo?</summary>

No, il bytecode è immutabile. Devo deployare un nuovo contratto, che avrà un nuovo indirizzo. Il vecchio resta attivo, quindi la dApp deve migrare. Per questo i test pre-deploy sono fondamentali.
</details>

<details>
<summary>3. Perché in Solidity non esiste una funzione random nativa?</summary>

Perché tutti i nodi rieseguono ogni transazione e devono ottenere lo stesso stato (determinismo). Un valore davvero casuale darebbe risultati diversi su nodi diversi e romperebbe il consenso.
</details>

<details>
<summary>4. Differenza tra chiamare <code>store</code> e <code>retrieve</code> su Remix?</summary>

`store` modifica lo stato: genera una transazione minata in un blocco, con hash e costo in gas scalato dal saldo del chiamante. `retrieve` è `view`: legge lo stato e restituisce il valore senza transazione.
</details>

<details>
<summary>5. Cosa succede ai saldi degli account di test in Remix VM e perché?</summary>

Partono da 100 ETH finti. Ogni deploy o tx che modifica lo stato riduce il saldo dell'account che la invia, per il gas consumato.
</details>

<details>
<summary>6. Quale analogia lega EVM e JVM?</summary>

In entrambi i casi un linguaggio ad alto livello viene compilato in bytecode eseguito da una macchina virtuale. La differenza è che la EVM gira su ogni nodo e l'esecuzione deve essere deterministica e pagata in gas.
</details>

<details>
<summary>7. Quali strumenti usare oggi per sviluppare e testare smart contract?</summary>

Remix per prototipazione, Hardhat o Foundry per sviluppo e test professionali, OpenZeppelin per componenti sicuri. Truffle è sconsigliato.
</details>

## 6. ⚠️ Parte non registrata

La registrazione si interrompe durante i tipi di dato base. **Da integrare dalle slide o da Panopto.** Probabili argomenti successivi (da confermare): `address`, `mapping`, `struct`, `enum`, visibilità (`public` / `private` / `internal` / `external`), `view` / `pure` / `payable`, `modifier`, `event`.

> _[Placeholder: inserire qui il contenuto]_

## 7. Approfondimenti (non dalla lezione)

- **`storage` vs `memory`:** `storage` è persistente on-chain e costoso, `memory` è temporanea, solo per la durata della chiamata.
- **Randomness sicura:** oracoli (es. Chainlink VRF) o schemi commit-reveal.

---

### Da verificare

- [ ] Integrare la mezz'ora finale (§ 6) da slide o Panopto
- [ ] Link alle slide e alla registrazione Panopto
- [ ] Versione del compilatore usata a lezione (`pragma`)
- [ ] Indirizzi esatti mostrati nella demo di redeploy (`…138` / `…E07`)
- [ ] Se Ferretti ha dato indicazioni sul project work legate a Remix/Hardhat

### Fonti e verifica

Riassunto Plaud della lezione del 26/10/2026; slide del corso. Le sezioni § 6 e § 7 non derivano dall'audio della lezione.
