# Guide Git — comprendre et utiliser les commandes essentielles

Ce guide présente les bases de Git et les commandes qui seront utiles pendant le projet. Il s'adresse aux personnes qui découvrent Git comme à celles qui souhaitent retrouver rapidement une commande.

Il ne remplace pas le [guide de collaboration](COLLABORATION-GUIDE.md), qui explique la procédure propre à notre équipe.

> **À retenir :** Git est l'outil qui suit l'évolution des fichiers sur ton ordinateur. GitHub héberge une copie distante du dépôt et ajoute des outils de collaboration autour de Git.

## 1. Git, GitHub et un dépôt

### Git et GitHub : quelle différence ?

- **Git** est un logiciel de gestion de versions. Il conserve l'historique des modifications et permet de travailler sur plusieurs branches.
- **GitHub** est une plateforme d'hébergement et de collaboration. Elle permet notamment de partager un dépôt Git, de créer des Issues et de faire relire des Pull Requests.

Git peut fonctionner sans connexion à Internet. La connexion devient nécessaire pour échanger les modifications avec GitHub.

### Dépôt local et dépôt distant

Le **dépôt local** est la copie du projet présente sur ton ordinateur. Le **dépôt distant** est la copie hébergée sur GitHub. Dans notre projet, le dépôt distant principal est `origin`, et la branche principale s'appelle `main`.

Quelques termes utiles :

- *commit* : un point enregistré dans l'historique ;
- *branch* : une ligne de développement indépendante ;
- *remote* : un dépôt distant configuré ;
- *working tree* : les fichiers sur lesquels tu travailles actuellement.

## 2. Installer et vérifier Git

Vérifie que Git est installé :

```bash
git --version
```

Configure ton identité une seule fois sur ton ordinateur :

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

L'adresse doit être une adresse vérifiée associée à ton compte GitHub. Tu peux aussi utiliser l'adresse `noreply` fournie par GitHub si tu ne souhaites pas exposer ton adresse personnelle dans les commits.

Pour consulter la configuration :

```bash
git config --global --list
```

`user.name` et `user.email` indiquent l'identité inscrite dans les commits. Ils ne servent pas à authentifier ton compte GitHub.

## 3. Cloner le dépôt

Pour récupérer une copie du projet sur ton ordinateur :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

`git clone` crée un dossier, télécharge les fichiers et configure généralement le dépôt distant sous le nom `origin`.

Pour vérifier le dépôt distant :

```bash
git remote -v
```

## 4. Comprendre les trois zones de travail

Git distingue trois zones qu'il est important de comprendre :

1. **Working directory** : les fichiers que tu modifies.
2. **Staging area** (*index*) : les changements que tu as sélectionnés pour le prochain commit.
3. **Repository** : l'historique des commits déjà enregistrés.

Le déroulement classique est donc : modifier un fichier, sélectionner les changements avec `git add`, puis les enregistrer avec `git commit`.

### Vérifier l'état du dépôt

```bash
git status
```

C'est l'une des commandes les plus utiles. Elle indique notamment les fichiers modifiés, les fichiers préparés pour le prochain commit et la branche active.

### Examiner les différences

```bash
git diff
```

Affiche les modifications qui ne sont pas encore dans la staging area.

```bash
git diff --staged
```

Affiche les changements déjà préparés pour le prochain commit. Prends l'habitude de l'exécuter avant un commit.

### Ajouter des fichiers à la staging area

```bash
git add src/player.py
```

Ajoute un fichier précis à la staging area.

```bash
git add .
```

Ajoute les modifications du répertoire courant et de ses sous-répertoires. Cette commande est pratique, mais vérifie toujours `git status` et `git diff --staged` pour éviter d'inclure des fichiers non souhaités.

### Créer un commit

```bash
git commit -m "feat(player): add player movement"
```

Un commit enregistre un ensemble cohérent de changements dans l'historique local. Un commit n'est pas la même chose qu'un push : il peut exister localement sans avoir été envoyé sur GitHub.

## 5. Écrire des messages Conventional Commits

Le projet utilise des messages en anglais selon la structure suivante :

```text
<type>(<scope>): <short description>
```

Le scope est facultatif, mais utile lorsqu'il précise la partie concernée.

| Type | Utilisation | Exemple |
|---|---|---|
| `feat` | Ajouter une fonctionnalité | `feat(grid): add grid rendering` |
| `fix` | Corriger un bug | `fix(player): prevent invalid coordinates` |
| `docs` | Modifier la documentation | `docs(git): clarify branch workflow` |
| `refactor` | Réorganiser le code sans changer le comportement attendu | `refactor(grid): simplify cell lookup` |
| `test` | Ajouter ou modifier des tests | `test(player): cover movement boundaries` |
| `chore` | Maintenance et tâches techniques | `chore: update development tools` |
| `style` | Modifications de présentation sans changement de logique | `style: normalize Python formatting` |

Écris une description courte, claire et en anglais. Évite les messages vagues comme `update`, `fix` ou `changes`.

Référence : [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## 6. Comprendre les branches

Une branche permet de travailler sur une modification sans changer directement la branche principale.

Dans ce projet, les branches de travail commencent par l'un des préfixes suivants :

- `feature/` pour une fonctionnalité ;
- `fix/` pour une correction ;
- `docs/` pour la documentation ;
- `refactor/` pour une refactorisation.

Afficher les branches :

```bash
git branch
```

Créer et sélectionner une branche :

```bash
git switch -c feature/short-description
```

Changer de branche :

```bash
git switch main
```

Supprimer une branche locale déjà fusionnée :

```bash
git branch -d feature/short-description
```

Si Git refuse de supprimer la branche, il peut rester des commits non fusionnés. Ne remplace pas automatiquement `-d` par `-D` : vérifie d'abord ce que tu risques de supprimer.

## 7. Échanger avec le dépôt distant

### `git fetch`

```bash
git fetch origin
```

Récupère les informations et les nouveaux commits du dépôt distant, sans intégrer automatiquement ces changements dans ta branche actuelle.

### `git pull`

```bash
git pull --ff-only
```

Récupère les changements distants et met à jour la branche locale uniquement si une avance rapide est possible. Cette option évite de créer automatiquement un commit de fusion en cas d'histoires divergentes.

Dans le workflow du projet, utilise `git pull --ff-only` lorsque tu mets à jour `main`. Si Git refuse l'opération, ne tente pas un `reset` au hasard : vérifie `git status`, conserve tes changements et demande de l'aide si nécessaire.

### `git push`

```bash
git push -u origin feature/short-description
```

Envoie les commits de ta branche locale vers GitHub. L'option `-u` configure le suivi de la branche distante pour simplifier les prochains `git push` et `git pull`.

## 8. Consulter l'historique

```bash
git log --oneline
```

Affiche l'historique sous une forme compacte.

```bash
git log --oneline --graph --decorate --all
```

Affiche les branches et les relations entre les commits sous forme de graphe textuel.

```bash
git show <commit>
```

Affiche le détail d'un commit donné. Remplace `<commit>` par son identifiant ou une référence reconnue par Git.

## 9. Fusion et conflits

Une fusion (*merge*) rassemble des changements provenant de branches différentes. Dans notre projet, les contributions destinées à `main` sont fusionnées via une Pull Request GitHub, en utilisant **Squash and merge**. Les contributeurs n'ont donc pas à fusionner eux-mêmes leur branche dans `main`.

Un **conflit** apparaît lorsque Git ne peut pas combiner automatiquement certaines modifications. Il faut alors ouvrir les fichiers concernés, comprendre les deux versions, choisir ou réécrire le contenu correct, puis vérifier le résultat.

Après résolution :

```bash
git status
git add chemin/du/fichier
git commit
```

Les commandes exactes dépendent de l'opération en cours. Si tu n'es pas certain de l'état de Git, demande de l'aide avant de continuer.

## 10. Annuler ou corriger une modification

Ces commandes n'ont pas toutes le même effet.

### Annuler les modifications locales d'un fichier non préparé

```bash
git restore chemin/du/fichier
```

Cette commande abandonne les changements locaux non commités du fichier ciblé. Ils peuvent être perdus.

### Retirer un fichier de la staging area

```bash
git restore --staged chemin/du/fichier
```

Le fichier reste modifié dans le répertoire de travail ; il est simplement retiré de la prochaine préparation de commit.

### Annuler un commit déjà partagé

Pour annuler l'effet d'un commit qui a déjà été envoyé ou intégré, `git revert` crée un nouveau commit inverse :

```bash
git revert <commit>
```

Cela préserve l'historique existant.

> **Attention — commandes destructrices :** `git reset --hard`, `git clean -fd` et `git push --force` peuvent supprimer des changements ou réécrire un historique partagé. Ne les utilise pas dans le cadre du projet sans avoir compris leur effet et obtenu l'aide du responsable du dépôt.

## 11. Authentification HTTPS

GitHub n'accepte plus le mot de passe du compte comme mot de passe Git lors d'une opération HTTPS. Pour ce projet, le plus simple est d'utiliser GitHub CLI :

```bash
gh auth login
```

Choisis GitHub.com, HTTPS et l'authentification via navigateur lorsque l'assistant le propose. Vérifie ensuite :

```bash
gh auth status
```

Ne colle jamais un token dans un fichier du dépôt, une Issue, une Pull Request, Discord ou une capture d'écran.

## 12. Quelques habitudes utiles

Avant de commencer une tâche :

```bash
git status
git switch main
git pull --ff-only
```

Avant de créer un commit :

```bash
git status
git diff
git diff --staged
```

Après une fusion :

```bash
git switch main
git pull --ff-only
git branch -d feature/short-description
```

Pour le déroulement complet, suis le [guide de collaboration](COLLABORATION-GUIDE.md).

## Ressources officielles et pour aller plus loin

- [Documentation officielle de Git](https://git-scm.com/doc)
- [Livre Pro Git — gratuit en ligne](https://git-scm.com/book/fr/v2)
- [Référence des commandes Git](https://git-scm.com/docs)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Documentation GitHub sur les dépôts](https://docs.github.com/en/repositories)

*Dernière vérification des liens et des procédures : novembre 2026. Les commandes restent à adapter si l'équipe fait évoluer son workflow.*
