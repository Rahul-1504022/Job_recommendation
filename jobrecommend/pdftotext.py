import PyPDF2
import textract
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def cvrecommend(filename):
       # filename = 'my cv2.pdf'
        pdfFileObj = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count += 1
                text += pageObj.extractText()
                if text != "":
                        text = text
                #else:
                        #text = textract.process(fileurl,method='tesseract',language='eng')

        #print(text)
        tokens = word_tokenize(text)
        #print(tokens)
        punctuations = ['(',')',':',',',';','[',']']
        stop_words = stopwords.words('english')

        keyword = [word for word in tokens if not word in stop_words and not word in punctuations]
        s = ""
        for w in keyword:
                s = s + " " + w
        #print(keyword)
        #print(s)
        return s

#keyfeature = cvrecommend('cv/my cv2.pdf')
#print(keyfeature)