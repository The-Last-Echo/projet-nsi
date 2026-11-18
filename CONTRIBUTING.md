# Contribuer au projet

Ce fichier explique comment proposer une modification au dépôt. Il est volontairement pratique : pour comprendre les notions Git en détail, consulte le [guide Git](docs/GIT-GUIDE.md). Pour suivre toutes les étapes de collaboration, consulte le [guide de collaboration](docs/COLLABORATION-GUIDE.md).

## Avant de commencer

- Vérifie qu'une Issue existe déjà pour le travail envisagé. Si ce n'est pas le cas, crée-en une ou demande à l'équipe de clarifier le besoin.
- Vérifie que tu as accepté ton invitation de collaborateur et que tu peux accéder au dépôt.
- Ne travaille pas directement sur `main`.
- Ne place jamais de mot de passe, token, clé API ou fichier contenant des secrets dans le dépôt.

## 1. Récupérer le dépôt

Pour la première installation :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

Si le dépôt est déjà présent sur ton ordinateur :

```bash
cd chemin/vers/projet-nsi
git status
git switch main
git pull --ff-only
```

Avant de changer de branche, vérifie que `git status` ne signale pas de modifications locales que tu souhaites conserver.

## 2. Créer une branche

Chaque tâche doit être développée sur sa propre branche, créée à partir de `main` à jour.

```bash
git switch -c feature/short-description
```

Préfixes utilisés dans le projet :

- `feature/` : ajout d'une fonctionnalité ;
- `fix/` : correction d'un problème ;
- `docs/` : modification de la documentation ;
- `refactor/` : réorganisation du code sans changer son comportement attendu.

Utilise un nom court, descriptif, en minuscules, avec des tirets si nécessaire. Exemple : `docs/update-git-guide`.

## 3. Développer et préparer les changements

Travaille sur la tâche décrite dans l'Issue. Avant de créer un commit, vérifie ce qui a changé :

```bash
git status
git diff
```

Ajoute uniquement les fichiers liés à ta modification :

```bash
git add chemin/du/fichier.py
git diff --staged
```

Puis crée un commit dont le message respecte Conventional Commits, en anglais :

```bash
git commit -m "feat(player): add player movement"
```

Évite de regrouper des changements sans rapport dans un même commit ou une même Pull Request.

## 4. Envoyer la branche

```bash
git push -u origin feature/short-description
```

L'option `-u` associe la branche locale à sa branche distante. Pour les prochains envois de cette même branche, `git push` suffit généralement.

## 5. Ouvrir une Pull Request

Sur GitHub, ouvre une Pull Request avec :

- la branche de ta tâche comme branche source (*compare*) ;
- `main` comme branche de destination (*base*) ;
- un titre clair respectant Conventional Commits ;
- une description expliquant ce qui a changé et comment la modification a été vérifiée ;
- un lien vers l'Issue associée, par exemple `Closes #12`.

Ne fusionne pas toi-même la Pull Request. Le responsable de l'intégration s'occupe de la relecture et de la fusion. Si la Pull Request est ouverte par le responsable lui-même, un autre membre doit effectuer la relecture.

## 6. Répondre à la review

Si des changements sont demandés, effectue les corrections sur la même branche, crée un ou plusieurs commits supplémentaires, puis renvoie-les :

```bash
git add chemin/du/fichier.py
git commit -m "fix(player): handle invalid movement"
git push
```

La Pull Request se met à jour automatiquement. Réponds aux commentaires lorsque tu as effectué les corrections ou lorsque tu as besoin d'une précision.

## 7. Après la fusion

Une fois la Pull Request fusionnée, mets à jour ta branche principale et supprime ta branche locale :

```bash
git switch main
git pull --ff-only
git branch -d feature/short-description
```

La suppression de la branche distante est normalement effectuée automatiquement par GitHub après la fusion, si le paramètre correspondant est activé.

## Quelques règles simples

- Fais des modifications ciblées et faciles à relire.
- N'ajoute pas de fichiers générés, temporaires ou personnels sans raison.
- Vérifie le programme et les tests disponibles avant de demander une review.
- Signale les bugs et les idées de travail avec une Issue plutôt que de les laisser uniquement dans Discord.
- Si une commande Git produit un résultat inattendu, arrête-toi et demande de l'aide avant d'essayer une commande destructive.
