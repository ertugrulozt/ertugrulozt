import os
import openpyxl
import datetime


path = "//10.1.232.58/kurumsal/TEKLIF/IRAQ"

def teklifler():
    files = []
    x = []
    y= []
    z= []
    for file in os.listdir(path):
        #print(file) #Excel Ana Başlık

        newpath= path + '/' + file


        for newfile in os.listdir(newpath):
            #print(newfile) #Excel'de Alt başlık-1

            if ('PROPOSAL' or 'PROPOSALS') in newfile:
                x.append(newfile)
                nnpath = newpath + '/' + newfile
                if os.path.isdir(nnpath) == True:
                    for nnfile in os.listdir(nnpath):
                        if ('ELECTRICAL' or 'ELECTRIC') in nnfile:
                            y.append(nnfile)
                            nnnpath = nnpath + '/' + nnfile
                            if os.path.isdir(nnnpath) == True:
                                for nnnfile in os.listdir(nnnpath):
                                    z.append(file + ':' + nnnfile)
    print(*z, sep='\n')



teklifler()