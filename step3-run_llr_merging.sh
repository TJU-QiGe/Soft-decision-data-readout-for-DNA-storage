#! /bin/bash

echo "Begin Processing time :" `date`

	inputDir=./soft_decision_FBA/result/genome-A
	outputDir=./multiple_read_probability_merging/result/genome-A

	if [ ! -d "$outputDir" ]; then
		mkdir -p "$outputDir"
	fi
	
	inputFile=$inputDir/Indel_corrected_output.txt
	genome=Genomefile_A.txt
	outputFile=$outputDir/Soft_infor_consensus.txt
	watermarker=SequenceLengthALL_FILE001R025

	./multiple_read_probability_merging/llr_merging $genome $inputFile $outputFile $watermarker
	
	echo "End Processing time :" `date`
