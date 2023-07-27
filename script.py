import json
from flask import Flask, jsonify
from core import data

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/cities/<int:geonameid>', methods = ['GET'])
def get_cities(geonameid):
    try:
        return json.dumps(data[f'{geonameid}'], ensure_ascii=False, indent=4).encode('utf8')
    except KeyError:
        return json.dumps({"error": "CodeNameId doesn't exist!"}, ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)