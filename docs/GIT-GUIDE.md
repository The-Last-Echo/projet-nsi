# Guide Git et GitHub

Ce guide résume les commandes utiles au quotidien. Il complète `CONTRIBUTING.md`.

## Vérifier son installation

```bash
git --version
git config --global --list
```

Configurer son identité (à faire une seule fois sur la machine) :

```bash
git config --global user.name "Votre nom ou pseudo"
git config --global user.email "adresse-associee-a-GitHub"
```

Utiliser une adresse e-mail vérifiée sur GitHub ou l'adresse `noreply` fournie dans les paramètres GitHub si vous souhaitez préserver votre adresse personnelle.

## Cloner le dépôt

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

## Les commandes courantes

```bash
git status                 # état des fichiers
git add fichier.py         # préparer un fichier
git add .                  # préparer toutes les modifications du dossier
git commit -m "message"    # créer un commit
git push                   # envoyer les commits
git pull                   # récupérer et intégrer les changements
git log --oneline          # historique compact
git diff                   # voir les modifications non préparées
```

## Workflow conseillé

```bash
git switch main
git pull
git switch -c feature/ma-fonctionnalite

# modifier les fichiers
git status
git add .
git commit -m "feat: décrit la fonctionnalité"
git push -u origin feature/ma-fonctionnalite
```

Créer ensuite une Pull Request sur GitHub vers `main`. Après la fusion :

```bash
git switch main
git pull
git branch -d feature/ma-fonctionnalite
```

## Annuler / corriger avec prudence

```bash
git restore fichier.py       # annule les changements locaux non commités du fichier
git restore --staged fichier.py  # retire le fichier de la zone de préparation
```

Ces commandes peuvent faire perdre des modifications. Vérifier `git status` avant de les utiliser. Éviter `git reset --hard` et `git push --force` dans le travail courant.

## Authentification HTTPS

GitHub n'accepte plus le mot de passe du compte comme mot de passe Git en HTTPS. Utiliser GitHub CLI (`gh auth login`) ou un gestionnaire d'identifiants compatible OAuth. Ne jamais coller un token dans un dépôt, un message Discord ou une capture d'écran.
