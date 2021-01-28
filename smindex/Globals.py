import numpy as np
import os

#try and find the SMINDEX_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('SMINDEX_PATH')+'/'
	
	#if this is successful - now check whether the subdirectories exist
	dlddir = DataPath + 'download/'
	bindir = DataPath + 'binary/'
	if not os.path.isdir(dlddir):
		os.system('mkdir -pv '+dlddir)
	if not os.path.isdir(bindir):
		os.system('mkdir -pv '+bindir)
except:
	print('Please set SMINDEX_PATH environment variable')
	DataPath = ''

#this is the data type for the recarray which will store the indices
#The regional SME,SMU,SML indices are centred on a 3-hour MLT range 
#equal to the index + 0.5 - i.e. SMEr[12] corresponds to 11:00 - 14:00 MLT)
#Regional versions of SMR are centered on a 6 hour MLT window, 
#i.e. SMR00 corresponds to 21:00 to 03:00 MLT
idtype = [	('Date','int32'),			#Date in the format yyyymmdd
			('ut','float32'),			#Time in hours since the start of the day
			('utc','float64'),			#Continuous time since 1950 (in hours)
			('SME','float32'),			#Global SME index
			('SML','float32'),			#Global SML index
			('SMU','float32'),			#Global SMU index
			('MLTSML','float32'),			#Global SML index MLT
			('MLTSMU','float32'),			#Global SMU index MLT
			('MLATSML','float32'),			#Global SML index Latitude
			('MLATSMU','float32'),			#Global SMU index Latitude
			('SMEr','float32',(24,)),	#Regional SME index 
			('SMLr','float32',(24,)),	#Regional SML index
			('SMUr','float32',(24,)),	#Regional SMU index
			('SMR','float32'),			#Global SMR index
			('SMR00','float32'),		#SMR near midnight
			('SMR06','float32'),		#SMR near dawn
			('SMR12','float32'),		#SMR near noon
			('SMR18','float32')]		#SMR near dusk
			
