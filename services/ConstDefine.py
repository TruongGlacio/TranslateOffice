WORD_EXTENSION='.docx'
EXCEL_EXTENTION='.xlsx'
PPT_EXTENTION='.pptx'

WORD_NAMESPACE = ['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}']
WORD_PARA = ['p']
WORD_TEXT = ['t'] 

EXCEL_NAMESPACE = ['{http://schemas.openxmlformats.org/spreadsheetml/2006/main}','{http://schemas.openxmlformats.org/drawingml/2006/main}']
EXCEL_PARA = ['c','si','r']
EXCEL_TEXT = ['t','v']

PPT_NAMESPACE = ['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}']
PPT_PARA = ['p']
PPT_TEXT = ['t']


OFFICE_EXTENSION=['.doc','.docx','.ppt','.odf','.pptx','.xls','.xlsx']
EXCEL_SubFolder=['/xl/sharedStrings.xml','/xl/drawings','/xl/charts','/xl/diagrams/data.xml','/xl/comments.xml']
WORD_SubForder=['/word/embeddings','/word/diagrams/data.xml','/word/comments.xml' ,'/word/']
PPT_SubFolder=['/xl/sharedStrings.xml']