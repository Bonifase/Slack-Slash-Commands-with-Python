from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello Slack!'

if __name__ == '__main__':
    app.run(debug=True)