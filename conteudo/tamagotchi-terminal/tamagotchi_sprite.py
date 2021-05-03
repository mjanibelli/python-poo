pequeno = """
             ===
            |o o|
             ===
"""

medio = """
             ===
            |o o|
            | u |
             ===
"""

grande = """
            =====
           | - - |
        o--| O O |--o
           |  u  |
            =====
"""


def mostrar_sprite(dias_vida):
    if dias_vida < 5:
        sprite = pequeno
    
    elif 5 <= dias_vida < 10:
        sprite = medio
    
    else:
        sprite = grande

    return sprite
