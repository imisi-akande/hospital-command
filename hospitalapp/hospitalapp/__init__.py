"""
hospitalapp - Our Opal Application
"""
from opal.core import application
from opal.core import menus

class Application(application.OpalApplication):
    javascripts   = [
        'js/hospitalapp/routes.js',
    ]

    menuitems = [
        menus.MenuItem(
            href="/#/list/", activepattern="/list/",
            icon="fa-table", display="Lists",
            index=0
        ),
        menus.MenuItem(
            href='/pathway/#/add_patient',
            display='Add Patient',
            icon='fa fa-plus',
            activepattern='/pathway/#/add_patient'
        )
    ]

