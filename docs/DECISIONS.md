# Décisions du projet

Ce fichier garde une trace des choix qui influencent l'organisation ou la conception du projet. Il évite de devoir retrouver une décision importante dans une ancienne conversation Discord.

Une proposition n'est considérée comme adoptée qu'après discussion et validation par l'équipe. Les éléments marqués « à confirmer » ne doivent pas être présentés comme des règles déjà appliquées.

## 1. Contexte et faits établis

| Sujet | Information | État |
|---|---|---|
| Cadre | Projet de groupe de spécialité NSI en Première générale | Établi |
| Équipe | 2 à 3 élèves | Établi |
| Langage | Python | Établi |
| Interface | Jeu en terminal / console | Établi |
| Hébergement | GitHub, dépôt public `The-Last-Echo/projet-nsi` | Établi |
| Branche principale | `main` | Établi |
| Communication | Discord | Établi |

## 2. Organisation Git et GitHub

| Sujet | Orientation retenue | État |
|---|---|---|
| Branches | `feature/`, `fix/`, `docs/`, `refactor/` | Retenu pour le workflow |
| Commits | Conventional Commits en anglais | Retenu pour le workflow |
| Pull Requests | Toute modification destinée à `main` passe par une PR | Retenu pour le workflow |
| Fusion | Squash and merge | Retenu pour le workflow |
| Relecture | Le responsable de l'intégration relit les PR des autres membres ; si sa propre PR doit être fusionnée, un autre membre la relit | À confirmer collectivement |
| Protection de `main` | PR obligatoire, une approbation et conversations résolues | À configurer et vérifier sur GitHub |
| GitHub Actions | Ajouter les tests automatisés plus tard | Reporté |

## 3. Environnement de développement

| Sujet | Orientation retenue | État |
|---|---|---|
| Éditeur | Visual Studio Code recommandé, mais non obligatoire | Proposition retenue |
| Extensions | Python, GitLens, GitHub Pull Requests and Issues, Markdown All in One ; Ruff après définition des règles Python | Recommandé |
| Source documentaire | Markdown versionné dans le dépôt | Retenu |
| PDF | Supports pédagogiques exportés depuis les sources Markdown | Retenu comme principe |

## 4. Conception du jeu

Les éléments suivants restent à définir collectivement :

- nom et concept du jeu ;
- règles et conditions de fin ;
- structure et dimensions de la grille ;
- représentation et comportement du joueur ;
- autres éléments et interactions ;
- organisation des modules ;
- tests et version minimale de Python.

Une grille sous forme de liste de listes et un joueur représenté par un caractère ou un symbole sont des pistes envisagées, pas encore une spécification technique complète.

## 5. Licence

Aucune licence open source n'a été choisie. La décision doit être discutée avec l'ensemble des contributeurs avant d'ajouter un fichier `LICENSE`.

## 6. Ajouter une décision

Pour chaque décision importante, ajouter une entrée comprenant :

- la date ;
- le sujet ;
- la décision ou les options examinées ;
- la raison du choix ;
- les personnes ayant validé ;
- les conséquences éventuelles sur le code ou la documentation.

Pour une décision technique structurante, il peut être utile de créer une section dédiée plutôt que d'ajouter une simple ligne dans un tableau.
