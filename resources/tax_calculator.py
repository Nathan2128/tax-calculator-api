from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import requests

from schemas.tax_schema import TaxCalculationInputSchema, TaxCalculationOutputSchema
from utils import calculate_tax, get_retry_session

blp = Blueprint("Tax Calculator", __name__, description="Calculate income tax based on annual salary and tax year")

@blp.route("/tax_calculator/")
class TaxCalculator(MethodView):
    @blp.arguments(TaxCalculationInputSchema, location="query")
    @blp.response(200, TaxCalculationOutputSchema)
    def get(self, args):
        salary = args["salary"]
        tax_year = args["tax_year"]

        if salary == 0:
            return {
                "total_tax": 0.0,
                "effective_rate": 0.0,
                "tax_breakdown": []
            }

        tax_api_url = f"http://localhost:5001/tax-calculator/tax-year/{tax_year}"
        session = get_retry_session()
        try:
            response = session.get(tax_api_url)
            response.raise_for_status()
            data = response.json()
            tax_brackets = data.get("tax_brackets", [])
        except requests.RequestException as e:
            abort(502, message=f"Error fetching tax brackets. Please try again later.")

        result = calculate_tax(salary, tax_brackets)

        return result
