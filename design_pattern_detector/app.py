from flask import Flask, render_template, request, jsonify
from pattern_detector import detect_design_patterns

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-patterns', methods=['POST'])
def detect_patterns():
    data = request.get_json()
    code = data.get('code', '')

    # Detect patterns in the provided code
    detected_patterns = detect_design_patterns(code)

    return jsonify({'patterns': detected_patterns})

if __name__ == '__main__':
    app.run(debug=True)
