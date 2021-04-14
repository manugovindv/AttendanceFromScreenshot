import pytesseract
import requests
from googlesheet import markatt
import json

pathfile = json.loads("paths.json")

def img2str(imagepath): #change path to location of tesseract and file to location of ss
    
    pytesseract.pytesseract.tesseract_cmd = pathfile['tsrctPath']
    txt=pytesseract.image_to_string(imagepath)
    return txt

def cleaning(txt):
    txt=txt.replace("("," ")
    txt=txt.replace(")"," ")
    txt=txt.replace("["," ")
    txt=txt.replace("]"," ")
    txt=txt.replace("-"," ")
    txt=txt.replace("_"," ")
    txt=txt.replace("/"," ")
    txt=txt.split()
    res=[]
    for i in txt:
        i=i.upper()
        if i.startswith("1"):
            res.append(i[:10])
    
    return res    

def tocsv(cltxt):
    import pandas as pd
    lis=sorted(cltxt,key = lambda x:int(x[-3:]))  #sorting the cleaned list
    df = pd.DataFrame(lis)
    df.to_csv('test4.csv', index=False, header=False)  

def main():
    #todate = "11/12/2020"   #change accordingly,maintain dd/mm/yyyy format
    docname = pathfile['docname']
    imagepath = pathfile['imgPath']
    txt = img2str(imagepath)
    cltxt = cleaning(txt)
    #tocsv(cltxt) #uncomment only if a csv is required 

    markatt(cltxt,docname)  #if {todate} is not passed as argument,it defaults to date of the same day
      
if __name__ == '__main__':
    main()
    
