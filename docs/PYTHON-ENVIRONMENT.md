# Guide Python — créer et utiliser un environnement virtuel

Ce guide explique comment créer un environnement virtuel Python pour le projet.

Il est important que chaque membre utilise un environnement séparé : cela évite de mélanger les bibliothèques du jeu avec celles installées pour d'autres projets ou directement sur l'ordinateur.

## 1. Pourquoi utiliser un environnement virtuel ?

Un environnement virtuel est un dossier qui contient un environnement Python isolé pour un projet.

Sans environnement virtuel, les bibliothèques installées peuvent se mélanger entre plusieurs projets. Une mise à jour faite pour un projet peut alors casser un autre projet.

Avec un environnement virtuel :

- les bibliothèques installées pour le projet restent dans le dossier `.venv/` ;
- chaque membre peut préparer son propre environnement ;
- les bibliothèques du projet ne modifient pas l'installation Python générale de l'ordinateur ;
- le projet peut lister ses dépendances dans un fichier partagé comme `requirements.txt`.

**Attention :** un environnement virtuel ne garantit pas à lui seul que deux ordinateurs utilisent exactement la même version de Python. L'équipe devra aussi choisir une version de Python commune et documenter les bibliothèques nécessaires.

## 2. Avant de commencer

Il faut avoir installé Python 3 et avoir cloné le dépôt.

Place-toi dans le dossier du projet :

```bash
cd chemin/vers/projet-nsi
```

Vérifie Python :

```bash
python --version
```

Sous certaines distributions Linux, la commande est plutôt :

```bash
python3 --version
```

Sous Windows, le lanceur `py` fonctionne généralement :

```powershell
py --version
```

## 3. Créer l'environnement virtuel

Nous utilisons le nom `.venv` pour le dossier de l'environnement. Il doit être créé à la racine du dépôt, au même niveau que `README.md`.

### Windows — PowerShell

```powershell
py -m venv .venv
```

### Windows — Invite de commandes (cmd)

```cmd
py -m venv .venv
```

### Linux et macOS

```bash
python3 -m venv .venv
```

Si la commande indique que le module `venv` est indisponible sous Debian ou Ubuntu, installe le paquet correspondant :

```bash
sudo apt update
sudo apt install python3-venv
```

Puis relance la création de l'environnement.

## 4. Activer l'environnement virtuel

La création et l'activation sont deux étapes différentes. Il faut activer l'environnement dans chaque nouveau terminal utilisé pour travailler sur le projet.

### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque le script à cause de la politique d'exécution, tu peux autoriser les scripts pour **ce terminal uniquement** :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Puis relance la commande d'activation. Cette autorisation disparaît lorsque tu fermes le terminal. Ne change pas la politique d'exécution de tout l'ordinateur pour ce projet. Si l'ordinateur est géré par l'établissement et que cette opération est bloquée, ne cherche pas à contourner sa politique : tu peux utiliser directement l'interpréteur de l'environnement, par exemple `.\.venv\Scripts\python.exe -m pip --version` dans PowerShell, sans activer l'environnement.

### Windows — Invite de commandes (cmd)

```cmd
.venv\Scripts\activate.bat
```

### Linux et macOS

```bash
source .venv/bin/activate
```

Lorsque l'environnement est actif, le nom `(.venv)` apparaît généralement au début de la ligne de commande.

## 5. Vérifier que l'environnement est actif

Exécute :

```bash
python --version
python -m pip --version
```

Tu peux aussi vérifier le chemin de l'interpréteur :

### Windows — PowerShell

```powershell
(Get-Command python).Source
```

Le chemin affiché doit pointer vers le dossier `.venv` du projet.

### Linux et macOS

```bash
which python
```

Le chemin affiché doit également contenir `.venv`.

## 6. Installer les bibliothèques du projet

Quand le projet utilisera des bibliothèques externes, elles seront listées dans un fichier partagé `requirements.txt` à la racine du dépôt.

Une fois l'environnement activé, mets à jour l'outil d'installation :

```bash
python -m pip install --upgrade pip
```

Puis installe les dépendances listées dans le fichier :

```bash
python -m pip install -r requirements.txt
```

Pour l'instant, le projet n'a pas encore de code ni de dépendances définies. Il est donc normal que `requirements.txt` ne soit pas encore présent. N'invente pas de dépendances et n'en installe pas au hasard.

### Quand l'équipe ajoutera une bibliothèque

La personne qui ajoute une nouvelle dépendance devra :

1. l'installer dans son environnement `.venv` ;
2. vérifier que le projet fonctionne ;
3. mettre à jour `requirements.txt` avec les dépendances et versions nécessaires ;
4. envoyer ce fichier avec sa Pull Request.

Pour afficher les bibliothèques installées dans l'environnement :

```bash
python -m pip list
```

Pour produire une liste des versions installées :

```bash
python -m pip freeze
```

La sortie de `pip freeze` peut servir à mettre à jour `requirements.txt`, mais relis le résultat avant de l'envoyer : le fichier doit contenir les dépendances nécessaires au projet, pas des bibliothèques installées par erreur.

## 7. Utiliser l'environnement dans VS Code

1. Ouvre le dossier `projet-nsi` dans VS Code.
2. Vérifie que l'extension Python de Microsoft est installée.
3. Ouvre la palette de commandes avec `Ctrl + Shift + P`.
4. Recherche **Python: Select Interpreter**.
5. Sélectionne l'interpréteur situé dans `.venv`.

Si `.venv` n'apparaît pas, ferme et rouvre le dossier ou utilise l'option permettant de saisir le chemin de l'interpréteur.

## 8. Désactiver l'environnement

Quand tu as terminé, tu peux quitter l'environnement virtuel avec :

```bash
deactivate
```

Cela ne supprime pas l'environnement. Il sera toujours présent lorsque tu reviendras sur le projet.

## 9. Faut-il envoyer `.venv` sur GitHub ?

**Non.** Le dossier `.venv/` est propre à chaque ordinateur. Il peut être volumineux et contient des fichiers générés par Python.

Il est déjà exclu dans le fichier `.gitignore` du projet. Il ne doit jamais être ajouté à une Pull Request.

On partage le fichier `requirements.txt`, pas le dossier `.venv`.

Pour vérifier qu'il n'est pas suivi par Git :

```bash
git status --short
```

Si `.venv/` apparaît malgré tout, arrête-toi et demande de l'aide avant de forcer son ajout ou sa suppression.

## 10. Recréer son environnement en cas de problème

Si l'environnement est cassé ou incohérent, il est souvent plus simple de le recréer. Avant de le supprimer, assure-toi qu'il ne contient pas de fichier personnel à conserver : `.venv/` doit uniquement contenir l'environnement Python généré.

1. Désactive l'environnement si celui-ci est actif :

```bash
deactivate
```

2. Supprime le dossier `.venv/` depuis l'explorateur de fichiers ou avec la commande adaptée à ton système.

3. Recommence les étapes **3. Créer l'environnement virtuel**, **4. Activer l'environnement virtuel** et **6. Installer les bibliothèques du projet**.

## Checklist rapide

- [ ] Je suis dans le dossier `projet-nsi`.
- [ ] J'ai créé `.venv` à la racine du dépôt.
- [ ] J'ai activé l'environnement virtuel dans mon terminal.
- [ ] VS Code utilise l'interpréteur situé dans `.venv`.
- [ ] J'ai installé `requirements.txt` s'il existe.
- [ ] Je n'ajoute jamais le dossier `.venv` à Git.

## Ressources officielles

- [Documentation Python — `venv`](https://docs.python.org/3/library/venv.html)
- [Documentation Python — installation des paquets avec `pip`](https://docs.python.org/3/installing/index.html)
