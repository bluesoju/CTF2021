import sys

bin_dna = {'00':'A','10':'C','01':'G','11':'T'}


def bin_2_code(string):
	string = string.replace(" ","")
	string = string.replace("\n","")
	final=""
	for j in range(0,len(string),2):
		final+=bin_dna[string[j:j+2]]
	return final

def decode_dna(string):
    final= ""
    for i in range(0,len(string),3):
        final+=mapping[string[i:i+3]]
    return final

if len(sys.argv) < 2:
	print("Usage: python dna.py [file_name]")
else:
	input_string = open(sys.argv[1]).read().replace(" ","")
	print(" ")
	print(decode_dna(bin_2_code(input_string)))
