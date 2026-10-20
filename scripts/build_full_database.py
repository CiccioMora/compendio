import json

pythagorean = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
    'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
    'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
}

def calc_v(formula):
    clean = [c.upper() for c in formula if c.upper() in pythagorean]
    total = sum(pythagorean[c] for c in clean)
    s = total
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total, s

geometry_map = {
    1: 'Circonferenza (Elemento Acqua)',
    2: 'Angolo / Linea',
    3: 'Triangolo equilatero',
    4: 'Quadrato',
    5: 'Pentagono regolare (Elemento Aria)',
    6: 'Esagono regolare (Elemento Terra)',
    7: 'Ettagono regolare (Opposizione / Massima Energia)',
    8: 'Ottagono regolare (Elemento Fuoco)',
    9: 'Ellisse (Reincarnazione / Dinamismo estremo)'
}

# Read existing spellsData.js if needed or build the complete master list
# Let's write the comprehensive list in Python
