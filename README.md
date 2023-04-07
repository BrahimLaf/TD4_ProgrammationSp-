# TD4_ProgrammationSp-

Ce dépôt contient une collection de fichiers et de scripts utilisés pour gérer et traiter des données. Voici une brève description de chaque fichier dans le dépôt :
Assets

Le dossier assets contient différents fichiers utilisés par les scripts de ce dépôt. Ils comprennent :

- .env : Ce fichier contient les informations de connexion pour RabbitMQ.
- config.py : Ce fichier contient les paramètres de configuration pour les consommateurs et les producteurs de données.
- docker-compose.yml : Ce fichier contient la configuration pour les conteneurs Docker utilisés dans ce dépôt.

Scripts

Le dossier scripts contient les scripts qui effectuent diverses tâches liées à la gestion de données. Ils comprennent :

- data-clean-consumer.py : Ce script lit les données d'une file RabbitMQ et effectue des opérations de nettoyage dessus.
- data-lake-consumer.py : Ce script lit les données d'une file RabbitMQ et les écrit dans un lac de données.
- logs-producer.py : Ce script génère des données de journalisation et les écrit dans une file RabbitMQ.
- server.py : Ce script lance un serveur qui expose une API pour accéder aux données.

Dépendances

Le fichier requirements.txt répertorie les dépendances requises pour exécuter les scripts de ce dépôt. Vous pouvez installer ces dépendances en exécutant pip install -r requirements.txt.
Exécution des scripts

Pour exécuter les scripts de ce dépôt, vous devrez configurer une instance RabbitMQ et configurer les informations de connexion dans le fichier .env. Une fois que vous avez fait cela, vous pouvez démarrer les conteneurs Docker à l'aide du fichier docker-compose.yml. Ensuite, vous pouvez exécuter les scripts en utilisant les commandes suivantes :

python server.py
python logs-producer.py
python data-clean-consumer.py
python data-lake-consumer.py



C'est tout ! Avec ces scripts, vous pouvez gérer et traiter vos données facilement.
