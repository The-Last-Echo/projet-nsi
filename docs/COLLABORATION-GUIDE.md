# Guide de collaboration — le workflow de l'équipe

Ce guide décrit comment une tâche passe de l'idée à une modification intégrée dans `main`. Il est conçu pour être suivi étape par étape, même si tu découvres Git et GitHub.

Le principe est simple : **on discute et on suit le travail dans GitHub, on développe sur une branche, puis on propose les changements dans une Pull Request.** On ne développe pas directement sur `main`.

## 1. Comprendre les outils de suivi

### Issues : décrire le travail

Une Issue sert à décrire un bug, une amélioration ou une tâche. Elle doit permettre aux autres membres de comprendre ce qu'il faut faire et pourquoi.

Avant de commencer une tâche, vérifie qu'une Issue existe. Si le besoin n'est pas encore clair, discutez-en avant de créer une branche.

### Labels : classer les Issues

Les labels servent à retrouver rapidement les tâches par nature ou priorité. Le dépôt utilisera un petit ensemble de labels, par exemple :

- `type: bug` ;
- `type: feature` ;
- `type: documentation` ;
- `type: task` ;
- `priority: high` ;
- `priority: normal` ;
- `priority: low`.

Les labels sont des catégories. Ils ne représentent pas une version du jeu.

### Milestones : regrouper les tâches par version

Une milestone peut regrouper les Issues et Pull Requests prévues pour une version, par exemple V1 ou V2. Les contenus de ces versions seront définis collectivement quand le concept du jeu sera suffisamment précis.

### GitHub Projects : visualiser l'avancement

Un Project peut offrir une vue de type tableau (à faire, en cours, en review, terminé). Il est facultatif au début : les Issues et milestones suffisent pour démarrer. On l'ajoutera si le groupe en ressent le besoin.

## 2. Préparer son travail local

### Première utilisation

Clone le dépôt si ce n'est pas déjà fait :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

### Avant chaque nouvelle tâche

Vérifie d'abord l'état du dépôt :

```bash
git status
```

Si tu as des modifications locales que tu souhaites conserver, ne les écrase pas. Une fois ton espace de travail propre ou tes changements mis de côté de manière sûre, récupère `main` :

```bash
git switch main
git pull --ff-only
```

Si `git pull --ff-only` échoue, arrête-toi et vérifie pourquoi. Ne lance pas automatiquement `git reset --hard`.

## 3. Créer une branche

Chaque tâche doit avoir sa branche. Le nom commence par le préfixe adapté :

| Préfixe | Exemple | Utilisation |
|---|---|---|
| `feature/` | `feature/grid-rendering` | Nouvelle fonctionnalité |
| `fix/` | `fix/player-boundaries` | Correction |
| `docs/` | `docs/update-readme` | Documentation |
| `refactor/` | `refactor/grid-module` | Réorganisation interne |

Créer la branche :

```bash
git switch -c docs/update-readme
```

La branche est créée à partir de la branche actuellement sélectionnée. Vérifie donc que tu es bien sur `main` à jour avant de la créer.

## 4. Développer et vérifier les modifications

Modifie uniquement ce qui est nécessaire pour l'Issue. Enregistre souvent des commits cohérents plutôt qu'un énorme commit à la fin.

Avant de préparer un commit :

```bash
git status
git diff
```

Ajoute les fichiers concernés :

```bash
git add docs/README.md
```

Vérifie précisément ce qui partira dans le commit :

```bash
git diff --staged
```

Puis crée le commit avec un message Conventional Commits en anglais :

```bash
git commit -m "docs(readme): clarify project setup"
```

Exemples :

```text
feat(grid): add grid rendering
fix(player): prevent invalid coordinates
docs(git): explain branch creation
test(grid): cover empty grid handling
```

## 5. Envoyer sa branche sur GitHub

La première fois :

```bash
git push -u origin docs/update-readme
```

Les fois suivantes, sur la même branche :

```bash
git push
```

Le code est maintenant disponible sur GitHub, mais il n'est pas encore intégré à `main`.

## 6. Ouvrir une Pull Request

Sur GitHub :

1. ouvre le dépôt ;
2. sélectionne **Pull requests** ;
3. clique sur **New pull request** ;
4. choisis ta branche comme branche source (*compare*) et `main` comme branche de destination (*base*) ;
5. vérifie le diff ;
6. donne un titre conforme à Conventional Commits ;
7. complète le modèle de description ;
8. associe l'Issue, par exemple avec `Closes #12` ;
9. crée la Pull Request.

Une Pull Request (*PR*) est une proposition d'intégration. Elle sert à expliquer les changements, les examiner et les discuter avant la fusion.

## 7. Faire relire la Pull Request

Le responsable de l'intégration effectue la review des Pull Requests ouvertes par les autres membres. Il examine notamment :

- si la modification répond à l'Issue ;
- si le code est compréhensible et cohérent avec le projet ;
- si les cas limites évidents sont pris en compte ;
- si les tests disponibles ont été exécutés ;
- si aucun secret ou fichier inutile n'a été ajouté.

Des commentaires peuvent être laissés directement sur les lignes concernées. Une review peut approuver la PR ou demander des changements (*Request changes*).

Si le responsable de l'intégration est lui-même l'auteur de la PR, un autre membre doit faire la relecture. L'auteur ne peut pas approuver sa propre Pull Request pour satisfaire une règle d'approbation obligatoire.

## 8. Corriger les remarques

Si des modifications sont demandées, l'auteur reste sur la même branche et apporte les corrections :

```bash
git status
git add chemin/du/fichier
git commit -m "fix(player): handle invalid input"
git push
```

La PR est automatiquement mise à jour. Il n'est pas nécessaire d'en ouvrir une nouvelle.

Réponds aux commentaires pour indiquer ce qui a été corrigé ou demander une précision. Une conversation ne doit être résolue que lorsqu'elle est traitée ou explicitement considérée comme terminée.

## 9. Tester une Pull Request sur son ordinateur

Il est possible de tester une PR sans la fusionner.

Avec GitHub CLI, si elle est par exemple numérotée `15` :

```bash
gh pr checkout 15
```

Cette commande récupère la branche de la Pull Request et la sélectionne localement. Tu peux alors lire le code, exécuter le programme et lancer les tests disponibles.

Pour consulter le diff sans changer de branche :

```bash
gh pr diff 15
```

Pour travailler dans un dossier séparé sans quitter ta branche actuelle :

```bash
gh pr checkout 15 --worktree ../projet-nsi-pr-15
```

Après les tests, reviens à ton organisation habituelle. Si tu as créé un worktree séparé et qu'il ne contient aucun changement à conserver, tu peux le retirer avec :

```bash
git worktree remove ../projet-nsi-pr-15
```

Ne supprime pas un worktree qui contient des modifications non sauvegardées.

## 10. Fusionner la Pull Request

La fusion est effectuée par le responsable de l'intégration, après la review et les vérifications nécessaires.

La méthode retenue est **Squash and merge** : les commits de la branche sont regroupés en un seul commit dans `main`. Cela permet de conserver un historique principal lisible.

Avant de fusionner :

- vérifie que la PR vise bien `main` ;
- relis le titre et la description ;
- vérifie les commentaires et les tests ;
- vérifie que le titre du commit final respecte Conventional Commits ;
- confirme que les conversations nécessaires sont résolues.

Le titre de la Pull Request peut servir de titre au commit squash. Corrige-le si nécessaire avant la fusion.

## 11. Mettre à jour et nettoyer son dépôt local

Après la fusion :

```bash
git switch main
git pull --ff-only
git branch -d docs/update-readme
```

Si Git indique que la branche n'est pas complètement fusionnée, ne force pas sa suppression. Vérifie son état et demande de l'aide si tu n'es pas sûr.

La branche distante peut être supprimée automatiquement par GitHub après la fusion si l'option correspondante est activée.

## 12. Où utiliser l'IA ?

Un outil d'IA peut servir de deuxième regard pour repérer des bugs possibles, des cas oubliés ou des problèmes de lisibilité. Il ne connaît pas nécessairement toutes les règles du jeu et peut proposer des corrections incorrectes.

Pour demander une analyse, fournis le contexte de l'Issue et le diff de la PR. Demande des observations précises, avec fichier, ligne et explication. N'accepte pas automatiquement les modifications proposées.

La décision finale, la compréhension du code, les tests et la fusion restent sous la responsabilité des membres du groupe. Ne transmets jamais de secrets ou de données privées à un service d'IA.

## 13. Récapitulatif rapide

```bash
# Mettre main à jour
git switch main
git pull --ff-only

# Créer une branche
git switch -c feature/short-description

# Développer, puis vérifier
git status
git diff

# Préparer et inspecter le commit
git add chemin/du/fichier
git diff --staged

# Créer le commit et envoyer la branche
git commit -m "feat(scope): describe the change"
git push -u origin feature/short-description
```

Ouvre ensuite une Pull Request sur GitHub vers `main`, attends la review, effectue les corrections demandées et laisse le responsable de l'intégration réaliser le Squash and merge.

## Ressources officielles et pour aller plus loin

- [GitHub Docs — About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [GitHub Docs — About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [GitHub Docs — Reviewing proposed changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests)
- [GitHub Docs — About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [GitHub CLI — `gh pr checkout`](https://cli.github.com/manual/gh_pr_checkout)
- [GitHub Docs — About milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

*Dernière vérification des liens et des procédures : novembre 2026. Les noms d'interface peuvent évoluer ; le fonctionnement général du workflow reste le même.*
