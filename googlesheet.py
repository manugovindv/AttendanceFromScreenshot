import gspread
from gspread import models
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

today = date.today()





def markatt(checklist,docname: str="MMM attendance",todate: str=today.strftime("%d/%m/%Y")): #strftime to format dd/mm/yyyy

    #authentication
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("..\creds.json",scope)  #name the keyfile - "creds.json"
    client = gspread.authorize(creds)
    sheet = client.open(docname).worksheets()
    for j in sheet:  #loops through all sheets
        attli = []
          #worksheet("Section A")
        print(f'Checking sheet{j}')
        row = len(j.row_values(1))
        collen = len(j.col_values(2))
        j.update_cell(1,row+1,todate)  #updating header(date)
        rang = j.get(f'B2:B{collen}')  #collen is length of the column in each sheet
        rang = [i[0].strip().upper() for i in rang]  #converting from list of list to list of str
        
        checklist = list(map(lambda x:x.upper(),checklist)) #converting all reg.nos to uppercase
        
        for indx,reg in enumerate(rang):
            if reg in checklist:
                #print(f'{reg} is present today')
                attli.append(models.Cell(indx+2,row+1,'1'))
                #sheet.update_cell(indx+2,row+1,'1') #updates attendance in sheet
                checklist.remove(reg)  #removes the element from the list after checking
            else:
                attli.append(models.Cell(indx+2, row+1))
        j.update_cells(attli)

def main():
    #example list & date
    checklist = ['18GAEM9071', '18GAEM9037', '18GAEM9025', '18GAEM9031', '18GAEM9051', '18GAEM9054', '18GAEM9028', '18GAEM9004', '18GAEM9006', '18GAEM9009', '18GAEM9014', '18GAEM9015', '18GAEM9017', '18GAEM9021', '18GAEM9023', '18GAEM9024', '18GAEM9027', '18GAEM9029', '18GAEM9030', '18GAEM9039', '18GAEM9040', '18GAEM9046', '18GAEM9048', '18GAEM9052', '18GAEM9056', '18GAEM9058', '18GAEM9066', '18GAEM9070', '18GAEM9072', '18GAEM9073', '18GAEM9074', '18GAEM9075', '18GAEM9080', '18GAEM9082', '18GAEM9084', '18GAEM9086', '18GAEM9089', '18GAEM9090', '18GAEM9091', '18GAEM9095', '18GAEM9097', '18GAEM9035', '18GAEM9016', '19GAMEC107', '19GAMEC111', '19GAMEC104', '19GAMEC110', '19GAMEC112', '19GAMEC106']
    
    todate = "17/12/2020"

    markatt(checklist,todate)


if __name__=='__main__':
    main()
