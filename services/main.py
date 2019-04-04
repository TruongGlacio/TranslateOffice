import sys
import GeneralFuntions
import ExTractorOffice
generalFunctions=GeneralFuntions.General()

def main():

    extractorOffice=ExTractorOffice.ExtractorOffice()
    outputExcelTextFilePath='../excelText.txt'
    outputPPTTextFilePth='../PPTText.txt'
    outputDocxTextFilePth='../DocxText.txt'
    docInputPath='/media/glacio/Data/Translate/Project/translation-system/doc.docx'
    pptInputPath='/media/glacio/Data/Translate/Project/Bổ-sung_Quy-chế-lương_2018.pptx'
    excelInputPath='/media/glacio/Data/Translate/Project/test.xlsx'
    
    # /..........test for docx class............../
    textListJson=list()
    textListJson= extractorOffice.ReadText(docInputPath,outputDocxTextFilePth)
    print('textList:',textListJson)
   
   # textJsonChange=generalFunctions.ConvertStringToJson(textListChange)
   # print ('zipfolder: ', extractorOffice.GetZipFolder())
    #extractorOffice.WriteText(textListJson)
    
if __name__=='__main__':
    main()
