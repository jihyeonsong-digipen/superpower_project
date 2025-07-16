def ultraPower(f, g, n):
    """
    Computes the ultraproduct of two functions f and g over a natural number n.
    
    Parameters:
    f (function): A function that takes an integer and returns a value.
    g (function): Another function that takes an integer and returns a value.
    n (int): The number of elements to consider in the ultraproduct.
    
    Returns:
    function: A new function representing the ultraproduct of f and g.
    """
    def ultraproduct(x):
        return f(x) * g(x) / n
    
    return ultraproduct
    print(f"Teleporting {player.name} to {destination}...")