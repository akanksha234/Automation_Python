class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __repr__(self):
        formula = ""
        for atom in self.atoms:
            formula += atom.label
        return formula


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
print(salt)
salt = sodium + chlorine
print(salt)

