# Blind Deconvolution: Confronto tra Metodi Model-Based e Approcci Deep Learning Supervisionati

Esame di **Computational Imaging**

Questo progetto analizza e confronta due filosofie diverse per la risoluzione del problema della **Blind Deconvolution**: il recupero di un'immagine nitida da una sua versione sfocata senza conoscere a priori le caratteristiche del kernel di sfocatura.

## 📌 Introduzione al Problema

Il modello matematico della sfocatura è espresso dalla convoluzione:
$$y = k \otimes x$$

Dove:
*   **$y$**: L'immagine sfocata osservata.
*   **$k$**: Il kernel di sfocatura (blur) sconosciuto.
*   **$x$**: L'immagine nitida latente da recuperare.

L'obiettivo è stimare simultaneamente sia $x$ che $k$.

### Il Fallimento del MAP Standard
L'approccio teorico standard (Maximum A Posteriori - MAP) cerca la coppia $(x, k)$ statisticamente più probabile. Tuttavia, come dimostrato da **Levin et al.**, questo approccio tende a favorire soluzioni banali (*no-blur*). 
*   **Perché?** Un'immagine sfocata ha gradienti più bassi e risulta statisticamente "più semplice" e probabile rispetto alla versione nitida.
*   **Evidenza:** Solo nel 3% delle porzioni di immagine il modello MAP favorisce la versione nitida.

---

## 🛠️ Metodi a Confronto

Analizziamo due approcci opposti:

### 1. Model-Based: L'Algoritmo di Shan (2008)
Si basa su un modello matematico esplicito e su un processo di ottimizzazione iterativa.

*   **Funzione di Costo:** Bilancia la fedeltà ai dati e un *prior* sull'immagine che favorisce la sparsità dei gradienti.
*   **Strategia Piramidale (Coarse-to-Fine):** Stima il kernel partendo da una versione a bassa risoluzione per poi rifinirla, evitando minimi locali errati.
*   **Ottimizzazione Alternata:** Risolve il problema alternando la stima dell'immagine $x$ (mantenendo $k$ fisso) e la stima del kernel $k$ (mantenendo $x$ fissa).
*   **Limiti:** Elevata sensibilità all'intensità del blur e ai parametri iniziali.

### 2. Data-Driven: Rete Neurale U-Net
Approccio basato sull'apprendimento supervisionato che impara a rimuovere il blur osservando migliaia di esempi.

*   **Architettura:** Una **U-Net** con struttura Encoder-Decoder e **Skip Connections**. Queste ultime sono fondamentali per preservare i dettagli fini dell'immagine originale.
*   **Training:** Addestramento su un dataset di circa 10.000 coppie (immagine sfocata, immagine ground truth) generate sinteticamente.
*   **Vantaggi:** Robustezza alle sfocature intense e velocità di esecuzione (inferenza) quasi istantanea dopo il training.

---

## 🧪 Setup Sperimentale

*   **Dataset:** Immagini base dal dataset medico **C081**.
*   **Blur Sintetici:** 
    *   **Motion Blur:** Simula il movimento della camera (direzionale).
    *   **Gaussian Blur:** Simula sfocatura generale o defocus.
*   **Metriche:**
    *   **PSNR** (Peak Signal-to-Noise Ratio): Misura l'errore assoluto in dB.
    *   **SSIM** (Structural Similarity Index): Misura la somiglianza strutturale percepita (0-1).

---

## 📊 Risultati e Analisi

### Confronto Quantitativo

| Metodo | Livello Blur | PSNR (dB) ↑ | SSIM ↑ |
| :--- | :--- | :--- | :--- |
| **Shan** | Realistico | 23.32 | 0.6800 |
| **Shan** | Forte | 12.92 | 0.6000 |
| **U-Net** | Vario | **34.18** | **0.9056** |

### Analisi delle Performance
Dalla sperimentazione è emerso che:
1.  **Resilienza:** La U-Net mantiene performance elevate anche con blur intenso, dove l'algoritmo di Shan subisce un collasso qualitativo.
2.  **Stabilità:** Il grafico del PSNR al variare del parametro $\sigma$ (Gaussian Blur) mostra una linea quasi piatta per la U-Net, contro il declino rapido del metodo model-based.

---

## ⚖️ Conclusioni: Trade-off tra le Filosofie

| Caratteristica | Approccio Model-Based (Shan) | Approccio Data-Driven (U-Net) |
| :--- | :--- | :--- |
| **Dataset** | Non richiesto | Necessario (molto grande) |
| **Velocità** | Lento (iterativo) | Molto veloce (inferenza) |
| **Interpretabilità** | Alta (modello esplicito) | Bassa (Black box) |
| **Performance** | Sensibile ai parametri | Superiore e robusta |

### Note Aggiuntive: Fergus vs Shan
Mentre **Shan** utilizza una regolarizzazione generica per la sparsità, l'approccio di **Fergus** modella esplicitamente la distribuzione dei gradienti naturali tramite distribuzioni a coda pesante (*heavy-tailed*), utilizzando tecniche come Variational Bayes per preservare meglio i contorni senza sacrificare le texture.

---

## 🚀 Sviluppi Futuri
*   Addestramento su dataset con blur **non uniformi** per simulare movimenti reali più complessi.
*   Sperimentazione con architetture più avanzate come i **Vision Transformers**.

---
*Progetto sviluppato per il corso di Computational Imaging.*
