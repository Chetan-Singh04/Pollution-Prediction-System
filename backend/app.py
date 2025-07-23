from flask import Flask
from routes.air_routes import air_blueprint
from routes.water_routes import water_blueprint
from routes.noise_routes import noise_blueprint
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app)  # Enable cross-origin requests

# Register Blueprints
app.register_blueprint(air_blueprint, url_prefix='/air')
app.register_blueprint(water_blueprint, url_prefix='/water')
app.register_blueprint(noise_blueprint, url_prefix='/noise')

# @app.route("/")
# def home():
#     return "🌱 Pollution Prediction System API is Running!"


@app.route("/")
def home():
    return render_template('base.html')
@app.route("/air")
def air_page():
    return render_template('air.html')
@app.route("/water")
def water_pages():
    return render_template('water.html')
@app.route("/noise")
def noise_pages():
    return render_template('noise.html')
@app.route("/historical")
def historical_page():
    return render_template("historical.html")
@app.route("/map")
def map_page():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
