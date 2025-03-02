from flask import Flask
from flask_smorest import Api
from resources.tax_calculator import blp as tax_calculator_blp

# Import your configuration if needed
# from config import Config

app = Flask(__name__)

# Example configuration (you can also load from config.py)
app.config["API_TITLE"] = "Tax Calculator API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


api.register_blueprint(tax_calculator_blp)

# if __name__ == "__main__":
#     app.run(debug=True)
