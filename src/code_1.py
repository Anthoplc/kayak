import pandas as pd
import matplotlib.pyplot as plt

droit_nour1 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotD_Nour1_Machine.csv", delimiter=";")
gauche_nour1 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotG_Nour1_Machine.csv", delimiter=";")
gauche_nour2 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotG_Nour2_Machine.csv", delimiter=";")
milieu_nour2 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotM_Nour2_Machine.csv", delimiter=";")
droit_louison1 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotD_Louison1_Machine.csv", delimiter=";")
gauche_louison1 = pd.read_csv("C:/Users/antho/Documents/Digisport/Semestre_3/Projet_kayak/data/DotG_Louison1_Machine.csv", delimiter=";")
nour = "Nour"
Louison = "Louison"

def compare_sides(df_left, df_right, variable, nom, start_index, end_index):
    """
    Compare les deux côtés d'un DataFrame pour une variable spécifiée dans un intervalle donné.

    Paramètres :
    - df_left : DataFrame pour le côté gauche
    - df_right : DataFrame pour le côté droit
    - variable : Nom de la variable à comparer
    - start_index : Index de début de l'intervalle
    - end_index : Index de fin de l'intervalle
    """
    
    # Créer une nouvelle figure pour chaque graphique
    plt.figure()
    
    plt.plot(df_left.index[start_index:end_index], df_left[variable].iloc[start_index:end_index], label='Gauche - ' + variable)
    plt.plot(df_right.index[start_index:end_index], df_right[variable].iloc[start_index:end_index], label='Droit - ' + variable)

    # Ajouter une légende
    plt.legend()

    # Ajouter des titres et des étiquettes d'axe
    plt.title(f'Comparaison du côté {df_left} et {df_right} de {nom} pour {variable} entre les lignes {start_index} et {end_index}')
    plt.xlabel('Index')
    plt.ylabel('m/s')



# Exemple d'utilisation
compare_sides(gauche_nour1, droit_nour1, 'Acc_X', nour, 2000, 3000)
compare_sides(gauche_nour1, droit_nour1, 'Acc_Y', nour, 2000, 3000)
compare_sides(gauche_nour1, droit_nour1, 'Acc_Z', nour, 2000, 3000)
compare_sides(gauche_louison1, droit_louison1, 'Acc_X', Louison, 2000, 3000)
compare_sides(gauche_louison1, droit_louison1, 'Acc_Y', Louison, 2000, 3000)
compare_sides(gauche_louison1, droit_louison1, 'Acc_Z', Louison, 2000, 3000)

# Afficher le graphique
plt.show()