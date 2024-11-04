#!/bin/bash
echo "Begin Processing time :" `date` 

	##-----------step2:indel correcting using forward and backward algorithm--------------------------
	
	inputDir=./watermark_alignment/result/genome-A
	outputDir=./soft_decision_FBA/result/genome-A

	if [ ! -d "$outputDir" ]; then
		mkdir -p "$outputDir"
	fi
	inputFile=$inputDir/Watermark_alignment_result_output.txt
	readNum=30
	outputFile=$outputDir/Downsample_${readNum}.txt
	lineCount=$(wc -l < "$inputFile")
	halfCount=$((lineCount / 2))
	#--------------------------Random selection of sequencing reads----------------------------------------------------------
	./soft_decision_FBA/random_select_wateralign_result $inputFile $halfCount $readNum $outputFile
	
	#--------------------------indel correcting using soft-decision forward and backward algorithm-----------------------------------------------
	#Indel correcting program inputfile
    plasmidRef=TJ0083169-1-plasmid-A.txt
	watermarker=SequenceLengthALL_FILE001R025
	watermarkLen=40500 
	insErrorRate=0.005
	subErrorRate=0.005
	delErrorRate=0.01
	plasmidHead=Plasmid-A-head.txt
	plasmidTail=Plasmid-A-tail.txt
	waterAlignmentResult=$outputFile
	
	#Indel correcting program result output
	outputFile=./$outputDir/Indel_corrected_output.txt
	
	#program execution command
	./soft_decision_FBA/fb_soft_indel_corrrect $plasmidRef $waterAlignmentResult $outputFile $watermarker $watermarkLen $insErrorRate $subErrorRate $delErrorRate $plasmidHead $plasmidTail

echo "End Processing time :" `date`
