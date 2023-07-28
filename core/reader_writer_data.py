import os

PARSER_DIR = os.path.dirname(__file__)
def open_txt():
    txt_file = PARSER_DIR + '/RU.txt'
    with open(txt_file, 'r', encoding='utf8') as f:
        mydata = f.read().splitlines()
    return mydata

def parse_data(datatxt):
    data = {}
    data_id = {}
    counter_id = 0
    for datatmp in datatxt:
        tmp = datatmp.split('\t')
        data[tmp[0]] = {
            'geocodeid' : tmp[0],
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
        data_id[counter_id] = tmp[0]
        counter_id += 1
    return data, data_id

def generate_dict_city(geonameid, row):
    city = {
        'geonameid': geonameid,
        'name': row['name'],
        'asciiname': row['asciiname'],
        'alternatenames': row['alternatenames'],
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'feature class': row['feature class'],
        'feature code': row['feature code'],
        'country code': row['country code'],
        'cc2': row['cc2'],
        'admin1 code': row['admin1 code'],
        'admin2 code': row['admin2 code'],
        'admin3 code': row['admin3 code'],
        'admin4 code': row['admin4 code'],
        'population': row['population'],
        'elevation': row['elevation'],
        'dem': row['dem'],
        'timezone': row['timezone'],
        'modification date': row['modification date']
    }
    return city