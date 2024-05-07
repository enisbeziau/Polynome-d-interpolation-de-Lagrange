import sympy


x = sympy.symbols('x')


def calc_expression(a: list[int], b: list[int], long: int):
    """Applique l'algorithme du polynome d'interpolation de Lagrange"""
    expression = 0
    for i in range(long):
        term = b[i]
        for j in range(long):
            if j != i:
                term *= (x - a[j]) / (a[i] - a[j])
        expression += term
    return expression


def extraire_nbr(chaine: str) -> tuple[int, int]:
    """Renvoie [a,b] pour tout chaine de format P(a)=b"""
    return int(chaine.split('(')[1].split(')')[0]), int(chaine.split('=')[1])


def main() -> None:
    """Les inputs sont de la forme P(a)=b (les espaces sont importants)"""
    print("Entrez les conditions que doit respecter le polynome (appuyer sur entrée pour arrêter)")
    a, b = [], []
    fini = False
    while not fini:
        condition = input("==> ")
        if condition != '':
            valeur_a, valeur_b = extraire_nbr(condition)
            a.append(valeur_a)
            b.append(valeur_b)
        else:
            fini = True
    expression = calc_expression(a, b, len(a))
    sympy.pprint(sympy.expand(expression))


if __name__ == '__main__':
    main()
