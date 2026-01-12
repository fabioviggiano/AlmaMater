# Esame di Computational Imaging

Questa cartella **contiene esclusivamente la presentazione e la documentazione teorica** relativa al progetto d'esame.

👉 **Il codice sorgente e il lavoro completo di implementazione** sono disponibili nel repository dedicato:

🔗 [**github.com/fabioviggiano/BlindDeconvolution**](https://github.com/fabioviggiano/BlindDeconvolution)

---

## 📂 Contenuto della cartella

In questa sezione è possibile consultare i materiali teorici e i risultati dell'analisi comparativa:

*   📄 **[Paper Scientifico (Levin et al.)](https://github.com/fabioviggiano/AlmaMater/blob/main/Computational%20Imaging/Understanding%20and%20evaluating%20blind%20deconvolution%20algorithms.pdf)**: L'articolo di riferimento analizzato per comprendere i limiti dell'approccio MAP standard.
*   📝 **[Report di Progetto (Markdown)](https://github.com/fabioviggiano/AlmaMater/blob/main/Computational%20Imaging/Blind%20Deconvolution%3A%20Confronto%20tra%20Metodi%20Model-Based%20e%20Approcci%20Deep%20Learning%20Supervisionati.md)**: Analisi dettagliata del confronto tra l'algoritmo di Shan et al. e la rete neurale U-Net.
*   📊 **[Slide della Presentazione (PDF)](https://github.com/fabioviggiano/AlmaMater/blob/main/Computational%20Imaging/Blind%20deconvolution%20-%20Confronto%20tra%20metodi%20model-based%20e%20approcci%20deep%20learning%20supervisionati.pdf)**: Supporto visivo utilizzato per l'esposizione orale.

---

## 🚀 Il Progetto

Il lavoro si concentra sulla **Blind Deconvolution**, affrontando il problema del recupero di immagini nitide attraverso due filosofie contrapposte:
1.  **Metodi Model-Based**: Implementazione e test dell'algoritmo di Shan (2008).
2.  **Approcci Data-Driven**: Addestramento e valutazione di una rete neurale **U-Net** con apprendimento supervisionato.

### Risultati in sintesi
Dalle sperimentazioni è emerso come l'approccio basato su **Deep Learning** offra una robustezza significativamente maggiore all'aumentare dell'intensità del blur, superando i limiti di convergenza dei metodi classici di ottimizzazione.

Per consultare il codice, i notebook di addestramento e i risultati completi, visita il [**repository principale**](https://github.com/fabioviggiano/BlindDeconvolution).

---
*Studente: Fabio Viggiano*  
*Corso: Computational Imaging*
