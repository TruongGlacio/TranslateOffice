import sys
import DocxExtractor
import PPTExtractor
import ExcelExtractor
import GeneralFuntions
import ExTractorOffice
generalFunctions=GeneralFuntions.General()
def main():
    doc=DocxExtractor.DocxExtractor()
    ppt=PPTExtractor.PPTExtractor()   
    excel=ExcelExtractor.ExcelExtrator()
    extractorOffice=ExTractorOffice.ExtractorOffice()
    excelListText=list()
    excelListChange=list()
    docListText = list()
    docListChange = list()
    outputExcelTextFilePath='../excelText.txt'
    outputPPTTextFilePth='../PPTText.txt'
    outputDocxTextFilePth='../DocxText.txt'
    docInputPath='/media/glacio/Data/Translate/Project/【AINIX】【RS-Receiver】_Basic Design (v0.7)_VN (copy).docx'
    pptInputPath='/media/glacio/Data/Translate/Project/Bổ-sung_Quy-chế-lương_2018.pptx'
    excelInputPath='/media/glacio/Data/Translate/Project/test.xlsx'
    
    # /..........test for docx class............../
    
    textJson= extractorOffice.ReadText(docInputPath,outputDocxTextFilePth)
    print('textList:',textJson)
    textList=list()
    textListChange=list()
    textList=generalFunctions.ConvertJsonToString(textJson)
    for text in textList:
        textListChange.append('a')
    textJsonChange=generalFunctions.ConvertStringToJson(textListChange)
    print ('zipfolder: ', extractorOffice.GetZipFolder())
    extractorOffice.WriteText(extractorOffice.GetZipFolder(),textJsonChange)
    
if __name__=='__main__':
    main()
