
# 🧠 Plagiarism Detection Using Jaccard, MinHash & LSH

## 📌 Project Overview

This project builds a plagiarism detection system for documents using the following techniques:

- **Jaccard Similarity** with k-shingles
- **MinHash Signature Matrix** for scalable approximation
- **Locality Sensitive Hashing (LSH)** for fast detection of near-duplicates

The implementation uses custom Python modules in `plagiarism_lib` and analyzes real document pairs to detect and evaluate plagiarism.

---

## 🗂️ Project Structure

```
P1_Mohit_121330970/
├── data/                # Raw text files for training & evaluation
├── plagiarism_lib/      # Custom library implementing shingling, hashing, Jaccard, MinHash, and LSH
├── result_data/         # Output of experiments (CSV, .npy, result plots)
├── plagiarism.ipynb     # Main notebook for running and visualizing experiments
```

---

## 🧠 Methods Implemented

### 1. **Jaccard Similarity**
- Converts documents into sets of `k`-shingles (default `k=10`)
- Computes exact Jaccard similarity to compare overlap
- Used for baseline performance

### 2. **MinHash**
- Approximates Jaccard similarity using signature matrices
- Reduces dimensionality and speeds up comparisons
- Plots error (RMSE) as a function of number of hash functions

### 3. **Locality Sensitive Hashing (LSH)**
- Divides MinHash signatures into bands for efficient near-duplicate detection
- Helps scale to large corpora without pairwise comparisons
- Plots precision and recall vs. LSH threshold

---

## 📊 Experiments

- **Effect of k-shingle size** on plagiarism vs. non-plagiarism detection
- **RMSE** of MinHash estimates vs. number of hash functions
- **Precision & Recall** curves for LSH at different similarity thresholds

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/mohitsalur/plagiarism-detection-lsh.git
cd plagiarism-detection-lsh
```

2. Create a virtual environment and install requirements:
```bash
pip install -r requirements.txt
```

3. Run the notebook:
```bash
jupyter notebook plagiarism.ipynb
```

---

## ✅ Features

- `plagiarism_lib` includes:
  - `shingling.py` – k-shingle generation
  - `jaccard.py` – Jaccard similarity
  - `minhash.py` – MinHash matrix + similarity estimator
  - `lsh.py` – Locality Sensitive Hashing

- Notebooks produce:
  - Precision-recall graphs
  - RMSE comparisons
  - Threshold tuning

---

## 🚫 Note on Data

Large `.txt`, `.csv`, and `.npy` files in `data/` and `result_data/` are **excluded** from version control using `.gitignore`.

---

## 📁 To Do (optional)
- Add Flask API to run plagiarism checks on new text
- Expand to paragraph-level detection
- Visualize document clusters with t-SNE or PCA

---

## 👤 Author

**Mohit Saluru**  
University of Maryland, College Park  
Course Project | Algorithms | Spring 2025
