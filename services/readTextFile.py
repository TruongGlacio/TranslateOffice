import DocxExtractor
import sys
sys.path.insert(0, '../server/')
import util
import GeneralFuntions
import ExTractorOffice
generalFunctions = GeneralFuntions.General()

def main():
    Input = (sys.argv[1])
    Output = (sys.argv[2])
    extractorOffice = ExTractorOffice.ExtractorOffice()
    utilPack=util.utils();
    OutputTextFilePth =Output#'../DocxText.txt'
    InputPath = Input #'/home/vuhoangba/Desktop/testt.docx'
    # /..........test for docx class............../
    textListOutput = extractorOffice.ReadText(InputPath, OutputTextFilePth)
    # value return is a list include : textListOutput=[outputTextFile,Count, ZipFolder, FILE_EXTENTION]
    
    print('textList:', textListOutput)
    translatedTexFile=utilPack.TranslateText(textListOutput[0])
    textListOutput[0]=translatedTexFile
    officeTargetPath=extractorOffice.WriteText(textListOutput)
    return officeTargetPath
if __name__ == "__main__":
    main();
