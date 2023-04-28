# Client
## Rôle
Permet d'interagir avec le serveur pour effectuer diverses opérations
## Requis fonctionnels
- Permet d'effectuer les opérations CRUD d'un point de vue client
1) GET /reservation/{reservationId}: Retourne l'information sur la réservation
2) GET /reservations/{utilisateur}: Retourne toutes les réservations de l'utilisateur
3) POST /reservation: Ajoute une réservation
4) PUT /reservation/{reservationId}: Remplace la réservation
5) DELETE /reservation/{reservationId}: Supprime la réservation
6) POST /utilisateur: Ajoute un utilisateur
7) GET /reservations: Retourne toutes les réservations triées par ordre croissant de
reservationId
8) POST /chalet: Ajoute un chalet
9) GET /chalet/{chaletId}: Retourne les informations pour ce chalet
10) POST /chalet/{chaletId}/plage: Créer une plage de disponibilité pour le chalet {chaletId}
- Créer le code client permettant d'effectuer les opérations avec le serveur
- Voir le README.md du serveur pour le format JSON entre le client et le serveur
