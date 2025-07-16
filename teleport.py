def teleport(player, destination):
    """
    Teleports the player to the specified destination.

    Args:
        player (Player): The player to teleport.
        destination (str): The destination to teleport the player to.

    Returns:
        str: Confirmation message of the teleportation.
    """
    # Assuming player has a method to set their location
    player.set_location(destination)
    return f"{player.name} has been teleported to {destination}."