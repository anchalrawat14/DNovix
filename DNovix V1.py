import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
         page_title="DNA ANALYSIS",
         page_icon= "🧬",
         layout= "wide")

with st.sidebar:
    st.markdown(
        """
        <h2 style="color:#00c9a7;">🧬 DNovix</h2>
        <p style="color:#cbd5e1;">Version 1.0</p>
        <hr>
        <p><b>👩‍💻 Developer</b></p>
        <p style="color:#00c9a7;"><b>Anchal Rawat</b></p>
        <hr>
        <p style="font-size:13px; color:#94a3b8;">
        Turning DNA Into Insights
        </p>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
"""
<style>
.stApp {
   background: radial-gradient(
    circle at 50% 0%,
    #071a1a 0%,
    #03050a 50%,
    #000000 100%
);
}
</style>
""",
unsafe_allow_html=True
)

st.markdown("""
<style>

/* Input box */
.stTextArea textarea{
    background-color:#151826 !important;
    color:white !important;
    border:2px solid #00c9a7 !important;
    border-radius:12px !important;
    box-shadow:0 0 12px rgba(0,201,167,0.35) !important;
}

/* Click karne par glow */
.stTextArea textarea:focus{
    border:2px solid #00ffd5 !important;
    box-shadow:0 0 20px rgba(0,255,213,0.7) !important;
    outline:none !important;
}

</style>
""", unsafe_allow_html=True)
 


st.markdown(
"""
<h1 style="
color:#00c9a7;
text-shadow: 0 0 8px rgba(0,201,167,0.5);
"> 🧬 DNovix 
</h1>

<p style="
color:#cbd5e1;
text-shadow: 0 0 4px rgba(255,255,255,0.2);
">
🥈 Turning DNA Into Insight
</p>
""",
unsafe_allow_html=True
)
# Take DNA sequence input from user
dna = st.text_area("Enter DNA sequence",
                   height=120,
                   placeholder="Example: ATTGCGATG...").upper()

# if not dna:
#       st.stop()
if not dna:
    st.info("Please enter a DNA sequence.")
    st.stop()

# Validate DNA sequence
valid_bases = {"A", "T", "G", "C"} 
if not all(base in valid_bases for base in dna):
    st.error("❌ Invalid DNA sequence! Only A, T, G, and C are allowed.")
    st.stop()
length = len(dna) 
# Count individual nucleotide bases
a = dna.count("A")
t = dna.count("T") 
g = dna.count("G")
c = dna.count("C") 
gc_percent = round((g+c)/length*100,2)
at_percent = round((a+t)/length*100,2)



# Calculate sequence length
st.write("DNA\t :", dna)  
st.write("Length\t:", length)

base1=dna.replace("A","t")
base2=base1.replace("T","a")
base3=base2.replace("G","c")
base4=base3.replace("C","g")
mRNA= dna.replace("T","U")
complement= base4.upper()
reverse_complement= complement[::-1]

codons = {
    # Phenylalanine
    "TTT": "F", "TTC": "F",

    # Leucine
    "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",

    # Isoleucine
    "ATT": "I", "ATC": "I", "ATA": "I",

    # Methionine (Start)
    "ATG": "M",

    # Valine
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",

    # Serine
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "AGT": "S", "AGC": "S",

    # Proline
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",

    # Threonine
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",

    # Alanine
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    # Tyrosine
    "TAT": "Y", "TAC": "Y",

    # Histidine
    "CAT": "H", "CAC": "H",

    # Glutamine
    "CAA": "Q", "CAG": "Q",

    # Asparagine
    "AAT": "N", "AAC": "N",

    # Lysine
    "AAA": "K", "AAG": "K",

    # Aspartic Acid
    "GAT": "D", "GAC": "D",

    # Glutamic Acid
    "GAA": "E", "GAG": "E",

    # Cysteine
    "TGT": "C", "TGC": "C",

    # Tryptophan
    "TGG": "W",

    # Arginine
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    # Glycine
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",

    # Stop Codons
    "TAA": "*", "TAG": "*", "TGA": "*"}
proteins= ""
for i in range(0,len(dna),3):
      protein_code=dna[i:i+3]

      if len(protein_code)<3:
            break
      
      amino_acid= codons.get(str(protein_code),"X")
      proteins += amino_acid


# Defining start and stop codons for ORF detection
Stop_codons=("TAA","TGA","TAG")
Start_codon="ATG"

frame0_count=0
inside_orf=False
    
    # Searching for open reading frame 0 (ORFs)
start_index= None
for i in range(0,length-2,3):
        codon= dna[i:i+3]
        if codon== Start_codon and not inside_orf:
            inside_orf= True
            start_index=i
        elif codon in Stop_codons and inside_orf:
            frame0_count +=1
            inside_orf=False
    

        # Searching for open reading frame 1 (ORFs)

frame1_count=0
inside_orf=False
for i in range(1,length-2,3):
            codon= dna[i:i+3]
            if codon== Start_codon and not inside_orf:
                inside_orf= True
                start_index=i
            elif codon in Stop_codons and inside_orf:
                frame1_count +=1
                inside_orf=False
    

        # Searching for open reading frame 2 (ORFs)

frame2_count=0
inside_orf=False
for i in range(2,length-2,3):
            codon= dna[i:i+3]
            if codon== Start_codon and not inside_orf:
                inside_orf= True
                start_index=i
            elif codon in Stop_codons and inside_orf:
                frame2_count +=1
                inside_orf=False


def r_frame(reverse_complement,frame):
        count=0
        inside_orf=False

        for i in range(frame,len(reverse_complement)-2,3):
                codon= reverse_complement[i:i+3]
                if codon== Start_codon and not inside_orf:
                    inside_orf= True
                    # start_index=i
                elif codon in Stop_codons and inside_orf:
                    count +=1
                    inside_orf=False
        return count
R_frame0=r_frame(reverse_complement,0)
R_frame1=r_frame(reverse_complement,1)
R_frame2=r_frame(reverse_complement,2)

Reverse_ORFs=(R_frame0 + R_frame1 + R_frame2)
Forward_ORFs=(frame0_count + frame1_count + frame2_count)
total_orfs=(Reverse_ORFs + Forward_ORFs)


col1,col2,col3,col4,col5=st.columns(5)

with col1:
    st.metric("Length",length,"bp")
with col2:
    st.metric("🔎 Total ORFs :",total_orfs)

st.divider()
# st.subheader("BASE COMPOSITION")
# st.write("-"*30)
# st.write("A\t\t:",a)
# st.write("G\t\t:",g)
# st.write("T\t\t:",t)
# st.write("C\t\t:",c)

df= pd.DataFrame({
         "Base": ["A","T","G","C"],
         "Count": [a,t,g,c]
    })

fig=px.bar(
         df,
         x="Count",
         y="Base",
         orientation="h",
         text="Count",
         title="Base Composition"
    )

st.plotly_chart(fig,use_container_width=False)


with col3:
    st.metric("🟢 GC %",str(gc_percent) + "%")
with col4:
    st.metric("🟠 AT %:",str(at_percent) + "%")
with col5:
    st.metric("✅ Valid Sequence","Yes")
st.divider()

st.subheader("🧬 DNA Sequence")
st.code(dna, language=None)


st.divider()
st.subheader("DERIVED SEQUENCES")
st.divider()
# Generate complementary and reverse complementary strand
st.write("Complementary strand\t:" , complement)
st.write("Reverse complement\t:" , reverse_complement) 
# Transcribe DNA to RNA
st.write("mRNA\t\t:" , mRNA)


st.divider()
left,right=st.columns(2)
with left:
    st.write("**Forward Frames**") 
    st.write("Forward Frame 0\t:", frame0_count)
    st.write("Forward Frame 1\t:", frame1_count)
    st.write("Forward Frame 2\t:", frame2_count)
with right:
    st.write("**Reverse Frames**")   
    st.write("Reverse Frame 0\t:", R_frame0)
    st.write("Reverse Frame 1\t:", R_frame1)
    st.write("Reverse Frame 2\t:", R_frame2)
st.divider()

c1,c2=st.columns(2)
with c1:
    st.write("Forward ORFs:",Forward_ORFs)
    st.write("Reverse ORFs:",Reverse_ORFs)

    st.write("Total ORFs:", total_orfs)

st.divider()
st.subheader("Proteins:")
prot=proteins.split("*")
count=1
for p in prot:
        if p:
            st.write("Protein",count,":",p)
            count +=1


st.divider()
st.success("DNA ANALYSIS SUCCESSFULLY COMPLETED")

st.subheader("NOW YOU CAN DOWNLOAD THE REPORT 👇")

protein_report= ""
count = 1
for p in prot:
    if p:
        protein_report+= f"Protein {count}:{p}\n"
        count +=1
report= f"""
==========================
        DNovix Report
==========================
DNA Sequence: {dna}
Length: {length} bp
Base Composition:
A:{a}
T:{t}
G:{g}
C:{c}
GC Content: {gc_percent}%
AT Content: {at_percent}%

Complement:
{complement}

Reverse Complement:
{reverse_complement}

mRNA:
{mRNA}

Forward ORFs:
Frame 0 : {frame0_count}
Frame 1 : {frame1_count}
Frame 2 : {frame2_count}

Reverse ORFs:
Frame 0 : {R_frame0}
Frame 1 : {R_frame1}
Frame 2 : {R_frame2}

Forward ORFs Total : {Forward_ORFs}
Reverse ORFs Total : {Reverse_ORFs}
Total ORFs : {total_orfs}

Proteins:
{protein_report}

==========================
Thank you for using DNovix.

We hope this analysis was helpful.
==========================
"""

st.download_button(
    label="📥 Download Analysis Report",
    data=report,
    file_name="DNovix_Report.txt",
    mime="text/plain"
)








