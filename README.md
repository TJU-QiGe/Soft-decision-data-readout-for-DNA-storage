![python version](https://img.shields.io/badge/python-3.9-blue)
![cpp version](https://img.shields.io/badge/c%2B%2B-11-orange)
![shell version](https://img.shields.io/badge/shell-Bash-yellowgreen)
![license](https://img.shields.io/badge/license-MIT-8A2BE2)

[![Static Badge](https://img.shields.io/badge/github-TJU--QiGe-54af7d)](https://github.com/TJU-QiGe/Pragmatic-Soft-Decision-Data-Readout-of-Encoded-Large-DNA)

<h1 id="TJU-QiGe">Pragmatic Soft-Decision Data Readout of Encoded Large DNA</h1>

## **Table of Contents**

- [About the project](#About-The-Project)
- [Note](#Note)
- [Files](#Files)
- [Modules](#Modules)
- [Example of usage](#Example-of-usage)
- [Figures](#Figures)
- [License](#license)


<h2 id="About-The-Project"><strong>About the project</strong></h2>

To address the insertion and deletion errors introduced by nanopore sequencing technology in DNA data storage, as well as the high complexity of sequence assembly techniques in the data recovery process, we propose a pragmatic soft-decision data readout method that enables assembly-free sequence reconstruction, indel error correction, and ultra-low coverage data readout.

Here we provide the code of the soft-decision data readout pipeline used for encoded large DNA. To enhance understanding and better monitor the running of our code, the process of data readout is divided into four programs with chained input and output, each corresponding to the core components of the proposed method: (1) watermark alignment; (2) soft-decision forward-backward algorithm; (3) soft information merging from multiple reads; (4) soft-decision decoding. These input and output files are provided along with the programs. The software is implemented in C/C++, and our executable calls are integrated into shell scripts, allowing for easy and quick deployment on different versions of Linux systems.

In our work, to demonstrate the feasibility of the proposed method, the third-generation nanopore sequencer was used to attempt to retrieve the files from a set of large DNA fragments (two plasmids of ~51k bp, a yeast artificial chromosome of 254,886 bp). Here we provide the reference sequence of a plasmid DNA sample (referred to as "Plasmid A"), which stores Tagore’s poetry and has a length of 51,339 bp. Additionally, we include sequencing reads obtained through rapid library preparation and nanopore sequencing, as well as related data readout files and programs.


<h2 id="Note"><strong>Note</strong></h2>

For detailed information on coding procedures and sequencing data for yeast artificial chromosomes, see the literature: Chen W, Han M, Zhou J, Ge Q, Wang P, Zhang X, et al. An artificial chromosome for data storage. Natl Sci Rev 2021;8:nwab086. https://doi.org/10.1093/nsr/nwab028

In addition, the program used for data assembly can be obtained from the following URL. In fact, any assembly software meeting the requirements can be used for sequencing read assembly. Other computer codes used in this work are available from the authors upon request.

Minimap2: https://github.com/lh3/minimap2

Miniasm: https://github.com/lh3/miniasm

RACON: https://github.com/isovic/racon

<h2 id="Files"><strong>Files</strong></h2>

### Table 1. Plasmid sequence, watermark sequence, and sequencing data used in our study.

<table>
<tr>
  <tr>
    <td style="font-weight: bold; text-align: left;">Files</td>
    <td style="font-weight: bold; text-align: left;">Storage location</td>
    <td style="font-weight: bold; text-align: left;">Description</td>
  </tr>
  <tr>
    <td>Dreams.txt</td>
    <td>Current catalog</td>
    <td>The text file stored in plasmid DNA contains poetry by Tagore and has a size of 2,025 bytes</td>
  </tr>
  <tr>
    <td>Genomefile_A.txt</td>
    <td>Current catalog</td>
    <td>Encoded payload sequence, length: 40,500 nucleotides</td>
  </tr>
  <tr>
    <td>TJ0083169-1-plasmid-A.txt</td>
    <td>Current catalog</td>
    <td>The synthesized plasmid sequence of 51,339 bp was used as a reference, which contains the payload and plasmid vector, referred to as “Plasmid A”</td>
  </tr>
  <tr>
    <td>SequenceLengthALL_FILE001R025</td>
    <td>Current catalog</td>
    <td>Watermark sequence</td>
  </tr>
  <tr>
    <td>Plasmid-A-head.txt</td>
    <td rowspan="2">Current catalog</td>
    <td rowspan="2">Plasmid vector sequences</td>
  </tr>
  <tr>
    <td>Plasmid-A-tail.txt</td>
  </tr>
  <tr>
    <td>Guppy_barcode02.zip</td>
    <td>nanopore_duplex_fastq</td>
    <td>Standard sequencing reads generated using Guppy single-strand basecalling software;
    Based on the nanopore sequencing signals of “Plasmid A”, the standard sequencing reads generated using the base-calling software Guppy have a compressed file size of 93.8 MB, containing 46,000 raw reads with an average length of 2,187 nt and an average sequencing error rate of 0.052.
  </td>
  </tr>
  <tr>
    <td>Dorado_barcode02_duplex.fastq</td>
    <td>nanopore_duplex_fastq</td>
    <td>Duplex sequencing reads generated using Dorado duplex basecalling software;
    Using the base-calling software Dorado, the duplex nanopore sequencing reads generated from the same plasmid A sample have a file size of 8.86 MB, containing 1,156 duplex raw reads with an average length of 3,982 nt and an average error rate of 0.009.
  </td>
    </tr>
</tr>
</table>


<h2 id="Modules"><strong>Modules</strong></h2>

### Table 2. Programs used for data readout from nanopore sequencing reads and input/output files.


<table>
<tr>
  <tr>
    <td style="font-weight: bold; text-align: left;">Program</td>
    <td style="font-weight: bold; text-align: left;">Input</td>
    <td style="font-weight: bold; text-align: left;">Output</td>
    <td style="font-weight: bold; text-align: left;">Description</td>
  </tr>
  <tr>
    <td>step1-run_watermark_alignment.sh</td>
    <td>1. Dorado_barcode02_duplex.fastq<br>2.&nbsp;SequenceLengthALL_FILE001R025<br>3. Plasmid-A-head.txt<br>4. Plasmid-A-tail.txt</td>
    <td>Watermark_alignment_result_output.txt</td>
    <td>Step 1: Run the "watermark_alignment" program to align sequencing reads with the aid of watermark.</td>
  </tr>
  <tr>
    <td>step2-run_soft_decision_FBA.sh</td>
    <td>1.&nbsp;Watermark_alignment_result_output.txt<br>2. TJ0083169-1-plasmid-A.txt<br>3. SequenceLengthALL_FILE001R025<br>4. Watermark_sequence<br>5. Watermark_length<br>6. Ins. error rate<br>7. Sub. error rate<br>8. Del. error rate<br>9. Plasmid-A-head.txt<br>10. Plasmid-A-tail.txt</td>
    <td>Indel_corrected_output.txt</td>
    <td>Step 2: Run "random_select_wateralign_result" to randomly select some sequencing reads from the watermark alignment results; Run the program "fb_soft_indel_corrrect" to identify indel errors of sequencing reads and convert them into probability information that can be decoded.</td>
  </tr>
  <tr>
    <td>step3-run_llr_merging.sh</td>
    <td>1. Indel_corrected_output.txt.<br>2. Genomefile_A.txt<br>3. SequenceLengthALL_FILE001R025</td>
    <td>Soft_infor_consensus.txt</td>
    <td>Step 3: Run the "llr_merging" program to obtain consensus soft information from multiple reads.</td>
  </tr>
  <tr>
    <td>step4-run_decoding.sh</td>
    <td>Soft_infor_consensus.txt</td>
    <td>1. Plasmid_A_corrected_bits.txt<br>2. Dreams.txt</td>
    <td>Step 4: Run the "ldpc_r1_4_soft_decoder" program to complete soft-decision decoding.</td>
  </tr>
    </tr>
</table>

<h2 id="Example-of-usage"><strong>Example of usage</strong></h2>

### 1. Run "step1-run_watermark_alignment.sh":

### Run the shell script like this:

`./step1-run_watermark_alignment.sh`

### The description of input and output files:
Input files:
- `Dorado_barcode02_duplex.fastq`: Duplex sequencing reads generated by Dorado software, used as raw data for data recovery.
- `SequenceLengthALL_FILE001R025`: Watermark sequence embedded in the designed encoded large DNA fragment, used to assist in locating raw reads.
- `Plasmid-A-head.txt & Plasmid-A-tail.txt`: Vector parts of the plasmid sequence, used to distinguish the payload region from the vector region in sequencing reads.

Output files:
- `Watermark_alignment_result_output.txt`: The result of watermark alignment. Run “step1-xx.sh”, you will obtain the file named “Watermark_alignment_result_output.txt” containing the read alignment results, which is saved in the folder “watermark_alignment/result/genome-A”. Each set of three lines contains the start position, length, and sequence of a read.


### 2. Run "step2-run_soft_decision_FBA.sh":


### Run the shell script like this:
`./step2-run_soft_decision_FBA.sh`

### The description of input and output files:
This script includes two functions: (1) randomly select a certain number of reads from the watermark alignment results for error correction; (2) identify indel errors in reads using the soft-decision forward-backward algorithm and output soft information for each encoded symbol.

Function 1 input files:
- `Watermark_alignment_result_output.txt`: The result generated after running “step 1”.
- `readNum=30`: The number of reads you want to select; here, “readNum=30” is used as an example.

Function 1 output files:
- `Downsample_30.txt`: File storing the randomly selected reads.

Function 2 input files:
- `TJ0083169-1-plasmid-A.txt`: Reference sequence of the plasmid, used to compare the residual substitution error rate after error correction.
- `SequenceLengthALL_FILE001R025`: Watermark sequence embedded in the designed encoded large DNA fragment, used to assist in identifying indel errors in raw reads.
- `Watermark length`: Length of the watermark sequence.
- `Ins. error rate & Sub. error rate & Del. error rate`: Parameters for insertion, substitution, and deletion error rates used in the Hidden Markov Model. These parameters are derived from observed sequencing read error characteristics.
- `Plasmid-A-head.txt & Plasmid-A-tail.txt`: Vector parts of the plasmid sequence, used to distinguish the payload region from the vector region in sequencing reads.

Function 2 output files:
- `Indel_corrected_output.txt`: The result after identifying indel errors. Run “step2-xx.sh”, you will obtain the file “Indel_corrected_output.txt” containing the soft information for each read after indel error correction, which is saved in the folder “soft_decision_FBA/result/genome-A”. Each set of three lines contains the start position, length, and soft information of each encoded symbol.v


### 3. Run "step3-run_llr_merging.sh":

### Run the shell script like this:
`./step3-run_llr_merging.sh`

### The description of input and output files:
Input files:
- `Indel_corrected_output.txt`: Soft information generated by program “step 2”.
- `SequenceLengthALL_FILE001R025`: Watermark sequence embedded in the designed encoded large DNA fragment, used to XOR with sequencing data to remove the watermark.
- `Genomefile_A.txt`: Encoded payload sequence, used as a reference to verify the error rate of the results from program “step 3”.

Output files:
- `Soft_infor_consensus.txt`: The result of indel correction. Run “step3-xx.sh”, you will obtain the consensus soft information file “Soft_infor_consensus.txt”, which is saved in the folder “multiple_read_probability_merging/result/genome-A”. The result contains two columns of probability information: the probability of “1” in the first column and the probability of “0” in the second column. This probability information will be used for soft-decision decoding.


### 4. Run "step4-run_decoding.sh":


### Run the shell script like this:
`./step4-run_decoding.sh`

### The description of input and output files:
Input files:
- `Soft_infor_consensus.txt`: Probability information of bits “1” and “0” generated by program “step 3”.

Output files:
- `Plasmid_A_corrected_bits.txt`: Decoded bit stream. Run “step4-xx.sh”, you will obtain the bitstream file “Plasmid_A_corrected_bits.txt” containing the decoded results, which is saved in the folder “decoding_process/result/genome-A”.
- `Dreams.txt`: Digital file recovered from the decoding result. In this example, the stored digital file is the poetry “Dreams”.

#### After running the above four shell scripts, the stored digital file `Dreams.txt` will be recovered from the nanopore sequencing reads.

<h2 id="Figures"><strong>Figures</strong></h2>

The source data and data visualization programs for `Figures 3b, c, d and 5e, f`, which represent the performance of the proposed methods, are also provided and can be found in the “Figures” folder of the repository. All code for data visualization was written in Python 3.9.

<h2 id="license"><strong>License</strong></h2>

Distributed under the MIT License. See `LICENSE` for more information.