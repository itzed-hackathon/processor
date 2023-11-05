import json
from flask import Flask
from flask_cors import CORS, cross_origin

def main():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/eye')
    @cross_origin()
    def eye():
        print(request.get_json())

        return json.dumps({
            'cats': cats,
        })

    app.run()

if __name__ == '__main__':
    main()
