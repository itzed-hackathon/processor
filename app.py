import json
from flask import Flask

def main():
    app = Flask(__name__)

    @app.route('/eye')
    def eye():
        print(request.data)

        return json.dumps({
            'cats': cats,
        })

    app.run()

if __name__ == '__main__':
    main()
