from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/insurance', methods=['GET'])
def get_insurance():
    return jsonify({'message': 'List of insurances'})

if __name__ == '__main__':
    app.run(debug=True)

# http://localhost:5000/api/insurance - GET request 
