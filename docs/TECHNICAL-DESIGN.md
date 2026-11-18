# Conception technique du jeu

> **État du document : base de travail.** Le concept et les règles du jeu ne sont pas encore définis. Les sections ci-dessous servent à organiser la future conception ; elles ne décrivent pas des fonctionnalités déjà décidées.

## 1. Contexte et contraintes

### 1.1 Objectif du programme

À définir collectivement après validation du concept du jeu.

### 1.2 Contraintes connues

- Langage : Python.
- Interface : terminal / console.
- Le code source sera placé dans `src/`.
- Les tests seront placés dans `tests/` lorsqu'ils seront créés.

Une grille représentée par une liste de listes et un joueur représenté par un caractère ou un symbole ont été évoqués comme pistes, mais restent à confirmer.

### 1.3 Environnement d'exécution

- Version minimale de Python : à définir.
- Systèmes ciblés : à définir.
- Dépendances externes : à définir.
- Commande de lancement : à définir.

Chaque membre utilisera un environnement virtuel local `.venv`. Les dépendances communes seront décrites dans `requirements.txt` lorsqu'elles seront connues.

## 2. Règles et fonctionnement général

### 2.1 Objectif du joueur

À définir collectivement.

### 2.2 Déroulement d'une partie

À définir collectivement.

### 2.3 Conditions de fin

Conditions de victoire, de défaite ou d'arrêt à préciser.

## 3. Architecture logicielle

### 3.1 Vue d'ensemble

À définir à partir des règles du jeu. Ne créez pas de modules uniquement pour remplir cette section : chaque module devra avoir une responsabilité claire.

### 3.2 Modules et responsabilités

| Module | Responsabilité | État |
|---|---|---|
| À définir | À définir | Non décidé |

### 3.3 Point d'entrée

Le fichier et la fonction utilisés pour lancer le jeu restent à choisir.

## 4. Structures de données

### 4.1 Grille

Si le jeu utilise une grille, il faudra préciser :

- la signification des lignes et des colonnes ;
- les dimensions ;
- le type des valeurs stockées dans chaque case ;
- la représentation d'une case vide ;
- les règles d'accès et de modification ;
- les conditions qui doivent toujours rester vraies (*invariants*).

La représentation par liste de listes est une possibilité, pas encore une décision définitive.

### 4.2 Joueur

Il faudra préciser les informations nécessaires pour représenter le joueur dans le programme. Un caractère ou symbole peut servir à l'affichage, mais ne suffit pas nécessairement à représenter toutes les données du joueur.

### 4.3 Autres données

À définir selon le concept et les règles retenus.

## 5. Algorithmes et logique du jeu

Pour chaque algorithme important, documenter :

- son objectif ;
- ses paramètres et sa valeur de retour ;
- les étapes principales ou le pseudo-code ;
- les cas limites ;
- sa complexité si elle est pertinente au niveau du projet.

Les algorithmes ne sont pas encore définis.

## 6. Entrées et affichage

- Lecture des entrées utilisateur : à définir.
- Gestion des entrées invalides : à définir.
- Affichage du jeu dans le terminal : à définir.
- Messages affichés : à définir.

## 7. Gestion des erreurs et cas limites

À compléter lorsque les règles seront connues. Penser notamment aux limites de la grille si elle existe, aux entrées inattendues et aux états impossibles du jeu.

## 8. Tests

La stratégie de tests sera définie avec l'architecture. Elle pourra distinguer :

- tests unitaires des fonctions isolées ;
- tests des règles et interactions ;
- tests des cas limites ;
- vérifications du déroulement général du jeu.

Le framework et la commande de test restent à choisir.

## 9. Diagrammes

À ajouter lorsque l'architecture et les règles seront suffisamment stables. Selon les besoins, il pourra s'agir d'un diagramme de modules, d'organigrammes ou d'un diagramme d'états.

## 10. Décisions techniques ouvertes

| Sujet | Question | État |
|---|---|---|
| Version Python | Quelle version minimale retenir ? | À décider |
| Organisation du code | Quels modules sont réellement nécessaires ? | À décider |
| Structures de données | Quelles structures représentent les éléments du jeu ? | À décider |
| Tests | `unittest`, `pytest` ou autre approche ? | À décider |
| Dépendances | Le projet nécessite-t-il des bibliothèques externes ? | À décider |

## 11. Historique des modifications

| Date | Modification | Auteur |
|---|---|---|
| 2026-11-18 | Création de la base documentaire, sans préjuger du concept du jeu. | Équipe |
| 2026-11-18 | Clarification de l'organisation prévue en `src/` et de l'environnement virtuel `.venv`. | Équipe |
