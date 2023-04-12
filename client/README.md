# Client
## Rôle
Permet d'interagir avec le serveur pour aller chercher les informations de réservations
## Requis fonctionnels
- Permet d'effectuer les opérations CRUD d'un point de vue client
1) GET /reservation/{reservationId}: Retourne l'information sur la réservation
2) GET /reservations/{utilisateur}: Retourne toutes les réservations de l'utilisateur
3) POST /reservation: Ajoute une réservation
4) PUT /reservation/{reservationId}: remplace la réservation
5) DELETE /reservation/{reservationId}: Supprime la réservation
6) POST /utilisateur: Ajoute un utilisateur
7) GET /reservations: si administrateur, renvoyé toutes les réservations triées par ordre de
reservationId
- Afficher les informations de la réservation incluant l'image
