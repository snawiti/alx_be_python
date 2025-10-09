# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely perform division with error handling."""
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
