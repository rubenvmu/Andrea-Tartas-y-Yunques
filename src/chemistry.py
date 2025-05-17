ELEMENTS = {
    'Na': 'Sodio',
    'Cl': 'Cloro',
    'H': 'Hidrógeno',
    'O': 'Oxígeno',
    'C': 'Carbono',
}

RECETAS = {
    ('Na', 'Cl'): 'Sal',
    ('H', 'O'): 'Agua',
    ('C', 'H', 'O'): 'Paracetamol',
}

def combine_elements(inventory):
    key = tuple(sorted(inventory))
    return RECETAS.get(key, "Fórmula no válida")