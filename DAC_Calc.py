'''
This program performs simple calculations of digital to analog (DAC) samples based on parameters input at the top of the file. Samples are plotted with matplotlib and DAC codes are written to a text file.

The waveform generated is a sinusoid.
The DAC codes are in offset binary format.
'''

import math
import matplotlib.pyplot as plt

#INPUT PARAMETERS (UPDATE THESE)
Samples_Per_Cycle = 50				#Number of samples in a cycle of the baseband waveform
Phase_Offset_deg = 0				#Add a phase offset in degrees
Amplitude = 1					#Amplitude scaling factor (max = 1.0)
DAC_bits = 12					#DAC resolution
Output_Filename = "DAC_Waveform_Codes.txt"	#The filename for writing data

#CALCULATED PARAMETERS
Phase_Offset_rad = Phase_Offset_deg*math.pi/180
DAC_Fullscale = pow(2,DAC_bits)
DAC_Midscale = int(DAC_Fullscale/2)

#PRINT PARAMETERS
print()
print("Samples per cycle: ",Samples_Per_Cycle)
print("Phase offset: ",Phase_Offset_deg)
print("Amplitude: ",Amplitude)
print("Number of DAC bits: ",DAC_bits)
print("Number of DAC codes: ",DAC_Fullscale)
print("DAC mid-scale code: ",DAC_Midscale)
print()

#GENERATE SAMPLES
sample_dec=[]
for n in range(0,int(Samples_Per_Cycle)):
	sample_dec.append(int(DAC_Midscale*Amplitude*math.sin(2*math.pi*(n/Samples_Per_Cycle)+Phase_Offset_rad)+DAC_Midscale))

#PRINT BINARY CODES
sample_bin=[]
for n in range(0,int(Samples_Per_Cycle)):
	sample = bin(sample_dec[n])[2:]
	if len(sample) < DAC_bits:
		sample = str("0"*(DAC_bits - len(sample))) + sample
	sample_bin.append(sample)
	print(sample)

#PRINT TO FILE
with open(Output_Filename, "w") as file:
	for i in range(0,len(sample_bin)):
		file.write(sample_bin[i] + "\n")

#PLOT
plt.stem(sample_dec,'r')
plt.show()
