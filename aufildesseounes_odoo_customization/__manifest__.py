# Copyright 2024 Boris Gallet ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "aufildesseounes_odoo_customization",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Boris Gallet",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Customization for aufildesseounes’s Odoo",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "website_event",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/event_templates_page_registration.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}