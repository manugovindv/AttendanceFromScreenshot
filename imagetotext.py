import pytesseract
import pandas as pd
import requests
      
def img2str():
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract'
    txt=pytesseract.image_to_string(r'D:\Programs\Python\attendance\list2.png')
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
        if i.startswith("18"):
            res=res+" "+i
    for i in txt:
        i=i.upper()
        if i.startswith("19"):
            res=res+" "+i  
    res=res.split()
    res=sorted(res,key = lambda x:int(x[-3:]))
    return res    
def tocsv():
    txt=img2str()
    lis=sorting(txt)
    df = pd.DataFrame(lis)
    df.to_csv('test2.csv', index=False, header=False)  
def push(vals):
        url = "https://script.google.com/macros/s/AKfycbyr3kyl7wcTQYennD2P_odF0WLM8DzLQ5kfEAcFQrIYgzW4HJs/exec"
        parameters = {"id":"Sheet1"}
        paramlist=["turtle_x","turtle_y","turtle_theta"]
        
        vals=tuple(map(int, vals.strip("()").split(", ")))
        print(vals)
        paramlist=["turtle_x","turtle_y","turtle_theta"]
        for val,i in zip(vals,paramlist):
            parameters[i] = val
            parameters1[i] = val
        
        print(parameters)
        response = requests.get(url, params=parameters)
        print(response.content)

def main():
    tocsv()

if __name__ == '__main__':
    try:
        main()
    except :
        pass