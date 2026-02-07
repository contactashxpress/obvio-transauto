# ObvioTrans Auto - Site Web Django

Site vitrine pour l'entreprise d'import-export ObvioTrans Auto, spécialisée dans les véhicules tout-terrain, poids lourds et engins BTP.

## Fonctionnalités

- **Page d'accueil** avec showroom de véhicules
- **Page Services** détaillant les services d'import-export
- **Page À Propos** présentant l'entreprise
- **Page Contact** avec formulaire de demande de devis
- **Multilingue** : Français, Anglais, Arabe (avec support RTL)
- **Design responsive** Mobile-first

## Stack Technique

- **Backend** : Python 3.x + Django 5.x/6.x
- **Frontend** : HTML5, Tailwind CSS (via CDN), JavaScript
- **Base de données** : SQLite (développement) / PostgreSQL (production)

## Installation

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd obviotransauto
```

### 2. Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer l'environnement (optionnel)

Créer un fichier `.env` à la racine :

```env
DEBUG=True
SECRET_KEY=votre-clé-secrète
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Appliquer les migrations

```bash
python manage.py migrate
```

### 6. Collecter les fichiers statiques (production)

```bash
python manage.py collectstatic
```

### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site est accessible sur http://localhost:8000

## Structure du Projet

```
obviotransauto/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── obviotrans_project/          # Configuration Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── website/                     # Application principale
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── migrations/
    ├── static/
    │   └── website/
    │       ├── css/
    │       │   └── styles.css
    │       └── js/
    │           ├── i18n.js      # Système d'internationalisation
    │           └── main.js
    └── templates/
        └── website/
            ├── base.html        # Template de base
            ├── index.html       # Page d'accueil + Showroom
            ├── services.html    # Page Services
            ├── about.html       # Page À Propos
            └── contact.html     # Page Contact
```

## Déploiement en Production

### Configuration recommandée

1. **Variables d'environnement** :
   - `DEBUG=False`
   - `SECRET_KEY` : Clé secrète sécurisée
   - `ALLOWED_HOSTS` : Domaines autorisés
   - `DATABASE_URL` : URL de la base PostgreSQL (optionnel)

2. **Serveur WSGI** :
   ```bash
   gunicorn obviotrans_project.wsgi:application
   ```

3. **Serveur web** (Nginx exemple) :
   ```nginx
   location /static/ {
       alias /path/to/staticfiles/;
   }
   
   location / {
       proxy_pass http://127.0.0.1:8000;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
   ```

## Internationalisation

Le site supporte trois langues :
- **Français** (fr) - par défaut
- **Anglais** (en)
- **Arabe** (ar) - avec support RTL

La langue est automatiquement détectée selon les préférences du navigateur de l'utilisateur.

## Personnalisation

### Modifier les traductions

Les traductions sont dans `website/static/website/js/i18n.js`.

### Modifier le design

- **Couleurs** : Définies dans la configuration Tailwind dans `base.html`
- **Styles personnalisés** : `website/static/website/css/styles.css`

### Ajouter des véhicules

Modifier le template `website/templates/website/index.html` pour ajouter/modifier les cartes de véhicules.

## Contact

Pour toute question, contactez contact@obviotransauto.com
