from helpers.pdfutil import PdfParser
from helpers.nlp import NlpModels

pdfparser = PdfParser('pdfsamples/Nidhi_resume_new.pdf')
pdfparser.loadPdf()
pdfparser.getAllPageContents()
pdfparser.unloadPdf()

nlpmodels = NlpModels(pdfparser.extractedText)
print(nlpmodels.getNers())
print(nlpmodels.getSummary())