import os
import io
import GeneralFuntions
import chardet
generalFunctions=GeneralFuntions.General()
filePath=''
LengthOfList=0
class TXTExtractor:
	def __init__(self):
		pass
	def GetLength(self):
		return LengthOfList

	def SetLength(self, inputLength):
		global LengthOfList
		LengthOfList=inputLength

	def GetZipFolder(self): 
		return filePath

	def SetZipFolder(self, inpuzipfolder):
		global filePath
		filePath=inpuzipfolder
	def export_encoding(selt,InputPath):
		Dict={}
		Open_file=open(InputPath,'rb')
		Open_text=Open_file.read()
		result=chardet.detect(Open_text)
		Dict=result
		encoding=''
		encoding=Dict["encoding"]
		print("encoding is ",encoding)
		return encoding 	
	def ReadTextFromTXT(self,InputPath, outputTextFile):
		textList=list()
		folderZipFile=generalFunctions.extraZipfile(InputPath)	
		print('folderZipFile',folderZipFile)
		if(folderZipFile==None or os.path.exists(folderZipFile)==False):
			print('file not exit, return None')
			return None		
		TXTExtractor.SetZipFolder(self,folderZipFile)		
		file=open(folderZipFile,'r',encoding= TXTExtractor.export_encoding(self,InputPath))
		Open_text=file.read()
		textList.append(Open_text)
		print("text:",Open_text)
		jsonTextList=generalFunctions.ConvertStringToJson(textList)
		TXTExtractor.SetLength(self, len(textList))		
		generalFunctions.WriteTextFile(jsonTextList,outputTextFile)
		return outputTextFile
	def WriteTextFromJson(seft,inputPath,textListJson):
		textList=list()
		textList=generalFunctions.ConvertJsonToString(textListJson)
		text_file = open(inputPath, "w",encoding= TXTExtractor.export_encoding(self,InputPath))	
		for text in textList:
			text_file.write(text)
		text_file.close()
          
