#!/bin/bash
echo "Begin Processing time :" `date` 

	##-----------step2:indel correcting using forward and backward algorithm--------------------------
	
	inputDir=./watermark_alignment/result/genome-A
	outputDir=./soft_decision_FBA/result/genome-A

	if [ ! -d "$outputDir" ]; then
		mkdir -p "$outputDir"
	fi
	inputFile=$inputDir/watermark_alignment_result_output.txt
	readNum=30
	outputFile=$outputDir/downSample_${readNum}.txt
	line_count=$(wc -l < "$inputFile")
	half_count=$((line_count / 2))
	#--------------------------Random selection of sequencing reads----------------------------------------------------------
	./soft_decision_FBA/random_select_waterAlign_result $inputFile $half_count $readNum $outputFile
	
	#--------------------------indel correcting using soft-decision forward and backward algorithm-----------------------------------------------
	#Indel correcting program inputfile
	geno=TJ0083169-1-plasmid-A.txt
	water=SequenceLengthALL_FILE001R025
	watermark_len=40500 
	ins=0.005
	sub=0.005
	del=0.01
	plasmid_head=plasmid-A-head.txt
	plasmid_tail=plasmid-A-tail.txt
	waterAlignment_result=$outputFile
	
	#Indel correcting program result output
	outputFile=./$outputDir/indelCorrect_output_Soft_decision.txt
	
	#program execution command
	./soft_decision_FBA/fb_soft_indel_corrrect $geno $waterAlignment_result $outputFile $water $watermark_len $ins $sub $del $plasmid_head $plasmid_tail

echo "End Processing time :" `date`
