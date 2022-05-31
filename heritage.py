

class Heritage:

    def __init__(self, reseaux_semantique):
        self.reseaux_semantique = reseaux_semantique

    def _proprieter_node(self, node):
        return [conection for conection in node.connections_to if conection.name != "is a" and conection.type != "exeption"] + [conection for conection in node.connections_from if conection.name != "is a" and conection.type != "exeption"]

    def solve_for_node(self, node_id):

        node = self.reseaux_semantique[node_id]

        self.proprieter = self._proprieter_node(node)
        self.heritage = [node]

        index = 0
        changed = True
        while changed:
            parents = [conection.node for conection in node.connections_to if conection.name == "is a"]
            for parent in parents:
                self.proprieter += self._proprieter_node(parent)

            self.heritage += parents
            index += 1
            if index == len(self.heritage):
                changed = False
            else:
                node = self.heritage[index]

        return self.heritage, self.proprieter


    def print_heriter(self):
        print("Resultats de l'inferecne des classes utiliser:")
        for h in self.heritage:
            print(h.name)
        print()

    def print_proprieter(self):
        print("Deduction des propriétés:")
        for p in self.proprieter:
            print(p.name, p.node.name)
        print()
