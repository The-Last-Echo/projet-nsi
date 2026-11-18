# Contribuer au projet

Pour garder un historique compréhensible, toutes les modifications destinées à `main` passent par une Pull Request.

## 1. Récupérer le projet

```bash
git clone https://github.com/The-Last-Echo/projet-nsi.git
cd projet-nsi
```

## 2. Créer une branche

Partir de `main` à jour :

```bash
git switch main
git pull
git switch -c feature/nom-court
```

Préfixes conseillés :
- `feature/` : fonctionnalité ;
- `fix/` : correction ;
- `docs/` : documentation ;
- `refactor/` : réorganisation interne.

## 3. Travailler et enregistrer

```bash
git status
git add fichier.py
git commit -m "feat: ajoute une fonctionnalité"
git push -u origin feature/nom-court
```

Ne pas ajouter de fichiers secrets (`.env`, tokens, mots de passe).

## 4. Ouvrir une Pull Request

Sur GitHub, ouvrir une Pull Request de votre branche vers `main`, expliquer le changement et indiquer les éventuelles Issues concernées. Attendre une revue avant la fusion.

## 5. Après la fusion

```bash
git switch main
git pull
git branch -d feature/nom-court
```

La branche distante peut être supprimée automatiquement par GitHub après la fusion.

## Règles simples

- Faire des changements petits et compréhensibles.
- Ne pas travailler directement sur `main`.
- Tester le programme avant de proposer une Pull Request.
- Signaler les problèmes avec une Issue.
- Demander de l'aide si une commande Git produit un résultat inattendu.
