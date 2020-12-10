import pytesseract
import requests
from googlesheet import markatt
      
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
    txt=txt.replace("/"," ")
    txt=txt.split()
    res=""
    for i in txt:
        i=i.upper()
        if i.startswith("1"):
            res=res+" "+i
    res=res.split()
    res=sorted(res,key = lambda x:int(x[-3:]))
    return res    

def tocsv(lis):
    import pandas as pd
    df = pd.DataFrame(lis)
    df.to_csv('test4.csv', index=False, header=False)  

def main():
    todate = "11/12/2020"   #change accordingly,maintain dd/mm/yyyy format
    docname = "MMM attendance"
    txt=img2str()
    lis=sorting(txt)
    #tocsv(lis) #uncomment only if a csv is required 
    markatt(lis,todate,docname)
if __name__ == '__main__':
    main()
    