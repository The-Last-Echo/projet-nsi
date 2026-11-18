# Guide de collaboration — comment travailler en équipe

Ce guide explique comment une modification passe de ton ordinateur à la branche `main` sur GitHub. Tu peux le suivre même si tu découvres Git.

> **Le principe :** on travaille chacun sur une branche, on envoie cette branche sur GitHub, puis on propose une Pull Request. Après relecture, le responsable de l'intégration fusionne la PR dans `main`. On ne développe pas directement sur `main`.

## 1. À quoi servent les Issues ?

Une Issue est une fiche qui décrit un bug, une fonctionnalité ou une tâche. Elle est pratique lorsqu'il faut expliquer le besoin, répartir le travail ou garder une trace de ce qui reste à faire.

**Il n'est pas obligatoire de créer une Issue pour chaque modification.**

- Pour une fonctionnalité, un bug ou une tâche qui nécessite un suivi, crée ou utilise une Issue.
- Pour une petite correction évidente, une mise à jour de documentation ou un travail ponctuel, tu peux créer directement une branche et une PR.
- Avant de commencer un travail important, vérifie tout de même que quelqu'un d'autre ne travaille pas déjà dessus.

Les labels servent à classer les Issues, par exemple `type: bug`, `type: task` ou `priority: high`. Les milestones peuvent regrouper les tâches d'une version future. GitHub Projects est facultatif et pourra être ajouté si le groupe en ressent le besoin.

## 2. Préparer son dépôt local

La première fois, récupère le projet :

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

Avant chaque nouvelle tâche, vérifie ton état de travail :

```bash
git status
```

Si des modifications apparaissent, vérifie qu'elles sont enregistrées ou sauvegardées avant de changer de branche. Ensuite, mets `main` à jour :

```bash
git switch main
git pull --ff-only
```

Si `git pull --ff-only` échoue, arrête-toi et demande de l'aide. Ne lance pas automatiquement `git reset --hard`.

## 3. Créer une branche pour la tâche

Une branche est une zone de travail séparée. Elle évite de modifier directement `main`.

| Préfixe | Utilisation | Exemple |
|---|---|---|
| `feature/` | Nouvelle fonctionnalité | `feature/grid-rendering` |
| `fix/` | Correction d'un problème | `fix/player-boundaries` |
| `docs/` | Documentation | `docs/update-readme` |
| `refactor/` | Réorganisation interne | `refactor/grid-module` |

Crée la branche depuis `main` à jour :

```bash
git switch -c feature/grid-rendering
```

Choisis un nom court, en minuscules, sans espace. Utilise des tirets pour séparer les mots.

## 4. Modifier les fichiers et préparer un commit

Travaille uniquement sur les éléments liés à ta tâche. Tu peux faire plusieurs commits si cela permet de séparer des changements cohérents.

Avant de préparer ton commit :

```bash
git status
git diff
```

Ajoute seulement les fichiers concernés :

```bash
git add chemin/du/fichier
```

Vérifie ce qui sera enregistré :

```bash
git diff --staged
```

Crée ton commit :

```bash
git commit -m "feat(grid): add grid rendering"
```

Les messages sont rédigés en anglais et suivent la convention Conventional Commits. Exemples :

```text
feat(player): add player movement
fix(grid): prevent invalid coordinates
docs(git): clarify branch workflow
test(grid): cover empty grid handling
```

## 5. Envoyer la branche sur GitHub

Pour le premier envoi de la branche :

```bash
git push -u origin feature/grid-rendering
```

Pour les suivants :

```bash
git push
```

Le code est maintenant envoyé sur GitHub, mais il n'est pas encore intégré à `main`.

## 6. Créer une Pull Request

Sur GitHub :

1. ouvre le dépôt `The-Last-Echo/projet-nsi` ;
2. ouvre l'onglet **Pull requests** ;
3. clique sur **New pull request** ;
4. choisis ta branche comme branche source (*compare*) et `main` comme branche de destination (*base*) ;
5. vérifie les fichiers et les changements affichés ;
6. donne un titre clair, par exemple `feat(grid): add grid rendering` ;
7. complète la description ;
8. associe une Issue si la PR répond à une Issue, par exemple `Closes #12` ;
9. clique sur **Create pull request**.

Une Pull Request (*PR*) est une proposition de changement. Elle permet aux autres membres de comprendre, relire et commenter ton travail avant la fusion.

## 7. Faire relire la Pull Request

Le responsable de l'intégration ou un autre membre désigné examine la PR. Il vérifie notamment :

- que la modification correspond au besoin annoncé ;
- que le code ou le document est compréhensible ;
- que les tests disponibles ont été exécutés ;
- qu'aucun secret ou fichier personnel inutile n'a été ajouté ;
- que la documentation est mise à jour lorsque c'est nécessaire.

Une review peut approuver la PR (*Approve*) ou demander des corrections (*Request changes*). Si l'auteur de la PR est aussi le responsable de l'intégration, un autre membre réalise la relecture.

## 8. Corriger les remarques

Si des changements sont demandés, reste sur la même branche. Corrige les fichiers, puis crée un nouveau commit et envoie-le :

```bash
git status
git add chemin/du/fichier
git diff --staged
git commit -m "fix(player): handle invalid movement"
git push
```

La Pull Request se met à jour automatiquement : il n'est pas nécessaire d'en créer une nouvelle. Réponds aux commentaires pour expliquer ce que tu as corrigé ou demander une précision.

## 9. Tester une Pull Request sur son ordinateur

Il est possible de récupérer la branche d'une PR sans la fusionner. Avec GitHub CLI, pour une PR numéro 15 :

```bash
gh pr checkout 15
```

Tu peux alors examiner le code et lancer les vérifications disponibles. Pour consulter uniquement les différences :

```bash
gh pr diff 15
```

Après tes vérifications, tu peux revenir sur `main` :

```bash
git switch main
```

N'effectue pas de modifications sur la branche d'un autre membre sans vous être mis d'accord au préalable.

## 10. Fusionner la Pull Request

La fusion est réalisée par le responsable de l'intégration, après la review et les vérifications nécessaires.

La méthode retenue est **Squash and merge**. GitHub rassemble les commits de la branche dans un seul nouveau commit sur `main`. Cela garde l'historique de la branche principale plus lisible.

Avant la fusion, vérifie :

- que la PR vise `main` ;
- que les commentaires importants sont traités ;
- que les tests disponibles passent ;
- que le titre et le message du commit final sont clairs ;
- que la PR ne contient que les changements attendus.

## 11. Mettre à jour et nettoyer son dépôt après la fusion

Vérifie d'abord sur GitHub que la PR est bien indiquée comme **Merged**. Puis mets `main` à jour :

```bash
git switch main
git pull --ff-only
```

Supprime ensuite la branche locale :

```bash
git branch -D feature/grid-rendering
```

Avec Squash and merge, `git branch -d` peut refuser la suppression : les commits d'origine de la branche ne sont pas forcément présents tels quels dans `main`. `-D` force la suppression de la référence locale. C'est approprié uniquement après avoir confirmé que la PR est fusionnée et qu'il ne reste rien à récupérer sur cette branche.

GitHub peut également supprimer la branche distante après la fusion si l'option **Automatically delete head branches** est activée.

## 12. Quand demander de l'aide ?

Arrête-toi avant d'essayer des commandes risquées si :

- `git pull` ou `git push` affiche une erreur que tu ne comprends pas ;
- tu as créé des modifications sur la mauvaise branche ;
- Git signale des conflits ;
- tu penses avoir perdu un fichier ou un commit ;
- une commande te propose de supprimer ou de remplacer des changements.

Envoie le message d'erreur complet, après avoir masqué toute information privée. Ne partage jamais de token ou de mot de passe.

## Récapitulatif : le cycle de travail

```bash
# Mettre main à jour
git switch main
git pull --ff-only

# Créer sa branche
git switch -c feature/short-description

# Modifier les fichiers, puis inspecter
git status
git diff

# Préparer et créer un commit
git add chemin/du/fichier
git diff --staged
git commit -m "feat(scope): describe the change"

# Envoyer la branche
git push -u origin feature/short-description
```

Ouvre ensuite une Pull Request vers `main`, fais relire tes changements, corrige les remarques et attends la fusion.

## Ressources officielles

- [GitHub Docs — À propos des Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [GitHub Docs — À propos des Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [GitHub CLI — `gh pr checkout`](https://cli.github.com/manual/gh_pr_checkout)
- [GitHub Docs — Méthodes de fusion](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)
- [GitHub Docs — Suppression automatique des branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches)
