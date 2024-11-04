#!/bin/bash
echo "Begin Processing time :" `date` 

  outDir=./watermark_alignment/result/genome-A
 
  if [ ! -d "$outDir" ]; then
	mkdir -p "$outDir"
  fi
#######################-Input Parameters and Output Parameters-############################
	#Sequencing duplex read
	inputFastq=./nanopore_duplex_fastq/Dorado_barcode02_duplex.fastq
	#Readout-aware ideal watermark sequence
	watermark=./watermark_alignment/SequenceLengthALL_FILE001R025
	#Plasmid vector sequences
	plasmidHead=./watermark_alignment/Plasmid-A-head.txt
	plasmidTail=./watermark_alignment/Plasmid-A-tail.txt
	#Output file of watermark alignment results
	resultOutput=$outDir/Watermark_alignment_result_output.txt
	
#######################-Program running-############################
	./watermark_alignment/watermark_alignment $inputFastq $watermark $plasmidHead $plasmidTail $resultOutput
	
echo "End Processing time :" `date`
