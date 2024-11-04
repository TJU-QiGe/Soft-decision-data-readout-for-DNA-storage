#!/bin/bash
echo "Begin Processing time :" `date` 
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

##-----------step4:soft-decoding--------------------------
	#soft-decoding program inputfile
	inputDir=./multiple_read_probability_merging/result/genome-A
	outputDir=./decoding_process/result

	if [ ! -d "$outputDir" ]; then
		mkdir -p "$outputDir"
	fi
	inputFile=$inputDir/Soft_infor_consensus.txt
	#soft-decoding program result output
	correctedBitStream=$outputDir/Plasmid_A_corrected_bits.txt
	plasmidARecovery=$outputDir/Dreams.txt
	#program execution command
	./decoding_process/ldpc_r1_4_soft_decoder  $inputFile   $correctedBitStream  $plasmidARecovery  S
	
echo "End Processing time :" `date`
