# Contribuer au projet

Ce fichier résume la procédure pour proposer une modification. Les explications détaillées sont dans le [guide Git](docs/GIT-GUIDE.md) et le [guide de collaboration](docs/COLLABORATION-GUIDE.md).

## Avant de commencer

- Vérifie que tu as accepté ton invitation de collaborateur GitHub et que tu peux accéder au dépôt.
- Ne travaille jamais directement sur `main`.
- Pour une fonctionnalité, un bug ou un travail qui nécessite un suivi, utilise une Issue si cela aide l'équipe. **Une Issue n'est pas obligatoire pour chaque petite modification.**
- Ne place jamais de mot de passe, token, clé API ou fichier contenant des secrets dans le dépôt.

## 1. Récupérer les dernières modifications

Si le dépôt n'est pas encore sur ton ordinateur :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

Si tu as déjà le dépôt :

```bash
git status
git switch main
git pull --ff-only
```

Si `git status` montre des modifications locales, ne change pas de branche avant de les avoir conservées ou terminées.

## 2. Créer une branche

Crée une branche à partir de `main` à jour. Choisis un nom court, descriptif, en minuscules :

```bash
git switch -c feature/player-movement
```

Préfixes utilisés :

- `feature/` : nouvelle fonctionnalité ;
- `fix/` : correction d'un problème ;
- `docs/` : documentation ;
- `refactor/` : réorganisation du code sans changer son comportement attendu.

## 3. Modifier les fichiers et créer un commit

Fais des changements ciblés. Avant de créer un commit, regarde ce qui a changé :

```bash
git status
git diff
```

Ajoute les fichiers concernés, puis vérifie exactement ce qui sera enregistré :

```bash
git add chemin/du/fichier
git diff --staged
```

Crée un commit avec un message en anglais suivant la convention du projet :

```bash
git commit -m "feat(player): add player movement"
```

Les types les plus utilisés sont `feat`, `fix`, `docs`, `refactor`, `test` et `chore`. Le [guide Git](docs/GIT-GUIDE.md) explique cette convention.

## 4. Envoyer la branche

La première fois que tu envoies cette branche :

```bash
git push -u origin feature/player-movement
```

Pour les prochains envois sur cette même branche :

```bash
git push
```

## 5. Ouvrir une Pull Request

Sur GitHub, ouvre **Pull requests → New pull request**. Sélectionne ta branche comme branche source (*compare*) et `main` comme branche de destination (*base*).

Dans la Pull Request :

- donne un titre clair, de préférence au format Conventional Commits ;
- explique ce qui a changé et pourquoi ;
- indique les vérifications effectuées ;
- associe une Issue si la modification en concerne une, par exemple `Closes #12`.

Une Pull Request (*PR*) est une proposition de modification. Elle permet de relire et discuter le changement avant son intégration dans `main`.

## 6. Review et fusion

Un autre membre relit la PR. Si des corrections sont demandées, effectue-les sur la même branche, crée de nouveaux commits et renvoie-les avec `git push`.

Quand la PR est validée, le responsable de l'intégration la fusionne avec **Squash and merge**. Les contributeurs ne fusionnent pas directement leur branche dans `main`.

## 7. Après la fusion

Vérifie que la PR est bien indiquée comme **Merged** sur GitHub. Mets ensuite `main` à jour :

```bash
git switch main
git pull --ff-only
```

Puis supprime la branche locale :

```bash
git branch -D feature/player-movement
```

**Pourquoi `-D` ?** Le projet utilise Squash and merge : GitHub rassemble les commits de la branche dans un nouveau commit. Git peut donc ne pas reconnaître les anciens commits comme fusionnés et refuser `git branch -d`. N'utilise `-D` qu'après avoir vérifié sur GitHub que la PR correspondante est bien fusionnée et qu'aucun travail de cette branche ne reste à conserver.

## Règles simples

- Fais des modifications ciblées et faciles à relire.
- Vérifie les fichiers ajoutés avant chaque commit et chaque PR.
- Lance le programme et les tests disponibles lorsque c'est pertinent.
- Mets à jour la documentation si le comportement ou les règles du projet changent.
- En cas de commande inattendue ou d'incertitude, arrête-toi et demande de l'aide plutôt que d'essayer une commande destructive.
