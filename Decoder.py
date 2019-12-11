import Decoderjson

def decode(filename):
    f = open(filename, 'r')
    dlstring = f.read()
    f.close()

    # clean this up
    dlstringarray = dlstring.split('\n')
    dlstringarray = dlstringarray[1:]
    dlstringarray = [line.strip() for line in dlstringarray]

    # remove 'ANSI' from first element (It's a fixed header)
    dlstringarray[0] = dlstringarray[0][5:]
    metadata = dlstringarray[0]
  
    dlstringarray.remove(metadata)
    
  
    indexOfInfo = []
    for x in Decoderjson.driverLicenseFields :
        indexOfInfo.append(metadata.find(x['abbreviation']))

    indexOfInfo = list(filter((-1).__ne__,indexOfInfo))
    indexOfInfo.sort()
   
    for index in range(len(indexOfInfo)-1):
        spl = slice(indexOfInfo[index], indexOfInfo[index+1])
        meta = metadata[spl]
        print(meta)
