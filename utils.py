from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def calculate_tax(salary, tax_brackets):
    total_tax = 0.0
    tax_breakdown = []
    remaining_salary = salary

    for bracket in tax_brackets:
        bracket_min = bracket.get("min")
        bracket_max = bracket.get("max", float("inf"))
        rate = bracket.get("rate", 0)

        if salary > bracket_min:
            taxable_income = min(remaining_salary, bracket_max - bracket_min)
            tax_for_bracket = taxable_income * rate
            tax_breakdown.append({
                "min": bracket_min,
                "max": bracket.get("max"),
                "rate": rate,
                "tax": round(tax_for_bracket, 4)
            })
            total_tax += tax_for_bracket
            remaining_salary -= taxable_income

        if remaining_salary <= 0:
            break

    effective_rate = round(total_tax / salary, 4) if salary else 0

    print(total_tax)
    return {
        "total_tax": round(total_tax, 2),
        "effective_rate": effective_rate,
        "tax_breakdown": tax_breakdown
    }

def get_retry_session():
    session = Session()
    retries = Retry(
        total=2,
        backoff_factor=0.3,
        status_forcelist=[500],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    return session