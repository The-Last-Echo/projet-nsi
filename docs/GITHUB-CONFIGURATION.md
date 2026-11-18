# Configuration GitHub du dépôt

Ce document décrit l'organisation retenue pour le dépôt `The-Last-Echo/projet-nsi`. Il sert de référence pour les membres de l'équipe et pour la personne qui administre le dépôt.

> **Important :** ce document décrit les réglages à conserver et les points à contrôler. Il ne remplace pas une vérification dans les paramètres GitHub : l'interface peut évoluer et seuls les réglages réellement enregistrés font foi.

## 1. Informations générales

| Élément | Valeur |
|---|---|
| Dépôt | `The-Last-Echo/projet-nsi` |
| URL | https://github.com/The-Last-Echo/projet-nsi |
| Visibilité | Public |
| Branche principale | `main` |
| Langage | Python |
| Protocole Git | HTTPS |
| Communication | Discord |
| Cahier des charges et comptes rendus | Document Word partagé par l'équipe |

## 2. Rôle de chaque outil

- **GitHub** : code, historique, Issues, Pull Requests et documentation technique de référence.
- **Word** : rédaction collaborative du cahier des charges et des comptes rendus de réunion. Les décisions validées qui concernent le développement doivent ensuite être reportées dans la documentation GitHub.
- **Discord** : échanges rapides, questions et coordination. Les décisions importantes ne doivent pas rester uniquement dans une conversation Discord.

## 3. Règles de collaboration

- Les développements se font sur des branches dédiées.
- Les membres ne travaillent pas directement sur `main`.
- Les modifications destinées à `main` passent par une Pull Request.
- Les PR sont relues par un autre membre avant leur fusion, conformément aux règles de protection configurées.
- La méthode de fusion retenue est **Squash and merge**.
- La suppression automatique des branches fusionnées est souhaitée.

Les étapes détaillées sont décrites dans [`COLLABORATION-GUIDE.md`](COLLABORATION-GUIDE.md).

## 4. Nommage des branches

| Préfixe | Utilisation | Exemple |
|---|---|---|
| `feature/` | Nouvelle fonctionnalité | `feature/grid-rendering` |
| `fix/` | Correction | `fix/player-boundaries` |
| `docs/` | Documentation | `docs/update-contributing` |
| `refactor/` | Réorganisation interne | `refactor/grid-module` |

Les noms sont courts, descriptifs, en minuscules et sans espaces. Utilise des tirets pour séparer les mots.

## 5. Commits et titres de Pull Requests

Le projet utilise Conventional Commits en anglais :

```text
<type>(<scope>): <short description>
```

Le scope est facultatif. Types retenus : `feat`, `fix`, `docs`, `refactor`, `test`, `chore` et, si nécessaire, `style`.

Exemples :

```text
feat(player): add player movement
fix(grid): prevent invalid coordinates
docs(git): clarify contribution workflow
test(grid): cover boundary conditions
```

Les titres des Pull Requests doivent suivre cette convention. Avec Squash and merge, vérifie le titre du commit final avant de confirmer la fusion.

Référence : [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## 6. Protection de la branche `main`

La branche `main` doit rester protégée. Les réglages souhaités sont :

| Règle | Réglage attendu | Vérification |
|---|---|---|
| Pull Request obligatoire | Activée | Settings → Rules → Rulesets, ou Branches selon le type de règle |
| Approbation avant fusion | Au moins une review d'un autre membre, si la règle est activée | Ouvrir le Ruleset actif et vérifier le nombre d'approbations |
| Conversations de review | Résolues avant fusion | Vérifier les règles du Ruleset |
| Force push sur `main` | Interdit | Vérifier le Ruleset |
| Suppression de `main` | Interdite | Vérifier le Ruleset |
| Tests obligatoires | À définir lorsque les tests automatisés existeront | Ne pas rendre obligatoire un statut de test inexistant |

Une approbation ne peut pas être donnée par l'auteur de la Pull Request pour satisfaire une règle qui exige l'approbation d'une autre personne. Si le responsable de l'intégration ouvre sa propre PR, un autre membre doit donc la relire et l'approuver lorsque cela est exigé.

Le document ne doit pas prétendre qu'une règle est active si elle n'a pas été contrôlée dans l'interface GitHub. Après toute modification du Ruleset, vérifie et mets cette section à jour.

## 7. Méthode de fusion et suppression des branches

La méthode retenue est **Squash and merge** : les commits d'une branche sont regroupés dans un seul commit sur `main`.

La suppression automatique des branches source après leur fusion peut être activée dans **Settings → General → Pull Requests → Automatically delete head branches**.

Attention : après un Squash and merge, Git peut considérer que les anciens commits de la branche ne sont pas présents dans `main`. Il peut donc refuser `git branch -d`. Le [guide de collaboration](COLLABORATION-GUIDE.md) explique comment supprimer la branche locale en vérifiant d'abord que la PR est bien fusionnée.

## 8. Issues, labels et milestones

Les Issues servent à décrire et suivre les bugs, fonctionnalités et tâches qui nécessitent une organisation. **Elles ne sont pas obligatoires pour chaque petite modification** : une correction documentaire simple peut passer directement par une branche et une PR.

Les modèles d'Issues se trouvent dans `.github/ISSUE_TEMPLATE/`.

Labels proposés :

| Label | Utilisation |
|---|---|
| `type: bug` | Problème à corriger |
| `type: feature` | Nouvelle fonctionnalité |
| `type: documentation` | Travail sur les documents |
| `type: task` | Tâche générale |
| `priority: high` | Priorité élevée |
| `priority: normal` | Priorité normale |
| `priority: low` | Priorité basse |

Les labels indiqués dans les modèles doivent exister dans les paramètres du dépôt avec exactement le même nom. Les champs de priorité dans les formulaires ne créent pas automatiquement un label de priorité : celui-ci est ajouté manuellement si nécessaire.

Les milestones peuvent regrouper les tâches par version. Leur contenu sera décidé lorsque le jeu et ses étapes de développement seront plus précis. GitHub Projects reste facultatif au lancement.

## 9. Sécurité

- Ne commite jamais de mot de passe, token, clé API ou fichier `.env` contenant des secrets.
- Le `.gitignore` exclut les environnements virtuels et les fichiers locaux courants.
- Vérifie les fichiers ajoutés avant chaque commit et chaque Pull Request.
- Ne partage pas tes identifiants dans Discord, Word, une Issue ou une PR.

Un `.gitignore` n'est pas un coffre-fort. Si un secret est déjà envoyé sur GitHub, l'ajouter ensuite au `.gitignore` ne l'efface pas de l'historique. Il faut révoquer ou renouveler le secret et prévenir le responsable du dépôt.

## 10. Licence

Aucune licence open source n'a encore été choisie. L'équipe doit en discuter avant d'ajouter un fichier `LICENSE`, en tenant compte des droits des contributeurs et des consignes de l'enseignant.

Un dépôt public sans fichier de licence est consultable, mais cela ne signifie pas que les autres utilisateurs disposent d'une autorisation générale de réutiliser le code.

## 11. GitHub Actions et automatisation

Aucun workflow GitHub Actions de test n'est activé pour le moment : le code Python et la stratégie de tests ne sont pas encore définis.

Lorsque le premier code et les tests existeront, on pourra ajouter un workflow simple qui :

1. installe la version de Python retenue par l'équipe ;
2. installe les dépendances définies dans `requirements.txt` ;
3. exécute les tests ;
4. signale le résultat sur chaque Pull Request vers `main`.

Ne rends pas obligatoire un statut de test dans la protection de `main` avant que le workflow existe et ait été vérifié.

## 12. Maintenance du document

Mets cette fiche à jour lorsque les paramètres réels du dépôt changent : Rulesets, méthode de fusion, suppression automatique des branches, labels ou permissions des collaborateurs.

## Ressources officielles

- [GitHub Docs — Règles disponibles dans les Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [GitHub Docs — Créer un Ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [GitHub Docs — Méthodes de fusion des Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)
- [GitHub Docs — Suppression automatique des branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches)
- [GitHub Docs — Modèles d'Issues et de Pull Requests](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
