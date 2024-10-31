#! /bin/bash

echo "Begin Processing time :" `date`

	inputDir=./soft_decision_FBA/result/genome-A
	outputDir=./multiple_read_probability_merging/result/genome-A

	if [ ! -d "$outputDir" ]; then
		mkdir -p "$outputDir"
	fi
	
	inputFile=$inputDir/indelCorrect_output_Soft_decision.txt
	geno=genomefile_A.txt
	outputFile=$outputDir/soft_infor_consensus.txt
	water=SequenceLengthALL_FILE001R025

	./multiple_read_probability_merging/LLRmerging $geno $inputFile $outputFile $water
	
	echo "End Processing time :" `date`
