import json
import os
import zipfile
import sys
import shutil
try:
    from xml.etree.cElementTree import XML
    import xml.etree.cElementTree as ET 
except ImportError:
    from xml.etree.ElementTree import XML

OFFICE_EXTENSION=['.doc','.docx','.ppt','.odf','.pptx','.xls','.xlsx']
EXCEL_SubFolder=['/xl/worksheets','/xl/drawings','/xl/charts' ]
WORD_SubForder=['/word/document.xml','/word/embeddings']
PPT_SubFolder=['/xl/sharedStrings.xml']
class General:
    def ConvertStringToJson(self,intputStringList):
        jsonArrayString=json.dumps(intputStringList)
        print (jsonArrayString)
        return jsonArrayString
    
    def ConvertJsonToString(self,inputJsonArray):      
        textList=json.loads(inputJsonArray)
        return textList
    
    def ReadTextXmlFile(self,inputXmlFilePath,NAMESPACE,PARA,TEXT):
        
        OFFICE_PARA=NAMESPACE+PARA
        OFFICE_TEXT=NAMESPACE+TEXT
        tree =ET.parse(inputXmlFilePath)
        paragraphs=list()
        for paragraph in tree.getiterator(OFFICE_PARA):
            for node in paragraph.getiterator(OFFICE_TEXT):
                if node.text: 
                    print(node.text)                
                    paragraphs.append(node.text)   
        print ('paragraphs: ',paragraphs)        
        return paragraphs
    
    def WriteTextXmlFile(self, inputXmlFilePath,NAMESPACE,PARA,TEXT,inputTextList,count):
        OFFICE_PARA=NAMESPACE+PARA
        OFFICE_TEXT=NAMESPACE+TEXT        
        tree =ET.parse(inputXmlFilePath)
        for paragraph in tree.getiterator(OFFICE_PARA):
            for node in paragraph.getiterator(OFFICE_TEXT):
                if node.text: 
                    node.text=inputTextList[count]
                    print(node.text) 
                    count=count+1
        tree.write(inputXmlFilePath)
        return count
    def WriteTextFile(self, inputString, textFilePath):    
        text_file = open(textFilePath, "w")
        text_file.write(inputString)
        text_file.close()  
        
    def extraZipfile(self,officeFileName):
        print('extraZipfile Function')    
        print('officeFileName:',officeFileName)            
        zipFileName=General.ReNameOfficeToZip(self, officeFileName)
        if(zipFileName==None):
            return None
        print ('zipFileName=',zipFileName)
        filename=os.path.splitext(os.path.basename(zipFileName))[0]
        extensionfile=os.path.splitext(os.path.basename(zipFileName))[1]
        if(extensionfile=='.xlsx'):
            folderpath=os.path.dirname(zipFileName)
        else:
            folderpath=os.path.dirname(zipFileName)+'/'+filename
        print('folder out put file is :%s',folderpath);      
        print('file name out put file is :%s',filename);          
        try:
            print('try extra zip file ' )
            with zipfile.ZipFile(zipFileName,"r") as zip_ref:
                zip_ref.extractall(folderpath);
                return folderpath
        except:
            print('Error when extra file');       
            return None
    
    def ReNameOfficeToZip(self,officeFilePath):
        print('ReNameOfficeToZip Function')            
        # check file exit 
        if(os.path.isfile(officeFilePath)):
            folderPath=os.path.dirname(officeFilePath)        
            fileName=os.path.splitext(os.path.basename(officeFilePath))[0]
            extensionFile=os.path.splitext(os.path.basename(officeFilePath))[1]
            print('extension file is :',extensionFile);                  
            newfilePath= folderPath+ '/'+ fileName+'1'+extensionFile 
            zipFilePath= folderPath+ '/'+ fileName+'1.zip'
            print('old path file is:',officeFilePath)
            print('new path file is:',newfilePath);                          
            for office_extension in OFFICE_EXTENSION:
                print('extensionFile:',extensionFile, 'office_extension',office_extension)
                
                if(office_extension==extensionFile):
                    # copy to new file
                    shutil.copyfile(officeFilePath, newfilePath)   
                    # rename file to zip
                    print('new path file is:',newfilePath);  
                    try:
                        shutil.move(newfilePath, zipFilePath);
                    except: 
                        print('Error rename File');                        
                    print('out put file is :%s',zipFilePath);
                    return zipFilePath;               
                else:
                    print("Finally finished!")
        else:
            print('No such file or directory')
            return None
        
    def CompressOfficeFolder(self,folders):    
        print('CompressOfficeFolder Function')   
        parentPath=os.path.abspath(os.path.join(folders, os.pardir))   
        baseFolderName=os.path.basename(folders)    
        print('folder path: ',folders)      
        print('baseNameFolder:',baseFolderName)  
        zip_filename=parentPath+ '/'+ baseFolderName+'.zip'
        # for folder in folders:
        #General.DeleteFolder(self, folders)
        try:
            zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)            
            for dirpath, dirnames, filenames in os.walk(folders):
                #if(dirpath!=folders):
                print('dirpath : ',dirpath)                
                for filename in filenames:
                    print('filename=',filename)                        
                    zip_file.write(os.path.join(dirpath, filename), os.path.relpath(os.path.join(dirpath, filename),folders))
            zip_file.close() 
            General.DeleteFolder(self,folders)                                        
            return zip_filename    
        except:
            print ('error while compress folder, go exit')
            return None
    def DeleteFolder(self,folder):
        # remove folder after compress                                
        try:
            for root, dirs, files in os.walk(folder, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))  
            os.rmdir(folder)
            return True
        except:
            print('Cant delete folder, go exit')   
            return False
            
    def GetPathExcelXml(self,zipFolderExcelPath):
        listFilePath=list()
        print('zipFolderExcelPath is :',zipFolderExcelPath)        
        for subfolder in EXCEL_SubFolder:
            subfolderPath= zipFolderExcelPath+ subfolder
            listfilePathInSubfolder= General.GetAllFilePathInFolder(self,subfolderPath)
            for filePath in listfilePathInSubfolder:
                listFilePath.append(filePath)
                print('xml file path:'+ filePath )
        return listFilePath
        
    def GetPathWordXml(self,zipFolderWordPath):
        listFilePath=list()
        print('zipFolderWordPath is :',zipFolderWordPath)        
        for subfolder in WORD_SubForder:
            subfolderPath= zipFolderWordPath+ subfolder
            listfilePathInSubfolder= General.GetAllFilePathInFolder(self,subfolderPath)
            for filePath in listfilePathInSubfolder:
                listFilePath.append(filePath)
                print('xml file path:'+ filePath )
        return listFilePath
        
    def GetPathPPTXml(self,zipFolderPPTPath):
        listFilePath=list()
        print('zipFolderPPTPath is :',zipFolderPPTPath)        
        for subfolder in PPT_SubFolder:
            subfolderPath= zipFolderPPTPath+ subfolder
            listfilePathInSubfolder= General.GetAllFilePathInFolder(self,subfolderPath)
            for filePath in listfilePathInSubfolder:
                listFilePath.append(filePath)
                print('xml file path:'+ filePath )
        return listFilePath
    
    def GetAllFilePathInFolder(self, folderPath):
        xmlType= '.xml'
        listPath=list()
        if(os.path.exists(folderPath)):
            if(os.path.isdir(folderPath)):
                listpath=os.listdir(folderPath)
                for path in listpath:
                    extensionFile=os.path.splitext(os.path.basename(path))[1]
                    if(extensionFile==xmlType):
                        listPath.append(path)
                    else:
                        print('file not xml file')
            else:
                listPath.append(folderPath)
                    
        return listPath
                
                
            
        