import hashlib

def crackHash(inputpass):
    try:
        passFile = open("wordlist.txt","r")
    except:
        print("Could not find the file ")

    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest==inputpass:
            print("password found:" +password)

if __name__ == '__main__':
    crackHash("e10adc3949ba59abbe56e057f20f883e")

