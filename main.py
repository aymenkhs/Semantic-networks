import os
import argparse
import json

import graph
import propagation_marqueurs
import propagation_marqueurs_exeptions
import heritage


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-file", "--file", help="""The path of the json file""")
    parser.add_argument("-p", "--part", help="""1, 2 or 3""")
    parser.add_argument("-node", "--node", help="""""")
    parser.add_argument("-node2", "--node2", help="""""")
    return parser.parse_args()

def main():

    args = parse_arguments()

    file_path = args.file
    # read the json file
    with open(os.path.join("reseaux", file_path), "r") as jsonFile:
        data = json.load(jsonFile)

    sn =  graph.SemanticNetwork(data["name"])
    sn.add_nodes(data["nodes"])
    sn.add_connections(data["connections"])

    node = args.node

    if args.part == "1":
        print("Partie 1 : l'algorithme de propagation de marqueurs")
        node2 = args.node2
        PM = propagation_marqueurs.PropagationMarqueurs(sn)
        solved, action_soluce, type = PM.solve_for_node(sn.id_name(node), sn.id_name(node2))
        if solved:
            print("il y a bien un lien entre les 2 noeuds")
            print("SOLUTION")
            if type == 1:
                print( node2, action_soluce , node)
            elif type == 2:
                print( node, action_soluce , node2)
        else:
            print("il n'y a pas de liens entre les 2 noeuds")

    elif args.part == "2":
        print("Partie 2 : r l’algorithme d'héritage")
        heritage_algorithm = heritage.Heritage(sn)
        heriter, proprieter = heritage_algorithm.solve_for_node(sn.id_name(node))
        heritage_algorithm.print_heriter()
        heritage_algorithm.print_proprieter()

    elif args.part == "3":
        print("Partie 3 : n dans le cas des liens d'exception")
        node2 = args.node2
        PM = propagation_marqueurs.PropagationMarqueurs(sn)
        solved, action_soluce = PM.solve_for_node(sn.id_name(node), sn.id_name(node2))
        if solved:
            print("il y a bien un lien entre les 2 noeuds")
        else:
            print("il n'y a pas de liens entre les 2 noeuds")


if __name__ == '__main__':
    main()
