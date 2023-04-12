# Serveur
## Rôle
Permet d'effectuer les opérations CRUD pour les réservations
## Requis fonctionnels
- Basé sur le protocole HTTP
1) GET /reservation/{reservationId}: Retourne l'information sur la réservation
2) GET /reservations/{utilisateur}: Retourne toutes les réservations de l'utilisateur
3) POST /reservation: Ajoute une réservation, doit être un administrateur
4) PUT /reservation/{reservationId}: remplace la réservation si elle lui appartient
5) DELETE /reservation/{reservationId}: Supprime la réservation
6) POST /utilisateur: Ajoute un utilisateur
7) GET /reservations: si administrateur, renvoyé toutes les réservations triées par ordre de
reservationId (pas de sort, votre choix d'algorithme)
- le format de communication est JSON
- Un administrateur peut effectuer toutes les opérations
- Un utilisateur régulier peut seulement consulter ou modifier ses propres réservations
- Les réservations devront être persistées dans le répertoire "voute" en format gzip avec la nomenclature:
{reservationId}.res.gz
  - Le format interne sera CSV
- Implémenter un cache pour retourner les informations de réservations plus rapidement
  - Ne pas oublié d'invalider ou modifier le cache lors de modifications
- Le serveur devra persister les utilisateurs à partir de la liste chargée via le sous-système "impex"
  - Les mots de passes ne doivent pas être sauvegardés en clair
    - Utiliser une fonction de hachage pour persister/vérifier le mot de passe
- Lors du lancement du serveur, utiliser le module impex pour initialiser les données initiales
