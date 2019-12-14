import Decoderjson
import openpyxl
import xlwings as xw





def decode(filename):
    firstName = ""
    lastName = ""
    DL = ""
    birth = ""
    exp = ""
    address = ""
    city = ""
    state = ""
    zipCode = ""

    f = open(filename, 'r')
    dlstring = f.read()
    f.close()

  
    dlstringarray = dlstring.split('\n')
    dlstringarray = dlstringarray[1:]
    metadata = dlstringarray[0][5:]


 
    indexOfInfo = []
    for x in Decoderjson.driverLicenseFields : 
        num = metadata.find(x['abbreviation'])
        if num != -1 :
            indexOfInfo.append(num)
        # print(metadata[num:])  // use for debugging
        # print(num)    // use for debugging
    
    # print(indexOfInfo) // use for debugging
    

    indexOfInfo = list(filter((-1).__ne__,indexOfInfo))
    indexOfInfo.sort()

    res = []
    for index in range(len(indexOfInfo)-1):
        spl = slice(indexOfInfo[index], indexOfInfo[index+1])
        meta = metadata[spl]
        res.append(meta)
    

    for index,word in enumerate(res): 
        if word == "D":
            previousWord = res[index-1] 
            previousWord = previousWord + word
            res[index-1] = previousWord

    
    for x in range(len(res)) :
        if res[x].find("DAC") != -1 :
            firstName = res[x][3:]
            print(firstName)
        elif res[x].find("DCT") != -1 :
            firstName = res[x][3:]
            print(firstName)
        if res[x].find("DCS") != -1 :
            lastName = res[x][3:]
            print(lastName)
        if res[x].find("DAQ") != -1 :
            DL = res[x][3:]
            print(DL)
        if res[x].find("DBB") != -1 :
            birth= res[x][3:]
            print(birth)
        if res[x].find("DBA") != -1 :
            exp = res[x][3:]
            print(exp)
        if res[x].find("DAG") != -1 :
            address = res[x][3:]
            print(address)
        if res[x].find("DAI") != -1 :
            city = res[x][3:]
            print(city)
        if res[x].find("DAJ") != -1 :
            state = res[x][3:]
            print(state)
        if res[x].find("DAK") != -1 :
            zipCode = res[x][3:][:5]
            print(zipCode)

    enteringDataToSheet(firstName,lastName,DL,exp,birth,address,city,state,zipCode)

def enteringDataToSheet(firstName,lastName,DL,exp,birth,address,city,state,zipCode) :
    
    wb = xw.Book("Ninja Pitsburgh.xlsx")
    sheet = wb.sheets["Ninja"]
    length = sheet.range('A1').current_region.end('down').row + 1
    print(length)
    sheet.range('A'+str(length)).value = firstName
    sheet.range('B'+str(length)).value = lastName
    sheet.range('C'+str(length)).value = DL
    sheet.range('D'+str(length)).value = exp
    sheet.range('E'+str(length)).value = birth

    sheet.range('F'+str(length)).value = address
    sheet.range('G'+str(length)).value = city
    sheet.range('H'+str(length)).value = state
    sheet.range('I'+str(length)).value = zipCode

    # wb.save("Ninja Pitsburgh.xlsx")
    # sheets.
