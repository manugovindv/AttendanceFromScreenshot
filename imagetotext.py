import pytesseract
import pandas as pd
import requests
      
def img2str(): #change path to location of tesseract and file to location of ss
    pytesseract.pytesseract.tesseract_cmd = r'path'
    txt=pytesseract.image_to_string(r'file')
    return txt

def sorting(txt):
    txt=txt.replace("("," ")
    txt=txt.replace(")"," ")
    txt=txt.replace("["," ")
    txt=txt.replace("]"," ")
    txt=txt.replace("-"," ")
    txt=txt.replace("_"," ")
    txt=txt.split()
    res=""
    for i in txt:
        i=i.upper()
        if i.startswith("1"):
            res=res+" "+i
    res=res.split()
    res=sorted(res,key = lambda x:int(x[-3:]))
    return res    
def tocsv():
    txt=img2str()
    lis=sorting(txt)
    df = pd.DataFrame(lis)
    df.to_csv('test2.csv', index=False, header=False)  

def main():
    tocsv()

if __name__ == '__main__':
    try:
        main()
    except :
        pass