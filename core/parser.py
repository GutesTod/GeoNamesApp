import os

PARSER_DIR = os.path.dirname(__file__)
txt_file = PARSER_DIR + '/RU.txt'
with open(txt_file, encoding='utf-8') as f:
    mydata = f.read().splitlines()

data = {}

for datatmp in mydata:
    tmp = datatmp.split('\t')
    data[tmp[0]] = {
        'name' : tmp[1],
        'asciiname' : tmp[2],
        'alternatenames' : tmp[3],
        'latitude' : tmp[4],
        'longitude' : tmp[5],
        'feature class' : tmp[6],
        'country code' : tmp[7],
        'cc2' : tmp[8],
        'admin1 code' : tmp[9],
        'admin2 code' : tmp[10],
        'admin3 code' : tmp[11],
        'admin4 code' : tmp[12],
        'population' : tmp[13],
        'elevation' : tmp[14],
        'dem' : tmp[15],
        'timezone' : tmp[16],
        'modification date' : tmp[17]
    }