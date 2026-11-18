# Projet NSI

Bienvenue sur le dépôt de notre projet de groupe réalisé dans le cadre de la spécialité **Numérique et sciences informatiques (NSI)**.

Le projet consiste à concevoir et développer collectivement un jeu en Python, jouable dans un terminal. Son concept et ses règles sont encore en cours de définition : cette documentation sera complétée au fur et à mesure des décisions prises par l'équipe.

## Objectifs

- Concevoir un jeu en Python en respectant les contraintes du projet scolaire.
- Organiser le développement à plusieurs avec Git et GitHub.
- Apprendre à travailler avec des branches, des commits et des Pull Requests.
- Expliquer les choix techniques et conserver une trace des décisions du groupe.

## État du projet

Le dépôt est en phase de préparation. Le langage et le principe d'une interface en terminal sont définis, mais les règles du jeu, son nom, son architecture et son point d'entrée restent à préciser.

Les informations connues et les points à décider sont répertoriés dans [`docs/PROJECT-OVERVIEW.md`](docs/PROJECT-OVERVIEW.md).

## Prérequis

Pour contribuer au dépôt, il faut disposer de :

- Git ;
- Python 3 (la version minimale sera précisée lorsque le projet l'exigera) ;
- un compte GitHub avec accès au dépôt.

**Éditeur recommandé :** Visual Studio Code, avec les extensions proposées dans [`.vscode/extensions.json`](.vscode/extensions.json). Il reste possible d'utiliser un autre éditeur.

Le guide d'installation explique comment préparer son environnement sous Windows et Linux, notamment Arch Linux : [`docs/INSTALLATION-GUIDE.md`](docs/INSTALLATION-GUIDE.md).

## Lancer le projet

Le programme n'a pas encore de point d'entrée définitif. Les instructions de lancement seront ajoutées ici lorsque la structure du code aura été décidée et mise en place.

## Documentation

| Document | À quoi sert-il ? |
|---|---|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Les règles à suivre pour proposer une contribution. |
| [`docs/INSTALLATION-GUIDE.md`](docs/INSTALLATION-GUIDE.md) | Installer les outils et préparer son environnement. |
| [`docs/GIT-GUIDE.md`](docs/GIT-GUIDE.md) | Comprendre les notions Git et retrouver les commandes courantes. |
| [`docs/COLLABORATION-GUIDE.md`](docs/COLLABORATION-GUIDE.md) | Suivre le workflow de l'équipe, de l'Issue à la fusion. |
| [`docs/GITHUB-CONFIGURATION.md`](docs/GITHUB-CONFIGURATION.md) | Retrouver les règles et paramètres prévus pour le dépôt. |
| [`docs/PROJECT-OVERVIEW.md`](docs/PROJECT-OVERVIEW.md) | Comprendre le contexte et l'état de définition du jeu. |
| [`docs/TECHNICAL-DESIGN.md`](docs/TECHNICAL-DESIGN.md) | Suivre la future conception technique du jeu. |
| [`docs/DECISIONS.md`](docs/DECISIONS.md) | Consulter les décisions prises ou restant à valider. |

## Organisation prévue du dépôt

```text
projet-nsi/
├── .github/               # Modèles GitHub et futurs workflows
├── .vscode/               # Recommandations d'extensions VS Code
├── docs/                  # Documentation du projet et guides
├── src/                   # Code source (à créer)
├── tests/                 # Tests (à créer)
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

Les dossiers `src/` et `tests/` seront ajoutés lorsque l'équipe aura défini la première structure du programme. Il n'est pas utile de créer des fichiers vides avant d'en connaître le rôle.

## Contribuer

Avant de commencer, lis [`CONTRIBUTING.md`](CONTRIBUTING.md) et le [guide de collaboration](docs/COLLABORATION-GUIDE.md). Les modifications destinées à `main` passent par une Pull Request : on ne développe pas directement sur la branche principale.
