from transformers import pipeline

class NlpModels():

    sum_pl = pipeline("summarization")
    ner_pl = pipeline("ner")
    textbody = ""
    min_length = 30
    max_length=200
    do_sample = False

    def __init__(self, textbody = "", max_length=200, min_length=30, do_sample=False):
        self.textbody = textbody
        self.max_length = max_length
        self.min_length = min_length
        self.do_sample = do_sample
    
    def getNers(self):
        return self.ner_pl(self.textbody)

    def getSummary(self):
        return self.sum_pl(self.textbody, self.max_length, self.min_length, self.do_sample)