from flask import Flask, jsonify, request
from flask_caching import Cache
from api.controller import Spike

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
spike = Spike()


@cache.cached(timeout=300)
@app.route('/', methods=['GET'])
def home():
    return 'API is online!'


@cache.cached(timeout=300)
@app.route('/matches/results', methods=['GET'])
def results():
    return jsonify(spike.get_match_results())


if __name__ == '__main__':
    app.run(debug=True)
