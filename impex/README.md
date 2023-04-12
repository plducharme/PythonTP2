# impex
##  Rôle
Permet d'importer et exporter des données du serveur SuperChalet
## Requis fonctionnels
- Lire un fichier CSV contenant les utilisateurs, leur type d'utilisateur (Enum), leur mot de passe
  - Appeler le serveur pour créer l'utilisateur
- Lire un fichier XML contenant les disponibilités de réservations 
- Lire un fichier XML contenant les réservations et appeler le serveur pour les créer si les plages sont disponibles
  - Envoyer une erreur "ReservationError" et écrire 'reservationId' dans un fichier "erreurs.log"
- Implémenter une méthode pour persister les réservations
- Les données sont dans le répertoire "data"
- Une méthode pour exporter les données de réservations dans un fichier "export_{timestamp}.csv" dans le format CSV
