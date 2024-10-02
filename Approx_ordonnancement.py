import random

taches=[]

n= int(input(" Veuillez saisir le nombre de tâches !? \n"))
m  = int(input(" Veuillez saisir le nombre de machines !? \n"))

for i in range(n):
    taches.append({'num':i+1 , "pi":random.randint(1, 1000)})

# print("\t les taches a ordonner sont les suivantes \n")
# for t in taches:
#     print("La tache T"+str(t["num"]) + " avec un temps de traitement = "+str(t["pi"])+" \n")

myFile = open("Ordononcement.txt", "w")
myFile.write("\t les taches a ordonner sont les suivantes \n\n")
for t in taches:
    myFile.write("La tache T"+str(t["num"]) + " avec un temps de traitement = "+str(t["pi"])+" \n")

####################### Initialiser l'ordonnencement #################
ordononcement=[]
ordonnancement = [[] for _ in range(m)]

####################### stocke le temps de traitement total de chaque machine jusqu'à présent
machine_temps = [0] * m


########################   Ordre décroissant  ########################################

def Ordre_Desc(list_Taches):
    Ordre_Desc_list = sorted(list_Taches, key=lambda x: x["pi"], reverse=True)
    return Ordre_Desc_list

########################   prendre les 10 premiere taches (supposons k=10)  ########################################

taches_decroissant= Ordre_Desc(taches)
taches10= taches_decroissant[0:10]
taches_Rest= taches_decroissant[10:]

# print(taches10)
# print(taches_Rest)

####################### Ordononcement (premiere tache non traité affecter au premiere machine libre  ) ##
list_Taches=Ordre_Desc(taches)

def Ordononcement_M_libre(list_Taches):
    for t in list_Taches:
            machine_libre = machine_temps.index(min(machine_temps))
            ordonnancement[machine_libre].append(t)
            machine_temps[machine_libre] += t["pi"]

########################################################################################################
### toutes les permutations possibles
def Permutation(taches):
    if len(taches) == 1:
        return [taches]

    permutations = []
    for i in range(len(taches)):
        tache = taches[i]
        taches_restantes = taches[:i] + taches[i+1:]
        remaining_permutations = Permutation(taches_restantes)
        for permutation in remaining_permutations:
            permutations.append([tache] + permutation)

    return permutations


def Ordononcement_permutations(taches, num_machines):
    # Générer toutes les permutations possibles des tâches
    all_permutations = Permutation(taches)

    # Pour chaque permutation, calculer la durée totale d'exécution sur chaque machine
    best_permutation = None
    min_total_time = float('inf')
    for permutation in all_permutations:
        machine_times = [0] * num_machines
        for tache in permutation:
        # Ajouter la tâche à la machine la moins chargée
            min_time = min(machine_times)
            machine_index = machine_times.index(min_time)
            machine_times[machine_index] += tache['pi']

        # Vérifier si cette permutation est la meilleure
        total_time = max(machine_times)
        if total_time < min_total_time:
            best_permutation = permutation
            min_total_time = total_time

    # Renvoyer la meilleure permutation 
    return (best_permutation)

ord1=Ordononcement_permutations(taches10,m)
Ordononcement_M_libre(ord1)

# ord1=Ordononcement_permutations(taches10,m)
# print(ord1)
# print (Ordononcement_permutations(taches,m))
#################################################################################



######################   Ordonner les taches qui reste selon  LPT      ############
def LPT(list_Taches):
    t=Ordre_Desc(list_Taches)
    Ordononcement_M_libre(t)

LPT(taches_Rest)

#ordononcement=Ordononcement_M_libre(list_Taches)
# print (Ordre_Desc(taches))
# print(ordonnancement)
# print(machine_temps)

# print(ordonnancement)

# print("\t l'ordre sur les differentes machines est ' \n")
# for o in range(len(ordonnancement)):
#     print("L'ordre sur la machnine "+ str(o+1) + " est : ")
#     for i in range(len(ordonnancement[o])):
#         print("T"+str(ordonnancement[o][i]["num"] ))

# print(" \n La Valeur de Cmax ="+str(max(machine_temps)))



myFile.write

myFile.write("\n\t La solution approximative du probleme P||Cmax : \n\n")
for o in range(len(ordonnancement)):
    myFile.write("\nL'ordre sur la machnine "+ str(o+1) + " est : \t")
    for i in range(len(ordonnancement[o])):
        myFile.write("T"+str(ordonnancement[o][i]["num"])+"\t" )

myFile.write("\n \n La Valeur de Cmax ="+str(max(machine_temps)))