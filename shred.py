from random import randint

#    **TARGET FILE**:       C:\Users\foots\python\Dependencies\targetfolder\targetfile.txt

def main():

    works = False
    #accept user input of target path (fileName) and times to overwrite (times)
    while works == False:
        try:
            print("Enter target path: ")    
            path = input()
            f = open(path, 'r')
            f.close()
        except:
            print("Invalid file path!")
        else:
            works = True 

    #pass user inputs into shred(), returns new length of file
    length = shred(path)

    #output DONE message and new file length to user
    print("File overwritten! New file length: " + str(length))
    
def shred(fileName):
    for i in range(0,32):      #overwrites each subsequent iteration of the file
        num = fileShredder(fileName)
    return num  #method returns number of characters of resulting file




def fileShredder(fileName): #overwrites file 
    text = ''
    rando = 0

    #read file first to verify length in characters
    try:
        f = open(fileName, 'r') #open target file in read-only
        text = f.read()         #capture file text
        length = len(text)      #capture length of file in characters
        text = str('')          #wipe text var to whitespace

        for i in range(length): #concat nums into string to overwrite file
            rando = randint(0, 10) 
            text = text + str(rando)

    #close filestream
    finally: 
        f.close()

    #overwrite file with new text of equal length
    try:
        f = open(fileName, 'w')
        f.truncate()    #wipe previous data
        num = f.write(text) #overwrite with new string of num

    #close filestream again
    finally:     
        f.close()

    #returns new length
    return num

        

if __name__ == "__main__":
    main()
