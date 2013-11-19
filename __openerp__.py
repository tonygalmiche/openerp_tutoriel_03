# -*- coding: utf-8 -*-

# Doc : https://doc.openerp.com/trunk/server/03_module_dev_01/
#       https://doc.openerp.com/trunk/server/03_module_dev_01/#manifest-file-openerp-py

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 03",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 03 
===================================================

Le but de ce module est de montrer la gestion et l'installation automatique des dépendances avec le paramètre 'depends' du fichier '__openerp__.py'

Ce module installe comme exemple 'Social Network' (mail)

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',

  "depends" : ["base","mail"], # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
                               # -> Il peut être interessant de créer un module dont la seule fonction est d'installer une liste d'autres modules
                               # Remarque : La desinstallation du module n'entrainera pas la desinstallation de ses dépendances (ex : mail)

  "init_xml" : [],             # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],             # Liste des fichiers XML à installer pour charger les données de démonstration
  "update_xml" : [],           # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)
  "installable": True,         # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False              # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}





