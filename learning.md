Il arrive parfois que bien lorsqu'on essaie de faire tourner une application Django avec un serveur de base de données PostgreSQL, on se retrouve avec des erreurs de connexion à la base de données. En effet le service peu bien démaré mais la base de données n'est pas prête.

Pour se faire, il faut attendre que le service soit prêt. Pour se faire, on crée une nouvelle application core pour mettre en place une commande. Une commande dans Django est un script personnalisé qui effectue une tâche spécifique.

Pour créer une commande, on va dans le dossier de l'application (core) et on créer un dossier management, à l'intérieur on créer un dossier commands et enfin dans ce dossier on créer un fichier wait_for_db.py

Dans ce fichier on va mettre en place la logique pour vérifier si le service est prêt. Pour récupérer les variables d'environnement, on va les récupérer du fichier .env. Pour se faire on va utiliser la librairie python decouple. Avec le code suivant :

```python
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


```     