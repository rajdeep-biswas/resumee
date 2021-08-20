import PyPDF2

class PdfParser():

    pdfFile = ""
    pdfFileObj = ""
    numPages = 0
    extractedText = ""

    def __init__(self, pdfFile):
        self.pdfFileObj = open(pdfFile, 'rb')

    def loadPdf(self):
        # except PdfReadWarning
        self.pdfFile = PyPDF2.PdfFileReader(self.pdfFileObj)
        self.numPages = self.pdfFile.numPages

    def unloadPdf(self):
        self.pdfFileObj.close()

    def getAllPageContents(self):
        for i in range(self.numPages):
            pageObj = self.pdfFile.getPage(i)
            self.extractedText += pageObj.extractText()