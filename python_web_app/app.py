from flask import Flask, send_from_directory
from api.api import api_bp

app = Flask(__name__, static_folder='static')

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
