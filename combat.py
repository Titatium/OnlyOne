import random

def calculate_attack(attacker, defender):
    """Calculates the attack damage based on attacker's strength and defender's defense."""
    base_damage = attacker.strength
    damage_reduction = defender.defense // 2  # Adjust division as needed for balance
    final_damage = max(0, base_damage - damage_reduction)

    # Add randomness for variation (optional)
    final_damage += random.randint(-2, 2)  # Adjust range as needed

    return final_damage

def apply_damage(target, damage):
    """Reduces a character's health based on the calculated damage."""
    target.health -= damage

def check_for_victory(player, opponent):
    """Determines if either the player or the opponent has won the combat encounter."""
    if player.health <= 0:
        return "opponent"  # Opponent wins
    elif opponent.health <= 0:
        return "player"  # Player wins
    else:
        return None  # Combat continues

def handle_combat_round(player, opponent):
    """Manages a single round of combat between the player and an opponent."""

    # Player's turn
    player_damage = calculate_attack(player, opponent)
    apply_damage(opponent, player_damage)
    print(f"You attack the {opponent.name} for {player_damage} damage!")

    # Check for victory after player's attack
    victor = check_for_victory(player, opponent)
    if victor:
        return victor

    # Opponent's turn
    opponent_damage = calculate_attack(opponent, player)
    apply_damage(player, opponent_damage)
    print(f"The {opponent.name} attacks you for {opponent_damage} damage!")

    # Check for victory after opponent's attack
    victor = check_for_victory(player, opponent)
    if victor:
        return victor

    return None  # No victor yet, combat continues
