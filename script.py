import json
from flask import Flask, request
from core import parse_data, open_txt, generate_dict_city, main_data, timezone_data, parse_timezone
from core import transliterate

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/city/<int:geonameid>', methods = ['GET'])
def get_city(geonameid):
    try:
        return json.dumps(data[f'{geonameid}'], ensure_ascii=False, indent=4).encode('utf8')
    except KeyError:
        return json.dumps({"error": "CodeNameId doesn't exist!"}, ensure_ascii=False).encode('utf8'), 404
    
@app.route('/api/cities', methods=['GET'])
def get_cities():
    start = (request.args.get('page', default=1, type=int) - 1) * request.args.get('per_page', default=10, type=int)
    end = start + request.args.get('per_page', default=10, type=int)
    cities = []
    for key in range(start, end + 1):
        city = data[f'{data_id[key]}']
        cities.append(city)
    return json.dumps(cities, ensure_ascii=False).encode('utf8')

@app.route('/api/two-cities', methods=['GET'])
def get_cities_info():
    city1_name = transliterate(request.args.get('city1_name'))
    city2_name = transliterate(request.args.get('city2_name'))
    cities = [None, None]
    population_city1, population_city2 = -1, -1
    for geonameid, row in data.items():
        if row['asciiname'] == city1_name and population_city1 < int(row['population']):
            cities[0] = generate_dict_city(geonameid, row)
            population_city1 = int(row['population'])
        if row['asciiname'] == city2_name and population_city2 < int(row['population']):
            cities[1] = generate_dict_city(geonameid, row)
            population_city2 = int(row['population'])
    if cities[0] == None or cities[1] == None:
        return json.dumps({"error": "cities doesn't exist!"}, ensure_ascii=False).encode('utf8'), 404
    if cities[0]['latitude'] > cities[1]['latitude']:
        north_city_name = cities[0]['name']
    elif cities[0]['latitude'] < cities[1]['latitude']:
        north_city_name = cities[1]['name']
    else:
        north_city_name = 'Both cities are on the same latitude.'
    if cities[0]['timezone'] == cities[1]['timezone']:
        same_timezone = True
    else:
        # дополнительное задание с часами
        same_timezone = float(data_time[cities[0]['timezone']]) - float(data_time[cities[1]['timezone']]) 
    return json.dumps({
        'city1': cities[0],
        'city2': cities[1],
        'north_city_name': north_city_name,
        'same_timezone': same_timezone
    }, ensure_ascii=False).encode('utf8')

@app.route('/api/suggest-city', methods=['GET'])
def suggest_city():
    partial_name = transliterate(request.args.get('name'))
    suggestions = []
    if partial_name:
        for geonameid, row in data.items():
            if row['asciiname'].find(partial_name) == 0:
                suggestions.append(data[geonameid]['asciiname'])
            elif row['asciiname'].find(partial_name) != -1 and row['asciiname'][row['asciiname'].find(partial_name) - 1] == ' ':
                suggestions.append(data[geonameid]['asciiname'])
        return json.dumps({'suggestions': suggestions},  ensure_ascii=False).encode('utf8')
    else:
        return json.dumps({'error': 'Please provide a partial city name as input'})

if __name__ == '__main__':
    txtdata = open_txt(main_data)
    txttimezone = open_txt(timezone_data)
    data, data_id = parse_data(txtdata)
    data_time = parse_timezone(txttimezone)
    app.run(host="127.0.0.1", port=8000, debug=True)