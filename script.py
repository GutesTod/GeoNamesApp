import json
from flask import Flask, request
from core import parse_data, open_txt

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/city/<int:geonameid>', methods = ['GET'])
def get_city(geonameid):
    try:
        return json.dumps(data[f'{geonameid}'], ensure_ascii=False, indent=4).encode('utf8')
    except KeyError:
        return json.dumps({"error": "CodeNameId doesn't exist!"}, ensure_ascii=False).encode('utf8')
    
@app.route('/api/cities', methods=['GET'])
def get_cities():
    start = (request.args.get('page', default=1, type=int) - 1) * request.args.get('per_page', default=10, type=int)
    end = start + request.args.get('per_page', default=10, type=int)
    cities = []
    for key in range(start, end + 1):
        city = data[f'{data_id[key]}']
        cities.append(city)
    return json.dumps(cities, ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
    txt_data = open_txt()
    data, data_id = parse_data(txt_data)
    app.run(host='127.0.0.1', port=8000, debug=True)