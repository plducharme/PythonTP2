# PythonTP2
Travail Pratique 2 pour le cours 420-SD2-HY

# Nouvelle Portée
- Le nombre de requis a été grandement diminué
  - toutes les notions d'authentification ne sont plus nécessaires
  - seulement 3 méthodes de votre choix dans la classe client doivent avoir des tests unitaires
    - 1 point boni si tous les tests unitaires sont présents pour toutes les méthodes dans la classe client
  - la gestion du cache est maintenant un boni de 3 pts, ce n'est plus un requis obligatoire
  - un requis boni (2 point) pour un affichage en HTML d'une réservation
    - voir serveur\README.md
  - ajustement des requis pour les deux méthodes d'exportation de données pour les rendre indépendantes et plus simples
  - simplification du requis de création des réservations
  - L'import des données du serveur est fait séparément
      - Partir votre serveur
      - Exécuter votre module impex.py en appelant la fonction executer()
        - voir le nouveau requis impex\README.md
  - Pour les objets utilisateurs, vous n'avez plus besoin d'utiliser un Enum pour le type

## Introduction
Bienvenue chez SuperChalets! Notre mission est de permettre
à nos clients de réserver des chalets idylliques à travers le Québec!

En tant que notre nouveau département informatique, vous devez implémenter un système permettant
d'importer/exporter des réservations à partir de fichiers et de pouvoir les exposer via un API json

## Survol du système

Le système sera composé des sous-systèmes suivants:
### Le serveur
- Responsable de sauvegarder sur disque les réservations qui lui sont soumises
- Doit aussi servir aux clients les informations sur leurs réservations via un API json
### Le module d'import/export "impex"
- Module qui permet d'importer des données dans le serveur via le client
- Permet aussi d'exporter les données vers divers formats
### Le client
- Le client communique avec le serveur pour effectuer une série d'opérations

## Détails
- Dans les répertoires de chaque sous-système, vous trouverez un README.md qui indique les 
requis fonctionnels de ce sous-système

## Évaluation
Ce TP vaut 20% de la note finale:
- 7% pour la fonctionnalité (si le code marche avec le jeu de test)
- 5% pour la qualité de l'implémentation (encapsulation, choix du type de méthodes, etc)
- 3% pour la documentation (je vous laisse le design, ça doit être clair le rôle d'une classe)
- 5% pour la qualité des tests unitaires (couvrir les cas de bases)

## Concept
2) Le module impex doit utiliser le module client pour effectuer les opérations d'import



