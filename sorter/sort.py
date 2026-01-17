def sort(width, height, length, mass):
    """
    Dispatch a package to the correct stack.

    Parameters:
        width (int): width in cm
        height (int): height in cm
        length (int): length in cm
        mass (int): mass in kg

    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"
    """
    volume = width * height * length

    bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
