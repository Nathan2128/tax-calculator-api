import pytest
from utils import calculate_tax

def test_calculate_tax_entirely_in_first_bracket():
    salary = 40000
    tax_brackets = [
        {"min": 0, "max": 50197, "rate": 0.15},
        {"min": 50197, "max": 100392, "rate": 0.205},
        {"min": 100392, "max": 155625, "rate": 0.26},
        {"min": 155625, "max": 221708, "rate": 0.29},
        {"min": 221708, "rate": 0.33}
    ]
    result = calculate_tax(salary, tax_brackets)
    expected_tax = round(40000 * 0.15, 2)
    expected_effective_rate = round(expected_tax / salary, 4)

    assert result["total_tax"] == expected_tax
    assert result["effective_rate"] == expected_effective_rate
    assert len(result["tax_breakdown"]) == 1

def test_calculate_tax_spanning_multiple_brackets():
    salary = 60000
    tax_brackets = [
        {"min": 0, "max": 50197, "rate": 0.15},
        {"min": 50197, "max": 100392, "rate": 0.205},
        {"min": 100392, "max": 155625, "rate": 0.26},
        {"min": 155625, "max": 221708, "rate": 0.29},
        {"min": 221708, "rate": 0.33}
    ]
    result = calculate_tax(salary, tax_brackets)
    tax_first_bracket = 50197 * 0.15
    tax_second_bracket = 9803 * 0.205
    expected_total_tax = round(tax_first_bracket + tax_second_bracket, 2)
    expected_effective_rate = round(expected_total_tax / salary, 4)

    assert result["total_tax"] == expected_total_tax
    assert result["effective_rate"] == expected_effective_rate
    assert len(result["tax_breakdown"]) >= 2
