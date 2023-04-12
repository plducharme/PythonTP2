# impex
##  Rôle
Permet d'importer et exporter des données du serveur SuperChalets
## Requis fonctionnels
- Lire un fichier CSV contenant les utilisateurs, leur type d'utilisateur (Enum), leur mot de passe
  - Appeler le serveur pour créer l'utilisateur
- Lire un fichier CSV contenant les Chalets
  - Appeler le serveur pour les créer
- Lire un fichier XML contenant les disponibilités de réservations pour les chalets
  - Appeler le serveur pour les créer
- Lire un fichier XML contenant les réservations et appeler le serveur pour les créer si les plages sont disponibles
  - Envoyer une erreur "ReservationError" et écrire 'reservationId' dans un fichier "erreurs.log"
- Les données sont dans le répertoire "data"
- Implémenter une méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV
  - Doit se faire via l'appel au serveur
- Implémenter une méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.json" dans le format JSON
  - Doit se faire via l'appel au serveur