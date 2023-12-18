from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = []

# Create a /script route
@app.route('/script')
# Define script() function
def script():
     # Return the static.js using send_from_directory() function
     return send_from_directory('static', 'script.js')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
