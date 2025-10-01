def compound(principal: float, rate: float, periods: int) -> float:
    if principal < 0 or rate < -1 or periods < 0:
        raise ValueError("Invalid inputs")
    return principal * (1 + rate) ** periods

if __name__ == "__main__":
    p, r, n = 1000.0, 0.05, 5
    print(f"Compound amount: {compound(p, r, n):.2f}")
