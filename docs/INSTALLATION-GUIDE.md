# Guide d'installation et de configuration

Ce guide accompagne chaque membre dans la préparation de son environnement de développement. Il présente Git, GitHub CLI et Visual Studio Code sous Windows et Linux, avec une attention particulière à Arch Linux.

Les commandes d'installation peuvent évoluer selon les versions des systèmes. En cas de différence, privilégie toujours la documentation officielle de l'outil ou de ta distribution.

## 1. Les outils utilisés dans le projet

| Outil | Rôle |
|---|---|
| Python 3 | Langage utilisé pour développer le jeu. |
| Git | Gestion des versions du code. |
| GitHub | Hébergement du dépôt et collaboration. |
| GitHub CLI (`gh`) | Utiliser les Issues et Pull Requests depuis le terminal. |
| Visual Studio Code | Éditeur recommandé pour le code et la documentation. |

Visual Studio Code est recommandé pour faciliter l'entraide et partager une sélection d'extensions. Il n'est pas obligatoire : chacun peut utiliser un autre éditeur s'il sait suivre le workflow du projet.

## 2. Installer les outils sous Windows

### Git

1. Ouvre [git-scm.com/download/win](https://git-scm.com/download/win).
2. Télécharge l'installateur adapté à ton ordinateur.
3. Lance l'installation. Pour une première utilisation, les options proposées par défaut conviennent généralement.
4. Ouvre un nouveau terminal PowerShell ou Git Bash et vérifie :

```powershell
git --version
```

### GitHub CLI

Si Windows Package Manager (`winget`) est disponible :

```powershell
winget install --id GitHub.cli
```

Ferme puis rouvre le terminal et vérifie :

```powershell
gh --version
```

Tu peux aussi suivre la méthode officielle : [Installation de GitHub CLI](https://github.com/cli/cli#installation).

### Visual Studio Code

1. Télécharge VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/).
2. Lance l'installateur.
3. Pendant l'installation, les options permettant d'ajouter `code` au PATH et d'ouvrir un dossier avec VS Code sont pratiques.
4. Ouvre un nouveau terminal et vérifie, si la commande est disponible :

```powershell
code --version
```

### Python

Télécharge une version prise en charge de Python depuis [python.org](https://www.python.org/downloads/). Pendant l'installation Windows, active l'option permettant d'ajouter Python au PATH si elle est proposée.

Vérifie ensuite :

```powershell
py --version
```

ou :

```powershell
python --version
```

La version minimale requise par le projet sera ajoutée au README lorsqu'elle sera décidée.

## 3. Installer les outils sous Linux

Les commandes dépendent de la distribution. La section suivante donne des exemples pour Arch Linux et les distributions basées sur Debian/Ubuntu.

### Arch Linux et distributions dérivées

Installe Git et GitHub CLI avec `pacman` :

```bash
sudo pacman -S --needed git github-cli
```

Pour Visual Studio Code, deux possibilités courantes existent :

- installer la version Code - OSS proposée par les dépôts de ta distribution, si elle te convient ;
- installer la version Microsoft de Visual Studio Code depuis le site officiel ou depuis une source de paquets fiable adaptée à Arch Linux.

Sur une installation utilisant un helper AUR comme `yay`, le paquet `visual-studio-code-bin` est une possibilité :

```bash
yay -S visual-studio-code-bin
```

Cette dernière commande suppose que `yay` est déjà installé. N'installe pas un helper AUR uniquement en copiant une commande trouvée au hasard : vérifie d'abord sa provenance et son fonctionnement.

Python 3 est généralement disponible dans les dépôts :

```bash
sudo pacman -S --needed python
```

Vérifie les installations :

```bash
git --version
gh --version
python --version
code --version
```

La commande `code` dépend du paquet installé. Avec certaines distributions Code - OSS, l'accès au Visual Studio Marketplace peut différer de celui de la version Microsoft. Si une extension n'apparaît pas, vérifie la distribution de l'éditeur et la documentation de celle-ci.

### Debian et Ubuntu

Git et Python sont disponibles dans les dépôts :

```bash
sudo apt update
sudo apt install git python3
```

Pour GitHub CLI, suis la procédure officielle adaptée à ta version de distribution : [GitHub CLI — Installation](https://github.com/cli/cli#installation).

Pour Visual Studio Code, utilise le paquet officiel Microsoft ou la méthode recommandée sur [code.visualstudio.com](https://code.visualstudio.com/).

## 4. Configurer Git

Git doit connaître le nom et l'adresse e-mail à inscrire dans les commits. Ces informations ne sont pas ton mot de passe GitHub.

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

Utilise une adresse vérifiée dans les paramètres de ton compte GitHub. Si tu souhaites préserver ton adresse personnelle, GitHub peut fournir une adresse `noreply` dans les paramètres de confidentialité de l'adresse e-mail.

Vérifie la configuration :

```bash
git config --global --list
```

Pour examiner la valeur d'un paramètre et son fichier d'origine :

```bash
git config --show-origin --get user.email
```

## 5. Se connecter à GitHub en HTTPS

Le projet utilise une URL distante HTTPS. GitHub n'accepte pas le mot de passe du compte comme mot de passe Git pour les opérations HTTPS.

La méthode recommandée pour commencer est GitHub CLI :

```bash
gh auth login
```

Dans l'assistant :

1. sélectionne `GitHub.com` ;
2. choisis `HTTPS` ;
3. accepte l'authentification Git avec les identifiants GitHub si la question est proposée ;
4. termine la connexion dans le navigateur.

Vérifie ensuite :

```bash
gh auth status
```

Une autre possibilité est d'utiliser un gestionnaire d'identifiants compatible avec Git et OAuth, comme Git Credential Manager. Il n'est pas nécessaire de configurer plusieurs solutions simultanément pour ce projet.

**Sécurité :** ne place jamais un token dans un fichier suivi par Git, une commande conservée dans un script, une Issue, une Pull Request, Discord ou une capture d'écran. N'envoie jamais tes identifiants à un autre membre.

## 6. Installer et ouvrir le projet dans VS Code

Clone le dépôt :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

Ouvre le dossier dans VS Code :

```bash
code .
```

Si la commande `code` n'est pas disponible, ouvre VS Code depuis le menu de ton système, puis utilise **File → Open Folder** pour sélectionner le dossier `projet-nsi`.

## 7. Extensions VS Code recommandées

Les extensions proposées par le dépôt sont répertoriées dans [`.vscode/extensions.json`](../.vscode/extensions.json). VS Code peut afficher une notification pour les installer. Ces recommandations ne les installent pas de force : chaque utilisateur garde le contrôle.

Pour ouvrir le panneau des extensions :

- Windows/Linux : `Ctrl + Shift + X` ;
- recherche une extension par son nom ;
- vérifie son éditeur et sa page Marketplace avant de l'installer.

### Python — Microsoft

**À installer.** Cette extension ajoute notamment l'exécution, le débogage, la sélection de l'interpréteur Python et l'intégration des tests.

Après installation :

1. ouvre un fichier `.py` ;
2. ouvre la palette de commandes avec `Ctrl + Shift + P` ;
3. lance `Python: Select Interpreter` ;
4. sélectionne l'interpréteur ou l'environnement virtuel du projet.

Marketplace : [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

### Pylance — Microsoft

Pylance fournit l'analyse du code, l'autocomplétion et la navigation dans les symboles Python. L'extension Python installe généralement Pylance comme extension associée ; vérifie sa présence avant de l'installer séparément.

Marketplace : [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).

### GitLens

**Fortement recommandée.** GitLens aide à comprendre l'historique du code : auteur d'une ligne (*blame*), historique d'un fichier, comparaison de commits et graphe des branches.

Pour commencer :

1. ouvre un fichier suivi par Git ;
2. utilise les annotations GitLens pour voir quel commit a modifié une ligne ;
3. ouvre la vue GitLens dans la barre latérale pour consulter l'historique et le graphe.

Ces informations aident à comprendre une modification, mais ne remplacent pas la lecture du code ni la review.

Marketplace : [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

### GitHub Pull Requests and Issues

**Recommandée pour les personnes qui relisent ou suivent des PR.** Elle permet de consulter les Pull Requests et Issues depuis VS Code, d'examiner les fichiers modifiés et de commenter les lignes.

Après connexion à GitHub, ouvre la vue GitHub Pull Requests dans la barre latérale et sélectionne une Pull Request à examiner.

Marketplace : [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github).

### Markdown All in One

**Recommandée pour la documentation.** Elle facilite l'écriture de fichiers Markdown : listes, raccourcis et tables des matières.

Marketplace : [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one).

### Ruff

**À adopter lorsque les conventions Python de l'équipe seront décidées.** Ruff peut signaler des problèmes de style, certains imports inutilisés et formater le code. Il ne faut pas laisser chaque membre appliquer des règles différentes : sa configuration devra être partagée dans le dépôt avant de devenir une règle commune.

Marketplace : [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

### Git Graph — facultative

GitLens couvre déjà une bonne partie de la visualisation de l'historique. Git Graph est une alternative si quelqu'un préfère une vue graphique dédiée des branches et commits. Il n'est pas nécessaire d'installer les deux.

Marketplace : [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph).

## 8. Tester l'installation

Exécute les commandes suivantes :

```bash
git --version
gh --version
python --version
git config --global --list
gh auth status
```

Puis vérifie que le dépôt est accessible :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
git status
```

Le résultat de `git status` doit indiquer que tu es sur `main` et que l'arbre de travail est propre si tu n'as pas encore modifié de fichier.

## 9. Problèmes courants

| Problème | Piste de résolution |
|---|---|
| `git: command not found` | Vérifie l'installation de Git et ouvre un nouveau terminal. |
| `gh: command not found` | Vérifie l'installation de GitHub CLI et le PATH. |
| `Authentication failed` | Relance `gh auth login`, puis `gh auth status`. |
| `Repository not found` | Vérifie l'URL, l'orthographe du dépôt et l'acceptation de ton invitation. |
| VS Code ne trouve pas Python | Lance `Python: Select Interpreter` et sélectionne le bon interpréteur. |
| Une extension est introuvable | Vérifie si tu utilises Microsoft VS Code ou une distribution Code - OSS, puis consulte la page de l'extension. |

Si le problème persiste, copie le message d'erreur en masquant les éventuels chemins personnels ou informations sensibles et demande de l'aide à l'équipe.

## Ressources officielles et pour aller plus loin

- [Télécharger Git](https://git-scm.com/downloads)
- [Documentation Git](https://git-scm.com/doc)
- [Installer GitHub CLI](https://github.com/cli/cli#installation)
- [Manuel GitHub CLI](https://cli.github.com/manual/)
- [Télécharger Visual Studio Code](https://code.visualstudio.com/)
- [Documentation VS Code — Extensions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
- [Documentation Python](https://docs.python.org/3/)
- [GitHub — gestion des identifiants avec HTTPS](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

*Dernière vérification des liens et des procédures : novembre 2026. Les commandes d'installation dépendent de la distribution et de ses dépôts.*
