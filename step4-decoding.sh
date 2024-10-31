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
	inputFile=$inputDir/soft_infor_consensus.txt
	#soft-decoding program result output
	S_correctedBitStream=$outputDir/plasmid_A_S_correctedBitStream.txt
	plasmid_A_recovery=$outputDir/Dreams.txt
	#program execution command
	./decoding_process/LDPC_r1_4_decoder_soft  $inputFile   $S_correctedBitStream  $plasmid_A_recovery  S
	
echo "End Processing time :" `date`
