try:
    from xml.etree.cElementTree import XML
    import xml.etree.cElementTree as ET 
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
import GeneralFuntions
generalFunctions=GeneralFuntions.General()
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
WORD_PARA = 'p'
WORD_TEXT = 't'  
global LenghtListOutput=0
zipFolder=''
class DocxExtractor:

    def __init__(self):
        pass  
    
    #/........Read text from doc......../    
    def GetCount(self):
        print('LenghtListOutput=',LenghtListOutput)
        return LenghtListOutput
    
    def SetCount(seft,count):
        global LenghtListOutput
        LenghtListOutput=count
        
    def GetZipFolder(self):
        print('zipFolder=',zipFolder)  
        
        return zipFolder
    def SetZipFolder(self,zipfolder):
        global zipFolder
        zipFolder=zipfolder

    def ReadWordText(self,inputPath,outputTextFilepath):
        """
        Take the path of a docx file as argument, return the text in unicode.
        """     
        folderZipFile=generalFunctions.extraZipfile(inputPath)
        if(folderZipFile==None):
            print ('Error When Extral file')
            return None 
        DocxExtractor.SetZipFolder(self,folderZipFile)
        xmlListFilePath=generalFunctions.GetPathWordXml(folderZipFile)
        print('xmlFilePath is:',xmlListFilePath)
        paragraphs = list()        
        for xmlPath in xmlListFilePath:
            paragraphs=generalFunctions.ReadTextXmlFile(xmlPath,WORD_NAMESPACE,WORD_PARA,WORD_TEXT)
        DocxExtractor.SetCount(self,paragraphs.count)
        jsonTextList=generalFunctions.ConvertStringToJson(paragraphs)
        generalFunctions.WriteTextFile(jsonTextList, outputTextFilepath)        
        return jsonTextList            
        #........Write Text ...................#
    def WriteTextFromJson(seft, inputPath,textListJson):
        textListInput=list()
        textListInput=generalFunctions.ConvertJsonToString(textListJson)
        if(textListInput.count==DocxExtractor.GetCount(seft)):
            i=0
            print("number item correct, do write")
            xmlListFilePath=generalFunctions.GetPathWordXml(inputPath)
            print('xmlFilePath is:',xmlListFilePath)
            for xmlPath in xmlListFilePath:
                i=generalFunctions.WriteTextXmlFile(xmlPath,WORD_NAMESPACE,WORD_PARA,WORD_TEXT,textListInput,i)            
            generalFunctions.CompressOfficeFolder(inputPath,'word.zip')
        else:
            print("number item incorrect, exit")
            