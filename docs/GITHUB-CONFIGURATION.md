# Configuration GitHub du dépôt

Ce document décrit les choix d'organisation du dépôt `The-Last-Echo/projet-nsi` et les paramètres à vérifier sur GitHub. Il distingue volontairement les décisions retenues des réglages dont l'activation doit encore être contrôlée dans l'interface.

> **Important :** ce document est une référence de configuration, pas une preuve que chaque option est déjà activée. Après toute modification dans les paramètres GitHub, mets cette fiche à jour.

## 1. Informations générales

| Élément | Valeur |
|---|---|
| Dépôt | `The-Last-Echo/projet-nsi` |
| URL | https://github.com/The-Last-Echo/projet-nsi |
| Visibilité | Public |
| Branche principale | `main` |
| Langage | Python |
| Protocole Git | HTTPS |
| Communication | Discord, avec notifications GitHub via webhook |

## 2. Organisation du développement

- Les développements se font sur des branches dédiées et courtes.
- Les modifications destinées à `main` passent par une Pull Request.
- On ne développe pas directement sur `main`.
- Les PR ouvertes par les autres membres sont relues par le responsable de l'intégration.
- Si le responsable de l'intégration est l'auteur de la PR, un autre membre effectue la review.
- La méthode de fusion retenue est **Squash and merge**.
- La suppression automatique des branches fusionnées est souhaitée ; son état doit être vérifié dans les paramètres du dépôt.

## 3. Convention de nommage des branches

| Préfixe | Usage | Exemple |
|---|---|---|
| `feature/` | Nouvelle fonctionnalité | `feature/grid-rendering` |
| `fix/` | Correction | `fix/player-boundaries` |
| `docs/` | Documentation | `docs/update-contributing` |
| `refactor/` | Réorganisation interne | `refactor/grid-module` |

Les noms sont courts, descriptifs et écrits en minuscules. Les espaces sont remplacés par des tirets.

## 4. Commits et titres de Pull Requests

Le projet utilise Conventional Commits en anglais :

```text
<type>(<scope>): <short description>
```

Types utilisés : `feat`, `fix`, `docs`, `refactor`, `test`, `chore` et `style`.

Exemples :

```text
feat(player): add player movement
fix(grid): prevent invalid coordinates
docs(git): clarify contribution workflow
test(grid): cover boundary conditions
```

Les titres des Pull Requests doivent suivre la même convention. Avec Squash and merge, le titre de la PR peut devenir le message du commit final dans `main`.

Référence : [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

## 5. Règles prévues pour `main`

La branche `main` doit être protégée par un Ruleset ou une protection de branche adaptée. La configuration cible est la suivante :

| Règle | Configuration souhaitée | État documentaire |
|---|---|---|
| Pull Request obligatoire | Activée | À vérifier sur GitHub |
| Nombre d'approbations | 1 approbation | À vérifier sur GitHub |
| Approbateur différent de l'auteur | Oui | À vérifier sur GitHub |
| Conversations de review | Toutes résolues avant fusion | À vérifier sur GitHub |
| Approbations devenues obsolètes | Les invalider si le diff change | À configurer selon le comportement retenu |
| Force push sur `main` | Interdit | À vérifier sur GitHub |
| Suppression de `main` | Interdite | À vérifier sur GitHub |
| Méthode de fusion | Squash uniquement | À vérifier dans les paramètres de fusion |
| Tests obligatoires | Pas encore définis | À ajouter quand les tests et Actions existeront |

### Attention aux approbations

Une personne ne peut pas approuver sa propre Pull Request pour satisfaire une règle d'approbation obligatoire. Si le responsable de l'intégration ouvre lui-même une PR, un autre collaborateur devra donc la relire et l'approuver.

Le rôle d'administrateur peut disposer de possibilités de contournement selon la configuration du Ruleset. Ces possibilités doivent être examinées consciemment : la protection de `main` n'a d'intérêt que si l'équipe évite les contournements de routine.

## 6. Issues, labels et milestones

Les Issues servent à décrire le travail. Les modèles sont fournis dans `.github/ISSUE_TEMPLATE/`.

Labels de départ proposés :

| Label | Utilisation |
|---|---|
| `type: bug` | Problème à corriger |
| `type: feature` | Nouvelle fonctionnalité |
| `type: documentation` | Travail sur les documents |
| `type: task` | Tâche générale |
| `priority: high` | Priorité élevée |
| `priority: normal` | Priorité normale |
| `priority: low` | Priorité basse |

Les labels devront être créés dans GitHub avec exactement les mêmes noms pour que les modèles d'Issues puissent les ajouter automatiquement.

Les milestones serviront à regrouper les Issues par version (V1, V2, etc.). Leur contenu sera défini collectivement après la clarification du jeu. Les milestones ne remplacent pas les tags Git : une milestone organise le travail, alors qu'un tag identifie un commit précis.

GitHub Projects reste facultatif au lancement. Un tableau simple pourra être ajouté lorsque le volume de tâches le justifiera.

## 7. Revue et fusion des Pull Requests

Le déroulement détaillé est décrit dans [`COLLABORATION-GUIDE.md`](COLLABORATION-GUIDE.md).

En résumé :

1. le contributeur ouvre une PR vers `main` ;
2. le responsable de l'intégration examine la description, le diff et les tests ;
3. il demande des corrections ou approuve la PR ;
4. après validation, il utilise Squash and merge ;
5. la branche de travail est supprimée après la fusion, si la suppression automatique est activée.

## 8. Sécurité du dépôt

- Ne jamais commiter de mot de passe, token, clé API ou fichier `.env`.
- Utiliser `.gitignore` pour les fichiers locaux, environnements virtuels et fichiers sensibles qui ne doivent pas être suivis.
- Ne jamais envoyer d'identifiants dans Discord, les Issues ou les Pull Requests.
- Vérifier les fichiers ajoutés à une PR avant de la fusionner.
- Examiner les alertes de dépendances et les fonctionnalités de protection des secrets disponibles pour le dépôt.

Un `.gitignore` est une précaution pratique, pas un coffre-fort : si un secret est déjà commité, l'ajouter ensuite à `.gitignore` ne le retire pas de l'historique. Il faut alors révoquer ou renouveler le secret concerné.

## 9. Licence et réutilisation du code

Aucune licence open source n'est retenue pour le moment. Le groupe doit en discuter avec l'ensemble des contributeurs et, si nécessaire, avec l'enseignant avant d'ajouter un fichier `LICENSE`.

L'absence de licence ne rend pas le dépôt privé : le code reste consultable publiquement. Elle signifie qu'aucune licence open source n'accorde une autorisation générale de réutilisation. Elle ne constitue pas une protection technique contre la copie, et les droits de chaque contributeur doivent être pris en compte.

## 10. Automatisation

GitHub Actions sera ajouté lorsque le code et les premiers tests Python seront disponibles. La première automatisation devra rester simple : installer la version de Python retenue et exécuter les tests lors des Pull Requests vers `main`.

Aucun statut de test ne doit être exigé dans un Ruleset avant que le workflow correspondant existe et ait été vérifié.

## 11. Maintenance de ce document

Mettre cette fiche à jour lorsqu'une règle est modifiée dans GitHub. Après une modification des Rulesets, de la méthode de fusion, des labels ou des permissions, vérifier que le document décrit bien l'état réel du dépôt.

## Ressources officielles

- [GitHub Docs — Rulesets disponibles](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub Docs — Créer un Ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [GitHub Docs — Modèles d'Issues](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [GitHub Docs — Méthodes de fusion](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)
- [GitHub Docs — GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

*Document préparé en novembre 2026. Les paramètres indiqués « à vérifier » doivent être contrôlés dans l'interface du dépôt avant de considérer la configuration comme terminée.*
