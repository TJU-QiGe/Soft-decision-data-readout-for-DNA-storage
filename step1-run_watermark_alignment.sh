#!/bin/bash
echo "Begin Processing time :" `date` 
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#gcc -o watermarkAlignment watermarkAlignment.c edlib.cpp -lstdc++ -lm
  
  outDir=./watermark_alignment/result/genome-A
 
  if [ ! -d "$outDir" ]; then
	mkdir -p "$outDir"
  fi
#######################-Input Parameters and Output Parameters-############################
	#Sequencing duplex read
	fastq=./nanopore_duplex_fastq/dorado_barcode02_duplex.fastq
	#Readout-aware ideal watermark sequence
	watermark=./watermark_alignment/SequenceLengthALL_FILE001R025
	#Plasmid vector sequences
	plasmid_head=./watermark_alignment/plasmid-A-head.txt
	plasmid_tail=./watermark_alignment/plasmid-A-tail.txt
	#Output file of watermark alignment results
	result_output=$outDir/watermark_alignment_result_output.txt
	
#######################-Program running-############################
	./watermark_alignment/watermarkAlignment $fastq $watermark $plasmid_head $plasmid_tail $result_output
	
echo "End Processing time :" `date`
