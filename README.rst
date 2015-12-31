======================
simple-python-drybones
======================

Template pour les projets python simples type script.

Prérequis
=========
pip, virtualenv et virtualenvwrapper doivent être installés.

Procédure
=========
Pour générer un template pour le projet **myapp** :

Création de l'environnement virtuel
-----------------------------------

Pour créer l'environnement virtuel, se placer dans le répertoire d'installation du projet::

    $ mkvirtualenv myapp

Création du projet
-------------------

Pour créer le nouveau projet en utilisant le template::

    $ git clone https://github.com/unistra/simple-python-drybones.git myapp

Le package par défaut s'appelle **myapp**. On pourra le renommer, ainsi que
toutes les références à celui-ci dans les différents fichiers si besoin.

Configuration du projet
-----------------------

Pour configurer le projet dans l'environnement virtuel::

    $ cd myapp
    $ setvirtualenvproject $VIRTUAL_ENV $(pwd)

    # Edition du fichier postactivate
    $ echo "export SETTINGS_MODULE=myapp.settings.dev" >> $VIRTUAL_ENV/bin/postactivate

    # Edition du fichier postdeactivate
    $ echo "unset SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

    # Rechargement de l'environnement virtuel
    $ workon myapp

    # Installation de l'application pour le dev
    $ python setup.py develop

Installation des librairies
---------------------------

Pour installer les librairies ::

    $ cdproject
    $ pip install -r requirements/dev.txt

Tester l'exécution du script python
-----------------------------------

Pour tester l'installation: ::

    $ python myapp/main.py

Déploiement
-----------

Il faut utiliser pydiploy.
