from Crypto.PublicKey import RSA
def GetRSAParams(nameFile):
    f = open(nameFile, 'r')
    r = RSA.importKey(f.read())
    f.close()
    return r.key

r = GetRSAParams('keyRSA.pem')
r = GetRSAParams('C:\\Users\Eska\Downloads\ctftask\HakerU\Task_2\key.pub')

print(r)