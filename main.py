from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={
    r'/test/*':{'origins': '*'}
})

@app.route('/health', methods=['GET'])
def check_health():
    return {'msg': "hello"}, 200

@app.route('/test', methods=['GET'])
def check_test():
    return {'msg': "Test"}, 202

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0", threaded=True)