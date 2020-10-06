#将PDF文件夹里的所有pdf添加签名图片
import os
import PyPDF2

SignPDF = PyPDF2.PdfFileReader('.\\PDF\\ZJSign\\Sign.pdf')   # 读取签名pdf内容

def add_sign(Sign_pdf,page_pdf):
    """
    将水印pdf与pdf的一页进行合并
    :param Sign_pdf:
    :param page_pdf:
    :return:
    """
    page_pdf.mergePage(Sign_pdf.getPage(0))
    return page_pdf

for root, dirs, files in os.walk('.\\PDF', topdown=False):
    for name in files:
        address = os.path.join(root, name)
        print(address)
        pdfReader = PyPDF2.PdfFileReader(address) 
        # 遍历pdf的每一页,添加水印,该功能尚未实现
        for page in range(pdfReader.numPages):            
            page_pdf = add_sign(SignPDF, pdfReader.getPage(page))
            
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(page_pdf)

        with open(address, 'wb') as target_file:
            pdfWriter.write(target_file)

