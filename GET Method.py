from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/health', methods=['get'])
def health():
    data = {
        "status" : "working"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
