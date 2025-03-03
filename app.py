from flask import Flask
from flask_smorest import Api
from resources.tax_calculator import blp as tax_calculator_blp


app = Flask(__name__)


app.config["API_TITLE"] = "Tax Calculator API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


api.register_blueprint(tax_calculator_blp)

