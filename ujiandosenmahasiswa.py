import pymongo
import json
import csv

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

newdb = mydb["kampus"]
newcol = newdb["dosen"]
datadosen =  []

for i in newcol.find():
    d = {
        'asal' : i['asal'],
        'nama' : i['nama'],
        'status1' : i['status1'],
        'usia' : i['usia']
    }
    datadosen.append(d)

file = open('dosen.json', 'w')
dataJson = json.dumps(datadosen)

file.write(dataJson)
file.close()

url= 'monggodb://localhost:27017'
mydb = pymongo.MongoClient()

newdb = mydb["kampus"]
newcol = newdb["mahasiswa"]
datamhs =  []

for i in newcol.find():
    d = {
        'asal' : i['asal'],
        'nama' : i['nama'],
        'status1' : i['status1'],
        'usia' : i['usia']
    }
    datamhs.append(d)

file = open('mahasiswa.json', 'w')
dataJson = json.dumps(datamhs)

file.write(dataJson)
file.close()

dataCSVdosen = json.dumps(datamhs)
dataCSVdosen = json.dumps(datadosen)

with open('dosen.csv','w',newline='') as dosen:
    createcsv = csv.DictWriter(dosen,fieldnames=['asal','nama','status1','usia'])
    # file.write(dataCSV)
    createcsv.writeheader()
    createcsv.writerows(datadosen)


with open('mahasiswa.csv','w',newline='') as mahasiswa:
    createcsv = csv.DictWriter(mahasiswa,fieldnames=['asal','nama','status1','usia'])
    # file.write(dataCSV)
    createcsv.writeheader()
    createcsv.writerows(datamhs)


import pandas as pd 
df1 = pd.read_csv('dosen.csv')
df2 = pd.read_csv('mahasiswa.csv')

print(df1)
print(df2)

import matplotlib.pyplot as plt
import csv

# x = []
# y = []

# with open('mahasiswa.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(row[1])
#         y.append(row[3])

# with open('dosen.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(row[1])
#         y.append(row[3])

# x.remove(x[0])
# y.remove(y[0])
# x.remove(x[3])
# y.remove(y[3])


# print(x)
# print(y)
# plt.bar(x,y, label='Loaded from file!')
# plt.xlabel('nama')
# plt.ylabel('usia')
# plt.title('Data usia mahasiswa dan dosen')
# plt.grid(True , color='cyan', linestyle='--')
# plt.legend()
# plt.show()

dosen = pd.read_csv('dosen.csv')
mahasiswa = pd.read_csv('mahasiswa.csv')

#plot berdasarkan usia 
plt.bar(dosen['nama'],dosen['usia'],color = 'blue')
plt.bar(mahasiswa['nama'],mahasiswa['usia'],color = 'orange')
plt.grid(True)
plt.legend(['Dosen','Mahasiswa'])
plt.title('Usia Warga Kampus')
plt.show()

