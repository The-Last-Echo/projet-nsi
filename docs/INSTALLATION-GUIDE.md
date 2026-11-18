# Guide d'installation — préparer son ordinateur

Ce guide explique comment installer les outils nécessaires au projet et connecter son ordinateur au dépôt GitHub. Il est destiné aux membres qui n'ont jamais utilisé Git.

Tu n'as pas besoin de tout comprendre immédiatement : suis les étapes dans l'ordre et vérifie les commandes indiquées.

## 1. Les outils nécessaires

| Outil | À quoi sert-il ? | Obligatoire ? |
|---|---|---|
| Python 3 | Exécuter et développer le jeu. | Oui |
| Git | Enregistrer l'historique des modifications. | Oui |
| GitHub | Héberger le code et collaborer en ligne. | Oui |
| GitHub CLI (`gh`) | Se connecter à GitHub et gérer les PR depuis le terminal. | Recommandé |
| Visual Studio Code | Éditer le code et la documentation. | Non, mais recommandé |

Le projet utilise une adresse GitHub en **HTTPS**. Il n'est pas nécessaire de créer une clé SSH pour suivre ce guide.

## 2. Installer les outils sous Windows

Ouvre **PowerShell**. Les commandes ci-dessous utilisent `winget`, le gestionnaire de paquets présent sur les versions récentes de Windows. Si `winget` n'est pas disponible, utilise les liens de téléchargement officiels indiqués sous chaque outil.

### 2.1 Installer Git

```powershell
winget install --id Git.Git -e
```

Tu peux aussi télécharger Git depuis [git-scm.com](https://git-scm.com/download/win).

Ferme puis rouvre PowerShell, puis vérifie :

```powershell
git --version
```

### 2.2 Installer GitHub CLI

```powershell
winget install --id GitHub.cli -e
```

Vérifie :

```powershell
gh --version
```

Page officielle : [Installation de GitHub CLI](https://github.com/cli/cli#installation).

### 2.3 Installer Python

Télécharge Python 3 depuis [python.org/downloads](https://www.python.org/downloads/). Pendant l'installation, conserve le lanceur Python (`py`) si l'installateur le propose.

Ouvre un nouveau PowerShell et vérifie :

```powershell
py --version
```

Si `py` n'est pas disponible, essaie :

```powershell
python --version
```

La version minimale de Python sera choisie par l'équipe au moment de définir le projet. Une fois ce choix fait, chaque membre devra installer cette même version.

### 2.4 Installer Visual Studio Code (facultatif)

Télécharge VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/). Pendant l'installation, l'option qui ajoute la commande `code` au PATH est pratique.

Vérifie si la commande est disponible :

```powershell
code --version
```

## 3. Installer les outils sous Linux

Les commandes dépendent de la distribution. Utilise uniquement la section correspondant à ton système.

### 3.1 Arch Linux et Omarchy

```bash
sudo pacman -S --needed git github-cli python python-pip
```

Vérifie les installations :

```bash
git --version
gh --version
python --version
```

Pour Visual Studio Code, tu peux utiliser l'éditeur fourni par ta distribution ou installer la version Microsoft depuis son site officiel. Sur Arch, les paquets et leurs sources peuvent différer : vérifie ce que tu installes et ne lance pas une commande AUR provenant d'un site inconnu.

### 3.2 Debian et Ubuntu

```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

Vérifie :

```bash
git --version
python3 --version
```

Installe ensuite GitHub CLI en suivant la procédure officielle adaptée à ta distribution : [GitHub CLI — Installation](https://github.com/cli/cli#installation). Cela évite d'utiliser un dépôt tiers ou une commande qui ne correspondrait pas à ta version de Debian/Ubuntu.

Pour Visual Studio Code, utilise [le site officiel](https://code.visualstudio.com/).

### 3.3 macOS

Si Homebrew est déjà installé, tu peux installer Git, GitHub CLI et Python avec :

```bash
brew install git gh python
```

Vérifie ensuite :

```bash
git --version
gh --version
python3 --version
```

Si Homebrew n'est pas installé, consulte sa documentation officielle avant de l'installer : [brew.sh](https://brew.sh/). Pour Visual Studio Code, utilise [le site officiel](https://code.visualstudio.com/).

## 4. Configurer son identité Git

Git doit connaître le nom et l'adresse e-mail à inscrire dans les commits. Ces informations permettent de savoir qui a enregistré une modification. **Ce ne sont pas les identifiants de connexion à GitHub.**

Dans un terminal :

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton-adresse@example.com"
```

Remplace les exemples par ton nom et une adresse e-mail vérifiée dans ton compte GitHub. Si tu ne souhaites pas afficher ton adresse personnelle, GitHub propose une adresse `noreply` dans les paramètres du compte, section **Emails**.

Vérifie :

```bash
git config --global --list
```

L'option `--global` signifie que ce réglage s'applique à tous tes dépôts Git sur cet ordinateur. Tu n'as normalement à faire cette configuration qu'une fois.

## 5. Se connecter à GitHub

Pour envoyer des modifications vers GitHub, Git doit pouvoir s'authentifier. On utilise GitHub CLI (`gh`) afin d'éviter de gérer manuellement un token.

### 5.1 Vérifier que GitHub CLI est installé

```bash
gh --version
```

### 5.2 Lancer la connexion

```bash
gh auth login
```

Dans l'assistant :

1. sélectionne **GitHub.com** ;
2. choisis **HTTPS** comme protocole Git ;
3. choisis l'authentification avec un navigateur si elle est proposée ;
4. ouvre le lien affiché et saisis le code temporaire dans le navigateur ;
5. confirme l'autorisation demandée.

Le code affiché est temporaire et personnel : ne le partage avec personne.

### 5.3 Configurer Git pour utiliser cette connexion

Après la connexion, lance :

```bash
gh auth setup-git
```

Cette commande configure Git pour utiliser GitHub CLI comme gestionnaire d'identifiants lors des opérations HTTPS.

Vérifie la connexion :

```bash
gh auth status
```

Tu dois voir le compte GitHub connecté et le protocole HTTPS.

> La connexion à GitHub ne donne pas automatiquement accès à tous les dépôts privés. Pour pouvoir envoyer des modifications à notre dépôt, tu dois avoir accepté l'invitation de collaborateur envoyée par le responsable du projet.

## 6. Récupérer le dépôt du projet

Choisis un dossier de ton ordinateur dans lequel ranger tes projets, puis exécute :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

La commande `git clone` télécharge le dépôt et crée le dossier `projet-nsi`. La commande `cd` entre dans ce dossier.

Vérifie que tout fonctionne :

```bash
git status
git remote -v
```

Tu dois être sur la branche `main`. L'adresse distante doit correspondre à `https://github.com/The-Last-Echo/projet-nsi.git`.

Le dépôt est public : il est possible de le télécharger sans être connecté. En revanche, pour envoyer des commits, tu dois être connecté et avoir les droits nécessaires.

## 7. Ouvrir le projet dans VS Code

Depuis le dossier `projet-nsi` :

```bash
code .
```

Si la commande `code` n'est pas disponible, ouvre VS Code depuis le menu de ton système, puis utilise **File → Open Folder** et sélectionne le dossier `projet-nsi`.

## 8. Extensions VS Code recommandées

Les extensions conseillées par le dépôt sont indiquées dans [`.vscode/extensions.json`](../.vscode/extensions.json). VS Code peut proposer de les installer lorsque tu ouvres le projet. Tu gardes le choix de les installer ou non.

| Extension | Utilité |
|---|---|
| Python (Microsoft) | Exécuter, déboguer et sélectionner l'interpréteur Python. |
| GitLens | Consulter l'historique et comprendre les modifications ligne par ligne. |
| GitHub Pull Requests and Issues | Consulter et relire les PR et Issues dans VS Code. |
| Markdown All in One | Faciliter la rédaction des fichiers Markdown. |

Pour afficher les extensions dans VS Code :

- Windows/Linux : `Ctrl + Shift + X` ;
- recherche le nom de l'extension ;
- vérifie l'éditeur indiqué avant l'installation.

Après avoir installé l'extension Python, ouvre un fichier `.py`, puis lance **Python: Select Interpreter** depuis la palette de commandes (`Ctrl + Shift + P`). Tu pourras sélectionner l'environnement virtuel du projet après l'avoir créé.

## 9. Préparer l'environnement Python

Chaque membre doit créer un environnement virtuel local pour le projet. Il permet d'installer les bibliothèques Python du projet sans les mélanger avec celles des autres projets ou du système.

Suis le [guide de l'environnement Python](PYTHON-ENVIRONMENT.md). Le dossier `.venv/` est déjà exclu du dépôt grâce au `.gitignore` : il ne doit pas être envoyé sur GitHub.

## 10. Vérification finale

Avant de commencer à travailler, vérifie les commandes disponibles :

```bash
git --version
python --version
gh --version
git config --global --list
gh auth status
```

Sur Windows, utilise `py --version` si `python --version` n'est pas reconnu.

Dans le dossier du projet :

```bash
git status
git remote -v
```

Tu dois être sur `main`, avec un dépôt propre, et voir l'adresse GitHub du projet comme dépôt distant.

## 11. Problèmes fréquents

| Message ou problème | Que vérifier ? |
|---|---|
| `git: command not found` ou commande inconnue | Vérifie l'installation de Git, puis ferme et rouvre le terminal. |
| `gh: command not found` | Vérifie l'installation de GitHub CLI et le PATH. |
| `python` n'est pas reconnu sous Windows | Essaie `py --version` ou relance l'installateur Python en vérifiant le lanceur. |
| `Authentication failed` | Lance `gh auth status`, puis reconnecte-toi avec `gh auth login` si nécessaire. |
| `Repository not found` ou accès refusé | Vérifie l'adresse du dépôt et assure-toi d'avoir accepté l'invitation de collaborateur. |
| `Permission denied` pendant un push | Vérifie que tu es connecté au bon compte et que tu as accepté l'invitation. |
| VS Code ne trouve pas Python | Installe l'extension Python puis choisis l'interpréteur avec `Python: Select Interpreter`. |

Si le problème persiste, demande de l'aide à l'équipe avec le message d'erreur complet. Masque les chemins personnels si nécessaire et ne partage jamais de mot de passe, token ou code de connexion.

## Ressources officielles

- [Télécharger Git](https://git-scm.com/downloads)
- [Documentation Git](https://git-scm.com/doc)
- [Installer GitHub CLI](https://github.com/cli/cli#installation)
- [Manuel GitHub CLI](https://cli.github.com/manual/)
- [Télécharger Visual Studio Code](https://code.visualstudio.com/)
- [Documentation Python](https://docs.python.org/3/)
- [Authentification GitHub avec HTTPS](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

