# Bienvenue sur le back-end de Sape !

Le projet estl livré avec une configuration docker complète il suffit juste de créer un fichier .env avec les différentes variables complétées :
Le projet démarre sur le port **8003** pour Django et **5436** pour la base de donnée. 
Un adminer est également fourni pour consulter la base de donnée sur le port **9090**.

### Attention les variales ci-dessous sont aussi à modifier dans sape>settings.py en raison d'un soucis d'environnement.
MINIO_ROOT_USER=
MINIO_ROOT_PASSWORD=
MINIO_ENDPOINT=
MINIO_BUCKET_NAME=

### Base de donnée :
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

### Dans le cas où vous utilisiez un Traefik sur votre serveur :
DOMAIN_NAME=
SUBDOMAIN=
