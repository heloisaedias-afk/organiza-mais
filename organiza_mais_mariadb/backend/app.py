from flask import Flask,jsonify
from flask_cors import CORS
from backend.routes.api import api
app=Flask(__name__)
CORS(app)
app.register_blueprint(api)
@app.get("/api/health")
def health(): return jsonify(status="ok",sistema="Organiza+")
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=True)
