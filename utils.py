def calculate_tax(salary, tax_brackets):
    total_tax = 0.0
    tax_breakdown = []
    remaining_salary = salary

    for bracket in tax_brackets:
        bracket_min = bracket.get("min")
        # If 'max' is not provided, consider it as infinity
        bracket_max = bracket.get("max", float("inf"))
        rate = bracket.get("rate", 0)

        # Calculate taxable income for the bracket if salary exceeds bracket_min
        if salary > bracket_min:
            taxable_income = min(remaining_salary, bracket_max - bracket_min)
            tax_for_bracket = taxable_income * rate
            tax_breakdown.append({
                "min": bracket_min,
                "max": bracket.get("max"),
                "rate": rate,
                "tax": round(tax_for_bracket, 2)
            })
            total_tax += tax_for_bracket
            remaining_salary -= taxable_income

        if remaining_salary <= 0:
            break

    effective_rate = round(total_tax / salary, 4) if salary else 0

    return {
        "total_tax": round(total_tax, 2),
        "effective_rate": effective_rate,
        "tax_breakdown": tax_breakdown
    }
