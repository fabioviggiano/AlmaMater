# Manuale di Studio: Teoria e pratica della Network Analysis

---

## 📑 Indice
1. [Introduzione Generale](#introduzione-generale)
2. [Capitolo 1: Introduzione alla Network Analysis](#capitolo-1-introduzione-alla-network-analysis)
3. [Capitolo 2: La Progettazione della Ricerca (Research Design)](#capitolo-2-la-progettazione-della-ricerca-research-design)
4. [Capitolo 3: Modelli Matematici delle Reti](#capitolo-3-modelli-matematici-delle-reti)
5. [Capitolo 4: Raccolta e Gestione dei Dati](#capitolo-4-raccolta-e-gestione-dei-dati)
6. [Capitolo 5: Misure e Metriche I - I Nodi](#capitolo-5-misure-e-metriche-i---i-nodi)
7. [Capitolo 6: Misure e Metriche II - Le Reti](#capitolo-6-misure-e-metriche-ii---le-reti)
8. [Capitolo 7: Gestione di Reti di Grandi Dimensioni](#capitolo-7-gestione-di-reti-di-grandi-dimensioni)
9. [Capitolo 8: Testing di Ipotesi su Dati di Rete](#capitolo-8-testing-di-ipotesi-su-dati-di-rete)
10. [Capitolo Finale: Guida Pratica all'Esame](#capitolo-finale-guida-pratica-alla-preparazione-dellesame)

---

## Introduzione Generale
Questo manuale è concepito come guida per trasformare i concetti teorici della Network Analysis in un percorso di apprendimento strutturato, finalizzato al superamento dell'esame tramite un **Project Report**.

### 1.1 Obiettivi Formativi
*   **Astrarre e Modellare**: Ridurre sistemi complessi a strutture di nodi e archi.
*   **Misurare e Quantificare**: Utilizzare metriche matematiche per descrivere nodi e intere reti.
*   **Progettare una Ricerca**: Formulare ipotesi e raccogliere dati in modo scientifico.
*   **Interpretare i Risultati**: Tradurre i numeri in conclusioni significative.

### 1.2 La Struttura dell'Esame
L'esame consiste in un report di gruppo (~5000 parole) che simula un articolo scientifico:
1.  Contesto e Problema (Domanda di ricerca).
2.  Dati e Metodi.
3.  Risultati e Interpretazione.
4.  Conclusioni e Limiti.

---

## Capitolo 1: Introduzione alla Network Analysis

### 1.1 Il Potere dell'Astrazione
Una rete è un modello semplificato che cattura solo i pattern di connessione (**topologia**). 
*   **Nodi (Nodes/Vertices)**: Le entità (persone, geni, aeroporti).
*   **Archi (Edges/Links/Ties)**: Le relazioni (amicizia, flussi, citazioni).

### 1.2 Visualizzazione
Strumento esplorativo fondamentale per identificare:
*   **Hubs**: Nodi super-connessi.
*   **Clusters**: Gruppi densi.
*   **Bridges**: Ponti tra comunità diverse.

---

## Capitolo 2: La Progettazione della Ricerca (Research Design)

### 2.1 Whole-network vs. Personal-network
*   **Whole Network**: Studio di tutti i legami in un gruppo definito (es. tutti i dipendenti di un'azienda).
*   **Personal Network (Egocentrata)**: Studio di un nodo focale ("ego") e dei suoi contatti ("alter").

### 2.2 Tipologie di Legami

| Categoria | Descrizione | Esempi |
| :--- | :--- | :--- |
| **Similitudini** | Condivisione di attributi | Stessa nazionalità, co-presenza |
| **Ruoli Relazionali** | Legami formali/istituzionalizzati | Capo/Dipendente, Fratelli |
| **Cognizione** | Percezione soggettiva | Amicizia, Stima |
| **Interazioni** | Scambi osservabili | Invio di email, conversazioni |
| **Flussi** | Trasferimento di risorse | Denaro, Informazioni, Virus |

### 2.3 Considerazioni Etiche
Nelle reti l'anonimato è quasi impossibile (i nodi devono essere nominati per costruire i legami). Si parla quindi di **confidenzialità** e trasparenza sui rischi.

---

## Capitolo 3: Modelli Matematici delle Reti

### 3.1 La Matrice di Adiacenza (A)
È la rappresentazione fondamentale. Matrice quadrata $N \times N$.
*   $A_{ij} = 1$: Legame presente.
*   $A_{ij} = 0$: Legame assente.

### 3.2 Tipi di Grafi
*   **Diretti (Digraphs)**: Gli archi hanno un verso (es. Twitter follower). Matrice asimmetrica.
*   **Pesati**: Gli archi hanno un valore d'intensità. Matrice con numeri reali.
*   **Bipartiti**: Due tipi di nodi (es. Attori e Film), i legami esistono solo tra insiemi diversi.

---

## Capitolo 4: Raccolta e Gestione dei Dati

### 4.1 Formati delle domande
*   **Closed-ended (Roster)**: Lista predefinita di nomi. Evita errori di memoria ma è pesante per reti grandi.
*   **Open-ended (Free-listing)**: Il rispondente nomina liberamente gli altri. Rischio di dimenticanze (Recall bias).

### 4.2 Trasformazione dei Dati
*   **Symmetrisation**: Rendere la rete non-diretta (usando logica AND o OR).
*   **Dichotomisation**: Trasformare una rete pesata in binaria usando una soglia (*cut-off*).

---

## Capitolo 5: Misure e Metriche I - I Nodi

### 5.1 Centralità: Chi è importante?

| Metrica | Significato | Uso nel Progetto |
| :--- | :--- | :--- |
| **Degree** | Numero di connessioni dirette | Trovare i più popolari o attivi. |
| **Eigenvector** | Connessione a nodi a loro volta importanti | Misurare prestigio o influenza. |
| **PageRank** | Importanza "divisa" tra i vicini | Analisi di reti dirette (Web, citazioni). |
| **Closeness** | Vicinanza media a tutti gli altri nodi | Studiare la velocità di diffusione. |
| **Betweenness** | Frequenza con cui un nodo è sul cammino più breve | Trovare i broker o intermediari. |

### 5.2 Buchi Strutturali (Structural Holes)
Un nodo che collega gruppi che altrimenti non parlerebbero tra loro ha un vantaggio di controllo e informativo (*brokerage*).

---

## Capitolo 6: Misure e Metriche II - Le Reti

### 6.1 Proprietà Macro-strutturali
*   **Small-World**: Alta clusterizzazione locale ma bassa distanza media (scorciatoie).
*   **Scale-Free**: Distribuzione a legge di potenza. Moltissimi nodi piccoli, pochissimi "hub" giganti.
*   **Assortatività**: Tendenza dei nodi a legarsi a simili (omofilia).

### 6.2 Coesione
*   **Densità**: Rapporto tra archi esistenti e possibili.
*   **Modularità**: Capacità della rete di dividersi in comunità distinte.

---

## Capitolo 7: Gestione di Reti di Grandi Dimensioni

### 7.1 La Sfida della Scala
Oltre certi numeri (milioni di nodi), il calcolo di metriche come la *betweenness* ($O(n^3)$) diventa impossibile. Si ricorre al **Subsampling**.

### 7.2 Tecniche di Campionamento

| Tecnica | Pro | Contro |
| :--- | :--- | :--- |
| **Node Sampling** | Semplice, unbiased sugli attributi | Distrugge la topologia (frammentazione). |
| **Induced Edge** | Preserva triangoli e clustering | Bias verso gli hub. |
| **Random Walk** | Esplora grandi componenti con poca memoria | Forte bias verso i nodi ad alto grado. |

---

## Capitolo 8: Testing di Ipotesi su Dati di Rete

### 8.1 Test di Permutazione
I dati di rete non sono indipendenti (violano i test statistici classici). 
Si usa il **confronto con mondi casuali**:
1. Si calcola la metrica sui dati reali.
2. Si mescolano (permutano) i dati migliaia di volte.
3. Si vede quante volte il caso produce un risultato estremo quanto il nostro (**p-value**).

### 8.2 QAP (Quadratic Assignment Procedure)
Tecnica specifica per correlare due matrici (es. La rete di amicizia è correlata a quella di scambio di consigli?).

---

## Capitolo Finale: Guida Pratica all'Esame

### 📝 Checklist per il Report
*   [ ] **Abstract**: Sintesi estrema di problema, metodo e risultati.
*   [ ] **Domanda di Ricerca**: Deve essere specifica (es. "Il ruolo della betweenness nel successo dei Medici").
*   [ ] **Giustificazione Metriche**: Perché hai usato il PageRank e non il Degree?
*   [ ] **Discussione Critica**: Riconoscere i limiti dei dati e i possibili bias del campionamento.

### ⚠️ Errori da evitare
1.  **Mancanza di interpretazione**: Non dare solo numeri, spiega cosa significano nel contesto.
2.  **Confondere Correlazione con Causalità**.
3.  **Visualizzazioni illeggibili**: Evitare l'effetto "gomitolo di lana" (hairball).

---
*Manuale ad uso degli studenti - Università di Bologna*
