# -*- coding: utf-8 -*-
# Copyright (c) 2020, GreyCube Technologies and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import make_records

#  is_custom_field=1,
def after_migrate():
    custom_fields = {
        "Delivery Note Item": [
            dict(
                fieldname="set_latest_customer_price",
                label="Set Latest Customer Price",
                fieldtype="Check",
                insert_after="section_break_1",
                translatable=0,
                is_system_generated=0
            ),
        ],
    }
    print("Creating custom fields for app Price feet:")
    for dt, fields in custom_fields.items():
        print("*******\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)
