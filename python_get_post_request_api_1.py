
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/insurance', methods=['GET', 'POST'])
def insurance():
    if request.method == 'GET':
        # Parse query parameters
        insurance_type = request.args.get('type', 'all')
        
        # Parse headers
        api_key = request.headers.get('X-API-Key')
        
        if not api_key:
            return jsonify({'error': 'API key is required'}), 401
        
        return jsonify({
            'message': f'List of {insurance_type} insurances',
            'api_key_used': api_key
        })
    
    elif request.method == 'POST':
        # Parse JSON payload
        data = request.json
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Process the data (in this example, we're just echoing it back)
        return jsonify({
            'message': 'Insurance data received',
            'data': data
        })

if __name__ == '__main__':
    app.run(debug=True)

# you can use curl to make GET requests to the API as below:
# curl "http://localhost:5000/api/insurance?type=health" -H "X-API-Key: your_api_key_here"

#Curl POST request, sometimes on windows the double quotes in the json payload need escape character \"
#curl -X POST "http://localhost:5000/api/insurance" -H "Content-Type: application/json" -d "{\"name\": \"Health Insurance\", \"coverage\": 1000000}"
#or use --data-raw option
#curl -X POST "http://localhost:5000/api/insurance" -H "Content-Type: application/json" --data-raw '{"name": "Health Insurance", "coverage": 1000000}'

#curl -X POST "http://localhost:5000/api/insurance" -H "Content-Type: application/json" -d @payload.json