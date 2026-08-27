# 🧬 DNovix

## Turning DNA Into Insights

DNovix is an interactive DNA sequence analysis application developed using **Python and Streamlit**.

It allows users to analyze DNA sequences and obtain important sequence-level information such as nucleotide composition, GC/AT content, complementary sequences, reverse complement, mRNA sequence, ORFs, and protein translation.

DNovix is designed as an educational bioinformatics tool to demonstrate how biological sequence analysis can be implemented using Python.

---

## ✨ Features

* 🧬 DNA sequence validation
* 📏 DNA sequence length calculation
* 🧪 Nucleotide base composition analysis
* 🟢 GC% and AT% calculation
* 🔄 Complementary DNA sequence
* ↩️ Reverse complement sequence
* 🧫 mRNA sequence generation
* 🔎 ORF detection in forward and reverse reading frames
* 🧬 Protein translation
* 📊 Base composition visualization
* 📥 Downloadable DNA analysis report

---

## 🛠️ Technologies Used

* 🐍 Python
* 🎈 Streamlit
* 🐼 Pandas
* 📊 Plotly

---

## ⚙️ How It Works

DNovix follows a simple DNA sequence analysis workflow:

1. User enters a DNA sequence.
2. The sequence is validated for valid DNA bases: A, T, G, and C.
3. DNA sequence length is calculated.
4. Individual nucleotide bases are counted.
5. GC% and AT% are calculated.
6. Complementary DNA sequence is generated.
7. Reverse complement sequence is generated.
8. DNA is transcribed into mRNA.
9. ORFs are detected across forward and reverse reading frames.
10. DNA is translated into amino acid sequences.
11. A complete analysis report can be downloaded as a text file.

---

## 🔎 ORF Analysis

DNovix identifies Open Reading Frames (ORFs) by searching for a start codon followed by a valid stop codon.

### Start Codon

ATG


### Stop Codons

TAA
TAG
TGA

ORF detection is performed across six reading frames:

* Forward Frame 0
* Forward Frame 1
* Forward Frame 2
* Reverse Frame 0
* Reverse Frame 1
* Reverse Frame 2

The application reports:

* Forward ORF count
* Reverse ORF count
* Total ORF count

---

## 🧬 Protein Translation

DNovix translates the DNA sequence into amino acid sequences using the standard genetic code.

Each three-base codon is mapped to its corresponding amino acid.

Examples:

ATG → M
GCT → A
TGG → W

Stop codons are represented by:

*


The resulting protein sequences are displayed separately in the application.

---

## 📊 Base Composition Analysis

DNovix calculates the number of each nucleotide present in the DNA sequence:

* Adenine (A)
* Thymine (T)
* Guanine (G)
* Cytosine (C)


A Plotly bar chart is used to visualize nucleotide composition.

---

## 🔄 Derived Sequences

DNovix generates three important derived sequences.

### Complementary DNA

The complementary strand is generated using standard base pairing:

A ↔ T
G ↔ C


### Reverse Complement

The complementary sequence is reversed to generate the reverse-complementary strand.

### mRNA

The DNA sequence is transcribed into mRNA by replacing:

T → U


---

## 📥 Analysis Report

DNovix provides an option to download the analysis results as a `.txt` file.

The report contains:

* DNA sequence
* Sequence length
* Base composition
* GC content
* AT content
* Complementary sequence
* Reverse complement
* mRNA sequence
* Forward ORFs
* Reverse ORFs
* Total ORFs
* Protein sequences

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DNovix.git
```

### 2. Navigate to the Project Directory

```bash
cd DNovix
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the application using Streamlit:

```bash
streamlit run "DNovix V1.py"
```

The application will open in your default web browser.

---

## 📁 Project Structure


DNovix/
│
├── .gitignore
├── DNovix V1.py
├── README.md
└── requirements.txt


### File Description

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| DNovix V1.py    | Main Python source code for the DNA analysis application |
| requirements.txt| Python dependencies required to run the application      |
| README.md        | Project documentation                                    |
| .gitignore       | Specifies files and folders ignored by Git               |

---

## 🖥️ Application Workflow


DNA Sequence Input
        ↓
Sequence Validation
        ↓
Sequence Length
        ↓
Base Composition
        ↓
GC% / AT%
        ↓
Complement
        ↓
Reverse Complement
        ↓
mRNA Generation
        ↓
Six-Frame ORF Detection
        ↓
Protein Translation
        ↓
Analysis Report


---

## 🎯 Project Purpose

DNovix was developed as a learning-oriented bioinformatics project combining:

* Molecular Biology
* Microbiology
* Python Programming
* Bioinformatics
* Data Visualization

The project demonstrates how fundamental DNA sequence analysis concepts can be implemented as an interactive computational application.

---

## 🔮 Future Improvements

Future versions of DNovix may include:

* FASTA file upload
* FASTQ file support
* Restriction enzyme analysis
* Codon usage analysis
* Amino acid composition analysis
* Sequence motif detection
* Improved ORF visualization
* Gene annotation
* Interactive sequence visualization
* Additional bioinformatics analysis modules

---


