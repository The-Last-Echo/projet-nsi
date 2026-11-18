# Présentation du projet

Ce document rassemble les informations connues sur le projet. Il sera mis à jour à mesure que le groupe précise le concept et valide ses choix.

## 1. Contexte

Projet de groupe réalisé dans le cadre de la spécialité **Numérique et sciences informatiques (NSI)** en Première générale.

Le développement est effectué en Python par une équipe de deux à trois élèves.

## 2. Concept général

Le projet prendra la forme d'un jeu jouable dans un terminal ou une console.

Le concept exact, les objectifs, les règles, les mécaniques et les conditions de victoire ou de défaite restent à définir collectivement. Aucune mécanique ne doit être considérée comme décidée tant qu'elle n'a pas été validée par l'équipe.

## 3. Choix techniques connus

| Élément | État |
|---|---|
| Langage | Python |
| Interface | Terminal / console |
| Code source | Dossier `src/` prévu, à créer avec le premier code |
| Tests | Dossier `tests/` prévu, à créer avec les premiers tests |
| Environnement Python | Environnement virtuel `.venv` par membre |
| Gestion de versions | Git |
| Hébergement et collaboration | GitHub |
| Dépôt | `The-Last-Echo/projet-nsi` |
| Branche principale | `main` |
| Communication rapide | Discord |
| Cahier des charges et comptes rendus | Word partagé |
| Éditeur recommandé | Visual Studio Code, sans obligation |

La structure du code, le point d'entrée et la version minimale de Python restent à définir.

## 4. Organisation du développement

- Les modifications sont développées sur des branches dédiées.
- Les branches suivent les préfixes `feature/`, `fix/`, `docs/` et `refactor/`.
- Les messages de commit suivent Conventional Commits et sont rédigés en anglais.
- Les modifications destinées à `main` passent par une Pull Request.
- La méthode de fusion retenue est Squash and merge.
- Une Issue est utilisée lorsqu'elle aide à suivre un bug, une fonctionnalité ou une tâche ; elle n'est pas obligatoire pour chaque petite modification.
- Les décisions importantes doivent être conservées dans la documentation du dépôt, pas uniquement dans les échanges Discord ou Word.

Les règles détaillées sont décrites dans [`GITHUB-CONFIGURATION.md`](GITHUB-CONFIGURATION.md) et [`COLLABORATION-GUIDE.md`](COLLABORATION-GUIDE.md).

## 5. Points à définir collectivement

- [ ] Nom définitif du jeu.
- [ ] Concept et objectif principal.
- [ ] Règles complètes.
- [ ] Conditions de victoire et de défaite.
- [ ] Dimensions et contenu de la grille, si le jeu en utilise une.
- [ ] Déplacements et interactions.
- [ ] Éléments présents dans le jeu.
- [ ] Gestion de l'état du jeu.
- [ ] Score, progression ou autres systèmes éventuels.
- [ ] Organisation des modules Python.
- [ ] Répartition des responsabilités dans l'équipe.
- [ ] Version minimale de Python.
- [ ] Dépendances éventuelles.
- [ ] Stratégie et outils de tests.

Cette liste sert à guider la conception ; elle n'impose aucune mécanique de jeu.

## 6. Documents associés

- [`TECHNICAL-DESIGN.md`](TECHNICAL-DESIGN.md) : conception technique à compléter lorsque les règles seront connues.
- [`DECISIONS.md`](DECISIONS.md) : décisions structurantes validées par l'équipe.
- [`GITHUB-CONFIGURATION.md`](GITHUB-CONFIGURATION.md) : organisation du dépôt et règles GitHub.
- [`PYTHON-ENVIRONMENT.md`](PYTHON-ENVIRONMENT.md) : création et utilisation de l'environnement virtuel.
- [`../README.md`](../README.md) : présentation générale du dépôt.
