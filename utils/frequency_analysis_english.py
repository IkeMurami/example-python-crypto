"""
Частотный анализ для аглийского алфавита
"""


def PrintEnglishFreq():
    mas = [12.7,9.06,8.17,7.51,6.97,6.75,6.33,6.09,5.99,4.25,4.03,2.78,2.76,2.41,2.36,2.23,2.02,1.97,1.93,1.49,0.98,0.77,0.15,0.15,0.1,0.05]
    alph = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'
    for i in range(0, 26):
        print(alph[i] + ' - ' + str(mas[i]))


def Print(dic):
    keys = dic.keys()
    keys = sorted(keys)
    chrs = ''
    val = ''
    for ch in keys:
        print(ch + ' - ' + "%.2f" % (dic[ch]*100))
        #chrs += (ch + '\t')
        #val += (str(dic[ch]) + '\t')
    #print(dic)
    #print(chrs)
    #print(val)


def Calc(message):
    d = dict()
    for ch in message:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1
    keys = d.keys()
    for ch in keys:
        d[ch] = d[ch] / len(message)
    return d


PrintEnglishFreq()
#Print(Calc('TNFOS FOZSW PZLOC GQAOZ WAGQR PJZPN ABCZP QDOGR AMTHA RAXTB AGZJO GMTHA RAVAP ZW'.replace(' ','')))