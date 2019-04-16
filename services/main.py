import sys
import GeneralFuntions
import ExTractorOffice
import PDFExtractor
generalFunctions=GeneralFuntions.General()

def main():

    extractorOffice=ExTractorOffice.ExtractorOffice()
    pdfExtrator=PDFExtractor.PDFExtractor()
    
    outputExcelTextFilePath='../excelText.txt'
    outputPPTTextFilePth='../PPTText.txt'
    outputDocxTextFilePth='../DocxText.txt'
    outputPdfTextFilePath='../PdfText.txt'
    outputTxtTextFilePath='../TxText.txt'
    pdfinputPath='/media/glacio/Data/Translate/Project/pdf/CV_Bui Xuan Truong.pdf'
    docInputPath='/media/glacio/Data/Translate/Project/クリップボードモード.docx'
    pptInputPath='/media/glacio/Data/Translate/Project/Truong_bui_XuanProfile.pptx'
    excelInputPath='/media/glacio/Data/Translate/Project/test.xlsx'
    txtfileInputPath='/media/glacio/Data/Translate/Project/translation-system/PdfText.txt'
    
    
    # /..........test for docx class............../
    #textListJson=list()
    
    #textListJson= extractorOffice.ReadText(docInputPath,outputDocxTextFilePth)
    #print('textList:',textListJson)
    
   
   # textJsonChange=generalFunctions.ConvertStringToJson(textListChange)
   # print ('zipfolder: ', extractorOffice.GetZipFolder())
    #extractorOffice.WriteText(textListJson)
    
    #read text from pdf 
    textList=extractorOffice.ReadText(pptInputPath,outputPPTTextFilePth)
    pptoutputfile=extractorOffice.WriteText(textList)
    print('textList',textList)
    
if __name__=='__main__':
    main()
