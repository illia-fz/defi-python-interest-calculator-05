import math
from src.compound import compound
import pytest

def test_typical():
    assert math.isclose(compound(1000, 0.05, 5), 1276.2815625, rel_tol=1e-9)

@pytest.mark.parametrize("p,r,n,expected", [
    (0, 0.05, 10, 0),
    (1000, 0.0, 10, 1000),
    (1000, -0.5, 1, 500),
])
def test_parametric(p, r, n, expected):
    assert math.isclose(compound(p, r, n), expected, rel_tol=1e-9)

def test_invalid():
    import pytest
    with pytest.raises(ValueError):
        compound(-1, 0.1, 5)
