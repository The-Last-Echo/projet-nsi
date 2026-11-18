# Décisions du projet

Ce fichier conserve les choix importants qui influencent l'organisation ou la conception du projet. Il évite de devoir retrouver une décision dans une ancienne conversation Discord ou dans un compte rendu.

Une proposition n'est considérée comme adoptée qu'après validation par l'équipe. Les éléments marqués **à décider** ne sont pas des règles définitives.

## 1. Contexte et faits établis

| Sujet | Information | État |
|---|---|---|
| Cadre | Projet de groupe de spécialité NSI en Première générale | Établi |
| Équipe | 2 à 3 élèves | Établi |
| Langage | Python | Établi |
| Interface | Jeu en terminal / console | Établi |
| Hébergement | Dépôt public GitHub `The-Last-Echo/projet-nsi` | Établi |
| Branche principale | `main` | Établi |
| Communication rapide | Discord | Établi |
| Cahier des charges et comptes rendus | Document Word partagé par l'équipe | Retenu |

## 2. Organisation Git et GitHub

| Sujet | Décision ou orientation | État |
|---|---|---|
| Branches | `feature/`, `fix/`, `docs/`, `refactor/` | Retenu |
| Commits | Conventional Commits en anglais | Retenu |
| Pull Requests | Toute modification destinée à `main` passe par une PR | Retenu |
| Issues | Utiles pour suivre les tâches importantes, mais non obligatoires pour chaque changement | Retenu |
| Fusion | Squash and merge | Retenu |
| Review | Une autre personne relit la PR avant fusion | Retenu comme règle d'équipe |
| Protection de `main` | Règles de protection configurées sur GitHub | À vérifier dans les paramètres réels |
| GitHub Actions | Automatiser les tests plus tard | Reporté jusqu'à l'existence du code et des tests |

## 3. Environnement de développement

| Sujet | Décision ou orientation | État |
|---|---|---|
| Éditeur | Visual Studio Code recommandé, non obligatoire | Retenu comme recommandation |
| Extensions | Python, GitLens, GitHub Pull Requests and Issues, Markdown All in One | Recommandées |
| Environnement Python | Un environnement virtuel `.venv` par copie locale du projet | Retenu |
| Dépendances | Partagées dans `requirements.txt` lorsqu'elles seront définies | À mettre en place avec le code |
| Source documentaire technique | Markdown versionné dans GitHub | Retenu |
| Cahier des charges | Document Word partagé | Retenu |
| PDF | Supports pédagogiques pouvant être exportés depuis les documents sources | À faire si utile |

## 4. Organisation des dossiers

| Dossier | Rôle prévu | État |
|---|---|---|
| `src/` | Code source Python | Retenu, à créer avec le premier code |
| `tests/` | Tests du programme | Retenu, à créer avec les premiers tests |
| `docs/` | Documentation et guides | Présent |
| `.github/` | Modèles GitHub et futurs workflows automatisés | Présent, workflows reportés |

Le dossier `src/` est retenu pour le code source. Le nom `srv/` n'est pas utilisé pour ce projet.

## 5. Conception du jeu

Les éléments suivants restent à définir collectivement :

- nom et concept du jeu ;
- règles et conditions de fin ;
- dimensions et contenu de la grille ;
- représentation et comportement du joueur ;
- éléments et interactions du jeu ;
- organisation des modules Python ;
- version minimale de Python ;
- dépendances éventuelles ;
- stratégie et outils de test.

Une grille sous forme de liste de listes et un joueur représenté par un caractère ou un symbole sont des pistes envisagées, pas une spécification définitive.

## 6. Licence

Aucune licence open source n'a été choisie. L'équipe doit discuter de ce point avant d'ajouter un fichier `LICENSE`.

## 7. Ajouter une décision

Pour une décision structurante, ajouter une entrée comprenant :

- la date ;
- le sujet ;
- la décision prise ;
- la raison du choix ;
- les personnes ayant validé ;
- les conséquences éventuelles sur le code ou la documentation.

Les comptes rendus complets restent dans le document Word partagé. Ce fichier ne conserve que les décisions qui doivent rester une référence durable pour le dépôt.
