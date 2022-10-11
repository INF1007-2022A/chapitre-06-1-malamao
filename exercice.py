#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        valeurs = []
        while (len(valeurs) < 10):
            valeurs.append(input("Veuillez entrer une valeur\n"))
    valeurs_num = []
    valeurs_str = []
    for element in valeurs:
        if element.isdigit():
            valeurs_num.append(element)
        else:
            valeurs_str.append(element)
    return sorted(valeurs_num)+sorted(valeurs_str)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input("Veuillez entrer le premier anagramme:\n")
        mot2 = input("Veuillez entrer le deuxième anagramme:\n")

    anagramme = False
    if len(mot1) == len(mot2):
        if sorted(mot1.upper()) == sorted(mot2.upper()):
            anagramme = True
            print("Les deux mots sont des anagrammes!")
    if anagramme == False:
        print("Ces deux mots ne sont pas des anagrammes")
    return anagramme


def contains_doubles(items: list) -> bool:
    doublon=False
    for n in range(len(items)):
        element=items[n]
        for k in range(len(items)):
            if k != n:
                if element==items[k]:
                    doublon=True

    return doublon


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    moyennes = {}
    for eleve in student_grades:
        notes = student_grades[eleve]
        somme = 0
        for score in notes:
            somme += score
        moyenne = somme / len(notes)
        moyennes[eleve] = moyenne
    meilleure_moy = [1]
    note = 0
    for cle in moyennes:
        if moyennes[cle] > note:
            meilleure_moy[0] = cle
    meilleur_eleve = {cle: moyennes[cle]}

    return meilleur_eleve


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    histogramme = {}
    for letter in sentence:
        if letter.isalpha():
            if letter in histogramme:
                histogramme[letter]+=1
            else:
                histogramme[letter]=1

    liste = []
    for cle in histogramme:
        if histogramme[cle]>5:
            liste.append((histogramme[cle], cle))
    print(sorted(liste, reverse=True))

    return liste


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recette = input("Veuillez entrer le nom de la recette: \n")
    ingredients = input("Veuillez entrer les ingrédients, séparés d'une virgule:\n").split(",")
    return {recette: ingredients}

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette = input("Quelle recette voulez vous voir?\n")
    if recette in ingredients:
        print("Les ingrédients sont:\n", ingredients[recette])
    else:
        print("Cette recette n'est pas dans le livre")


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #print(order())

    #print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
