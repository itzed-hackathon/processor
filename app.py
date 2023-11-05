import json
from flask import Flask, request
from flask_cors import CORS, cross_origin

def main():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/eye', methods=["POST", "OPTIONS"])
    @cross_origin()
    def eye():
        print(request.get_json())

        return json.dumps({
            'cats': 6,
        })

    app.run()

if __name__ == '__main__':
    main()
