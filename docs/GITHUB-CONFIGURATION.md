# Configuration GitHub du dépôt

## Informations

- Dépôt : `The-Last-Echo/projet-nsi`
- Visibilité : publique
- Branche principale : `main`
- Langage : Python

## Organisation

- Les développements se font sur des branches courtes.
- Les modifications vers `main` passent par Pull Request.
- Une autre personne relit la Pull Request avant fusion lorsque l'équipe le permet.
- Méthode de fusion recommandée : Squash and merge.
- Suppression automatique des branches fusionnées : activée.

## Branches

- `feature/nom` : fonctionnalité ;
- `fix/nom` : correction ;
- `docs/nom` : documentation ;
- `refactor/nom` : refactorisation.

## Sécurité

- Ne jamais commiter de mot de passe, token, clé API ou fichier `.env`.
- Conserver les secrets dans les paramètres prévus à cet effet, jamais dans le code.
- Utiliser `.gitignore` pour les fichiers locaux et environnements virtuels.
- Activer les alertes Dependabot et la protection contre les secrets si elles sont disponibles sans coût supplémentaire.

Cette fiche décrit les choix du projet ; elle doit être mise à jour si les paramètres GitHub changent.
