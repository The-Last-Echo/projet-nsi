# Projet NSI

Bienvenue sur le dépôt de notre projet de groupe réalisé dans le cadre de la spécialité **Numérique et sciences informatiques (NSI)**.

Le projet consiste à concevoir et développer collectivement un jeu en Python, jouable dans un terminal. Son concept et ses règles sont encore en cours de définition : cette documentation sera complétée au fur et à mesure des décisions prises par l'équipe.

## Objectifs

- Concevoir un jeu en Python en respectant les contraintes du projet scolaire.
- Apprendre à développer à plusieurs avec Git et GitHub.
- Utiliser des branches, des commits et des Pull Requests pour organiser les modifications.
- Conserver une documentation claire et une trace des décisions importantes.

## État du projet

Le dépôt est en phase de préparation. Le langage Python et le principe d'une interface en terminal sont définis, mais le nom du jeu, ses règles, son architecture et son point d'entrée restent à décider.

Les informations connues et les points à définir sont répertoriés dans [`docs/PROJECT-OVERVIEW.md`](docs/PROJECT-OVERVIEW.md).

## Prérequis

Pour contribuer au projet, il faudra disposer de :

- **Git**, pour gérer l'historique du code ;
- **Python 3**, pour exécuter le jeu ;
- **un compte GitHub** ayant accepté l'invitation au dépôt pour pouvoir envoyer des modifications ;
- **GitHub CLI (`gh`)**, recommandé pour se connecter à GitHub et consulter les Pull Requests depuis le terminal.

**Éditeur recommandé :** Visual Studio Code, avec les extensions proposées dans [`.vscode/extensions.json`](.vscode/extensions.json). Un autre éditeur reste possible.

Commence par le [guide d'installation](docs/INSTALLATION-GUIDE.md), puis suis le [guide de l'environnement Python](docs/PYTHON-ENVIRONMENT.md) pour préparer ton environnement virtuel.

## Lancer le projet

Le code du jeu n'a pas encore été créé et son point d'entrée n'est pas défini. Les instructions de lancement seront ajoutées ici lorsque l'architecture aura été décidée.

## Où trouver les informations ?

| Outil ou document | Utilisation |
|---|---|
| **GitHub** | Code, historique, Issues, Pull Requests et documentation technique validée. |
| **Word** | Cahier des charges collaboratif et comptes rendus de réunion. Les décisions validées et utiles au développement doivent ensuite être reportées dans GitHub. |
| **Discord** | Questions, échanges rapides et coordination de l'équipe. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Les règles essentielles pour proposer une modification. |
| [`docs/INSTALLATION-GUIDE.md`](docs/INSTALLATION-GUIDE.md) | Installer Git, Python, GitHub CLI et préparer les outils. |
| [`docs/PYTHON-ENVIRONMENT.md`](docs/PYTHON-ENVIRONMENT.md) | Créer, activer et utiliser l'environnement virtuel Python. |
| [`docs/GIT-GUIDE.md`](docs/GIT-GUIDE.md) | Comprendre Git et retrouver les commandes courantes. |
| [`docs/COLLABORATION-GUIDE.md`](docs/COLLABORATION-GUIDE.md) | Suivre le workflow de l'équipe, de la branche à la Pull Request. |
| [`docs/GITHUB-CONFIGURATION.md`](docs/GITHUB-CONFIGURATION.md) | Comprendre les règles et paramètres du dépôt GitHub. |
| [`docs/PROJECT-OVERVIEW.md`](docs/PROJECT-OVERVIEW.md) | Comprendre le contexte et l'état de définition du jeu. |
| [`docs/TECHNICAL-DESIGN.md`](docs/TECHNICAL-DESIGN.md) | Suivre la future conception technique du jeu. |
| [`docs/DECISIONS.md`](docs/DECISIONS.md) | Consulter les décisions structurantes prises par l'équipe. |

## Organisation prévue du dépôt

```text
projet-nsi/
├── .github/               # Modèles GitHub et futurs workflows automatisés
├── .vscode/               # Recommandations d'extensions VS Code
├── docs/                  # Documentation et guides
├── src/                   # Code source Python (à créer)
├── tests/                 # Tests automatisés (à créer)
├── .gitignore             # Fichiers à ne pas envoyer sur GitHub
├── .gitattributes         # Fins de ligne cohérentes entre systèmes
├── CONTRIBUTING.md        # Règles pour contribuer
└── README.md              # Présentation du projet
```

Nous utiliserons `src/` pour le code source Python. Le dossier `srv/` n'est pas retenu : il est généralement associé à des données ou services dans certaines conventions Unix, pas au code source d'un projet Python classique.

Les dossiers `src/` et `tests/` seront créés lorsque l'équipe commencera à définir l'architecture. Il n'est pas nécessaire de créer des dossiers vides maintenant.

## Contribuer

Avant de commencer, lis [`CONTRIBUTING.md`](CONTRIBUTING.md). Les modifications destinées à `main` passent par une Pull Request : on ne développe pas directement sur la branche principale.
