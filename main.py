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
    
    outputExcelTextFilePath='../excelText.txt'
    outputPPTTextFilePth='../PPTText.txt'
    outputDocxTextFilePth='../DocxText.txt'
    docInputPath='/home/truongglacio/Projects/TransLate/TranslateOffice/Bài tập lớn môn hệ thống viễn thông.docx'
    pptInputPath='/media/glacio/Data/Translate/Project/Bổ-sung_Quy-chế-lương_2018.pptx'
    excelInputPath='/media/glacio/Data/Translate/Project/test.xlsx'
    
    # /..........test for docx class............../
    textJson=doc.ReadWordText(docInputPath,outputDocxTextFilePth)
    print('textList:',textJson )
    textList=list()
    textListChange=list()
    textList=generalFunctions.ConvertJsonToString(textJson)
    for text in textList:
        textListChange.append('abcd')
    textJsonChange=generalFunctions.ConvertStringToJson(textListChange)
    doc.WriteTextFromJson(doc.GetZipFolder(),textJsonChange)
    
    #extractorOffice.ReadText(docInputPath)
    #/...........test for excel class............../
    #excelListJson=excel.ExcelReadText(excelInputPath,outputExcelTextFilePath)
    #excelListText=generalFunctions.ConvertJsonToString(excelListJson)
    #for text in excelListText:
     #   excelListChange.append('abcbd')
        
    #rint('excelListChange',excelListChange)    
    #excelListJsonChange=generalFunctions.ConvertStringToJson(excelListChange)
    #print('excelListJsonChange',excelListJsonChange)
    #excel.ExcelWriteText(excelInputPath,excelListJsonChange)
    
    #/..........test for ppt class............./
    #PPtTestListNormal=ppt.ReadTextTable(pptInputPath)
    #ppttextListChange=list()
    #for text in PPtTestListNormal:
     #   ppttextListChange.append('abcbd')
    #ppt.WriteTextTable(pptInputPath, ppttextListChange)
    
    
if __name__=='__main__':
    main()
