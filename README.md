# PythonTP2
Travail Pratique 2 pour le cours 420-SD2-HY

## Introduction
Bienvenue chez SuperChalets! Notre mission est de permettre
à nos clients de réserver des chalets idylliques à travers le Québec!

En tant que notre nouveau département informatique, vous devez implémenter un système permettant
d'importer des réservations à partir de fichiers et de pouvoir les exposer via un API json

## Survol du système

Le système sera composé des sous-systèmes suivants:
### Le serveur
- Responsable de sauvegarder sur disque les réservations qui lui sont soumises
- Doit aussi servir les clients authentifiés les informations sur leurs réservations via un API json
### Le module d'import/export "impex"
- Module qui permet d'importer des données dans les serveurs
- Permet aussi d'exporter les données vers divers formats
### Le client
- Le client communique avec le serveur pour aller chercher des informations sur les réservations
- Si appelé en tant qu'administrateur, peut retourner le résultat de recherches

## Détails
- Dans les répertoires de chaque sous-module, vous trouverez un README.md qui indique les 
requis fonctionnels de ce sous-système

## Évaluation
Ce TP vaut 20% de la note finale:
7% pour la fonctionnalité (si le code marche avec le jeu de test)
5% pour la qualité de l'implémentation (encapsulation, choix du type de méthodes, etc)
3% pour la documentation (je vous laisse le design, ça doit être clair le rôle d'une classe)
5% pour la qualité des tests unitaires (couvrir les cas de bases)



