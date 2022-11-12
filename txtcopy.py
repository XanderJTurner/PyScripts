#read in two .txt file paths, copy contents of file A to contents of file B
#utilize hex editor for testing purposes
#do NOT depend on file extension; manually capture file signature

#COPY FILE: C:\Users\foots\python\Dependencies\targetfolder\quick_revive.txt
#TARGET FILE: C:\Users\foots\python\Dependencies\targetfolder\targetfile.txt


#read in/verify file paths as input, pass to copy function
def main():
    #accept and verify user input of target path1
    works = False
    while works == False:
        try:
            print("Enter path to copy: ")    
            path1 = str(input())
            f = open(path1, 'r')
            f.close()
        except:
            print("Invalid file path!")
        else:
            works = True

   
    #accept and verify user input of target path2
    works = False
    while works == False:
        try:
            print("Enter path to copy to: (WARNING! File will be overwritten!)")    
            path2 = str(input())
            f = open(path2, 'r')
            f.close()
        except:
            print("Invalid file path!")
        else:
            works = True

    #pass both paths into copy
    try:
        copy(path1, path2)
    except: 
        print("Unknown error occurred")
    else:
        print("Copy successful!")


#capture file contents and return as str
def readTxt(fileName):
    try:
        f = open(fileName, 'r')
        text = f.read()
        return str(text)
    finally:
        f.close()

#pass in two file paths, copy contents of path1 into path2
def copy(path1, path2):
    text = readTxt(path1)
    try:
        f = open(path2, 'r+')
        ret = f.truncate()
        f.write(text)
    finally:
        f.close()
        return ret
    



if __name__ == "__main__":
    main()