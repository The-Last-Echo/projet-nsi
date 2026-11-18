# Présentation du projet

Ce document rassemble les informations connues sur le projet. Il doit évoluer à mesure que le groupe précise le concept et prend ses décisions.

## 1. Contexte

Projet de groupe réalisé dans le cadre de la spécialité **Numérique et sciences informatiques (NSI)** en Première générale.

Le développement est effectué en Python par une équipe de deux à trois élèves.

## 2. Concept général

Le projet prendra la forme d'un jeu jouable dans un terminal ou une console.

Le concept exact, les objectifs, les règles, les mécaniques et les conditions de victoire ou de défaite restent à définir collectivement. Aucune mécanique de jeu ne doit être considérée comme décidée tant qu'elle n'a pas été validée par le groupe.

## 3. Choix techniques connus

| Élément | État |
|---|---|
| Langage | Python |
| Interface | Terminal / console |
| Grille | Une représentation par liste de listes est envisagée |
| Représentation du joueur | Un caractère ou un symbole est envisagé |
| Gestion de versions | Git |
| Hébergement et collaboration | GitHub |
| Dépôt | `The-Last-Echo/projet-nsi` |
| Branche principale | `main` |
| Communication d'équipe | Discord |
| Éditeur recommandé | Visual Studio Code, sans obligation |

La liste de listes et la représentation du joueur sont des pistes connues, mais leurs détails restent à valider pendant la conception technique.

## 4. Organisation du développement

- Les modifications sont développées sur des branches dédiées.
- Les branches suivent les préfixes `feature/`, `fix/`, `docs/` et `refactor/`.
- Les messages de commit suivent Conventional Commits et sont rédigés en anglais.
- Les modifications destinées à `main` passent par une Pull Request.
- La méthode de fusion prévue est Squash and merge.
- Les décisions importantes doivent être conservées dans la documentation du dépôt, et pas uniquement dans les échanges Discord.

Les règles détaillées sont décrites dans [`GITHUB-CONFIGURATION.md`](GITHUB-CONFIGURATION.md) et [`COLLABORATION-GUIDE.md`](COLLABORATION-GUIDE.md).

## 5. Points à définir collectivement

- [ ] Nom définitif du jeu.
- [ ] Concept et objectif principal.
- [ ] Règles complètes.
- [ ] Conditions de victoire et de défaite.
- [ ] Dimensions et contenu de la grille.
- [ ] Déplacements et interactions.
- [ ] Éléments présents dans le jeu.
- [ ] Gestion de l'état du jeu.
- [ ] Score, progression ou autres systèmes éventuels.
- [ ] Organisation des modules Python.
- [ ] Répartition des responsabilités dans l'équipe.
- [ ] Version minimale de Python.
- [ ] Stratégie de tests.

Cette liste n'impose aucune mécanique : elle sert uniquement à ne pas oublier les sujets à discuter.

## 6. Documents associés

- [`TECHNICAL-DESIGN.md`](TECHNICAL-DESIGN.md) : future conception technique.
- [`DECISIONS.md`](DECISIONS.md) : historique des décisions.
- [`GITHUB-CONFIGURATION.md`](GITHUB-CONFIGURATION.md) : règles de collaboration.
- [`../README.md`](../README.md) : présentation à destination des visiteurs du dépôt.
