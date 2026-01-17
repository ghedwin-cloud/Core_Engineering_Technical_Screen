from sorter.sort import sort

# -------------------------
# Standard behavior tests
# -------------------------

def test_standard_package():
    assert sort(50, 50, 50, 10) == "STANDARD"


def test_heavy_only():
    assert sort(50, 50, 50, 20) == "SPECIAL"


def test_bulky_by_volume():
    assert sort(100, 100, 100, 10) == "SPECIAL"


def test_bulky_by_dimension():
    assert sort(150, 20, 20, 5) == "SPECIAL"


def test_bulky_and_heavy():
    assert sort(100, 100, 100, 20) == "REJECTED"


# -------------------------
# Edge case tests
# -------------------------

def test_exact_volume_threshold():
    assert sort(100, 100, 100, 19) == "SPECIAL"


def test_just_below_volume_threshold():
    assert sort(100, 100, 99, 19) == "STANDARD"


def test_exact_dimension_threshold():
    assert sort(150, 10, 10, 19) == "SPECIAL"


def test_just_below_dimension_threshold():
    assert sort(149, 149, 149, 19) == "STANDARD"


def test_exact_mass_threshold():
    assert sort(50, 50, 50, 20) == "SPECIAL"


def test_just_below_mass_threshold():
    assert sort(50, 50, 50, 19) == "STANDARD"


# -------------------------
# Combined boundary cases
# -------------------------

def test_volume_and_mass_thresholds():
    assert sort(100, 100, 100, 20) == "REJECTED"


def test_dimension_and_mass_thresholds():
    assert sort(150, 50, 50, 20) == "REJECTED"
