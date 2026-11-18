# Guide Git — comprendre les bases et les commandes utiles

Ce guide s'adresse aux membres qui découvrent Git. Il explique les notions essentielles, puis présente les commandes utilisées dans le projet.

Pour connaître l'ordre exact des étapes à suivre en équipe, consulte le [guide de collaboration](COLLABORATION-GUIDE.md).

> **À retenir :** Git enregistre l'historique des fichiers sur ton ordinateur. GitHub héberge le dépôt en ligne et ajoute des outils pour collaborer. Git et GitHub sont liés, mais ce ne sont pas la même chose.

## 1. Les notions essentielles

| Terme | Explication simple |
|---|---|
| Dépôt (*repository*) | Le projet et son historique suivis par Git. |
| Dépôt local | La copie du projet sur ton ordinateur. |
| Dépôt distant (*remote*) | La copie du projet hébergée sur GitHub. |
| `origin` | Le nom donné par défaut au dépôt distant principal. |
| Commit | Un ensemble de changements enregistré dans l'historique. |
| Branche (*branch*) | Une ligne de travail séparée, qui permet de développer sans modifier directement `main`. |
| Pull Request (PR) | Une proposition de changement à relire avant de l'intégrer dans `main`. |
| Push | Envoyer tes commits vers GitHub. |
| Pull | Récupérer les changements distants et les intégrer dans ta branche. |

Git peut être utilisé sans Internet. Une connexion est nécessaire pour échanger des modifications avec GitHub.

## 2. Vérifier et configurer Git

Vérifie que Git est installé :

```bash
git --version
```

Configure ton nom et ton adresse e-mail une seule fois sur ton ordinateur :

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton-adresse@example.com"
```

Ces deux informations seront enregistrées dans tes commits. **Elles ne servent pas à te connecter à GitHub.** Utilise une adresse vérifiée sur GitHub, ou l'adresse `noreply` proposée dans les paramètres de ton compte si tu ne veux pas afficher ton adresse personnelle.

Pour afficher la configuration :

```bash
git config --global --list
```

Pour connaître l'origine d'un paramètre :

```bash
git config --show-origin --get user.email
```

La procédure complète d'installation et de connexion est dans le [guide d'installation](INSTALLATION-GUIDE.md).

## 3. Compatibilité Windows / Linux / macOS

Les membres peuvent utiliser des systèmes différents. Le dépôt contient un fichier `.gitattributes` qui aide Git à normaliser les fins de ligne des fichiers texte. Cela évite que le passage de Windows à Linux ou macOS crée des différences inutiles dans les Pull Requests.

Ne modifie pas les fins de ligne manuellement si ton éditeur propose une option automatique.

## 4. Récupérer le projet pour la première fois

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

- `git clone` télécharge une copie du dépôt et crée le dossier `projet-nsi`.
- `cd projet-nsi` entre dans ce dossier.

Pour vérifier l'adresse du dépôt distant :

```bash
git remote -v
```

Tu dois normalement voir l'adresse GitHub du projet sous le nom `origin`.

Le dépôt étant public, le téléchargement peut fonctionner sans être connecté. En revanche, pour envoyer des modifications, il faut être connecté à GitHub et avoir les droits de collaborateur.

## 5. Vérifier l'état de son travail

La commande à connaître en priorité est :

```bash
git status
```

Elle indique notamment :

- la branche actuellement sélectionnée ;
- les fichiers modifiés ;
- les fichiers prêts à être enregistrés dans le prochain commit ;
- les fichiers non suivis par Git.

Pour une version plus courte :

```bash
git status -sb
```

## 6. Comprendre `git add` et `git commit`

Avant un commit, Git distingue trois zones :

1. **Répertoire de travail** : les fichiers que tu modifies.
2. **Zone de préparation (*staging area*)** : les modifications sélectionnées pour le prochain commit.
3. **Historique** : les commits déjà enregistrés.

Le fonctionnement habituel est : modifier un fichier, le préparer avec `git add`, puis enregistrer le commit avec `git commit`.

### Voir les modifications

```bash
git diff
```

Affiche les modifications qui ne sont pas encore préparées.

```bash
git diff --staged
```

Affiche ce qui est déjà préparé pour le prochain commit.

### Ajouter les fichiers souhaités

```bash
git add README.md
git add src/player.py
```

Ajoute un ou plusieurs fichiers précis.

```bash
git add .
```

Ajoute les modifications du dossier courant et de ses sous-dossiers. Cette commande est pratique, mais vérifie toujours `git status` et `git diff --staged` avant de créer le commit.

### Créer le commit

```bash
git commit -m "feat(player): add player movement"
```

Un commit enregistre les changements préparés dans l'historique local. **Il n'envoie rien sur GitHub** : c'est le rôle de `git push`.

## 7. Convention des messages de commit

Le projet utilise une convention appelée **Conventional Commits**. Les messages sont rédigés en anglais selon ce format :

```text
<type>(<scope>): <description courte>
```

Le `scope` entre parenthèses est facultatif. Il indique la partie du projet concernée.

| Type | Quand l'utiliser | Exemple |
|---|---|---|
| `feat` | Ajouter une fonctionnalité | `feat(grid): display the game grid` |
| `fix` | Corriger un bug | `fix(player): prevent invalid movement` |
| `docs` | Modifier la documentation | `docs(git): explain branch workflow` |
| `refactor` | Réorganiser le code sans changer le résultat attendu | `refactor(grid): simplify cell lookup` |
| `test` | Ajouter ou modifier des tests | `test(player): cover movement limits` |
| `chore` | Maintenance et tâches techniques | `chore: update development tools` |
| `style` | Mise en forme sans changer la logique | `style: format Python files` |

Évite les messages vagues comme `update`, `fix` ou `changes`.

## 8. Travailler avec des branches

Une branche permet de développer une modification sans toucher directement à `main`.

Afficher les branches locales :

```bash
git branch
```

Créer une branche et basculer dessus :

```bash
git switch -c feature/player-movement
```

Changer de branche :

```bash
git switch main
```

Dans ce projet, les préfixes sont :

- `feature/` : nouvelle fonctionnalité ;
- `fix/` : correction ;
- `docs/` : documentation ;
- `refactor/` : réorganisation interne.

Crée toujours ta branche depuis `main` à jour. Ne commence pas une nouvelle tâche avec des modifications non enregistrées qui appartiennent à une autre tâche.

## 9. Échanger des changements avec GitHub

Ces trois commandes ont des rôles différents.

### `git fetch` — regarder ce qui a changé en ligne

```bash
git fetch origin
```

Récupère les informations et commits du dépôt distant, sans modifier automatiquement les fichiers de ta branche actuelle.

### `git pull` — mettre à jour sa branche

```bash
git pull --ff-only
```

Récupère les changements distants et met à jour la branche locale uniquement si Git peut avancer sans créer de commit de fusion. Dans notre workflow, cette commande sert notamment à mettre `main` à jour.

Si elle échoue, ne lance pas `git reset --hard` au hasard. Regarde `git status` et demande de l'aide si tu ne comprends pas la situation.

### `git push` — envoyer ses commits

Pour le premier envoi d'une branche :

```bash
git push -u origin feature/player-movement
```

`origin` désigne le dépôt distant. Le nom après `origin` est la branche à envoyer. `-u` mémorise la relation entre la branche locale et la branche distante ; les prochains envois peuvent généralement se faire avec `git push`.

## 10. Lire l'historique

```bash
git log --oneline
```

Affiche les commits sous une forme compacte.

```bash
git log --oneline --graph --decorate --all
```

Affiche les commits et les branches sous forme de graphe textuel.

Pour afficher le détail d'un commit :

```bash
git show IDENTIFIANT_DU_COMMIT
```

Remplace `IDENTIFIANT_DU_COMMIT` par l'identifiant affiché dans `git log`.

## 11. Annuler une modification : prudence

Certaines commandes peuvent faire perdre du travail. Lis bien leur effet avant de les utiliser.

Retirer un fichier de la zone de préparation sans supprimer ses modifications :

```bash
git restore --staged chemin/du/fichier
```

Abandonner les modifications locales non enregistrées d'un fichier :

```bash
git restore chemin/du/fichier
```

La deuxième commande peut faire perdre les modifications de ce fichier. Ne l'utilise que si tu es certain de ne pas en avoir besoin.

Pour annuler un commit déjà partagé, on utilise généralement `git revert`, qui crée un nouveau commit annulant les changements :

```bash
git revert IDENTIFIANT_DU_COMMIT
```

Évite `git reset --hard`, `git clean -fd` et `git push --force` dans le cadre du projet. Ces commandes peuvent supprimer du travail ou réécrire un historique partagé.

## 12. Après la fusion d'une Pull Request

La PR est fusionnée sur GitHub avec **Squash and merge**. Cette méthode regroupe les commits de la branche dans un nouveau commit sur `main`.

Après avoir vérifié que la PR est indiquée comme **Merged** sur GitHub :

```bash
git switch main
git pull --ff-only
git branch -D feature/player-movement
```

`-D` force la suppression de la branche locale. Avec Squash and merge, `git branch -d` peut refuser de supprimer une branche parce que ses anciens commits ne sont pas les mêmes que le commit squashé sur `main`. Utilise `-D` uniquement après avoir vérifié que la PR est bien fusionnée et qu'il ne reste aucun travail à conserver sur cette branche.

GitHub peut supprimer automatiquement la branche distante après la fusion si cette option est activée dans les paramètres du dépôt.

## 13. Authentification GitHub en HTTPS

GitHub n'accepte pas le mot de passe de ton compte comme mot de passe Git en HTTPS. Pour ce projet, on utilise GitHub CLI (`gh`) pour se connecter.

```bash
gh auth login
```

Choisis `GitHub.com`, le protocole `HTTPS` et l'authentification par navigateur lorsque l'assistant le propose. Puis configure Git pour utiliser GitHub CLI comme gestionnaire d'identifiants :

```bash
gh auth setup-git
```

Vérifie la connexion :

```bash
gh auth status
```

Ne partage jamais de token, mot de passe ou code de connexion. Le [guide d'installation](INSTALLATION-GUIDE.md) détaille cette procédure.

## 14. Les commandes à retenir

Voici le cycle le plus fréquent :

```bash
# Récupérer le projet (une seule fois)
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi

# Au début d'une nouvelle tâche
git status
git switch main
git pull --ff-only
git switch -c feature/short-description

# Après avoir modifié les fichiers
git status
git diff
git add chemin/du/fichier
git diff --staged
git commit -m "feat(scope): describe the change"

# Envoyer la branche sur GitHub
git push -u origin feature/short-description
```

Ensuite, ouvre une Pull Request sur GitHub vers `main`, fais relire les modifications, effectue les corrections demandées et laisse le responsable de l'intégration réaliser le Squash and merge.

## Ressources

- [Documentation officielle de Git](https://git-scm.com/doc)
- [Livre Pro Git, en français](https://git-scm.com/book/fr/v2)
- [Référence des commandes Git](https://git-scm.com/docs)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Documentation GitHub CLI](https://cli.github.com/manual/)
