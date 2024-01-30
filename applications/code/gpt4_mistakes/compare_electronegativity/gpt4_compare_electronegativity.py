def compare_electronegativity(element1,element2):
    """
    This function returns True if element1 has a larger Pauling electronegativity than element2
    """
    import mendeleev
    element1 = mendeleev.element(element1)
    element2 = mendeleev.element(element2)
    result = element1.electronegativity_pauling > element2.electronegativity_pauling
    return result