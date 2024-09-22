from . import __version__ as app_version

app_name = "price_feat_auto"
app_title = "Price Feat Auto"
app_publisher = "GreyCube Technologies"
app_description = "fetch custom price in sales"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/price_feat_auto/css/price_feat_auto.css"
# app_include_js = "/assets/price_feat_auto/js/price_feat_auto.js"

# include js, css files in header of web template
# web_include_css = "/assets/price_feat_auto/css/price_feat_auto.css"
# web_include_js = "/assets/price_feat_auto/js/price_feat_auto.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "price_feat_auto/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Quotation" : "public/js/quotation.js",
"Sales Order" : "public/js/fetch_rates.js",
"Sales Invoice" : "public/js/sales_invoice.js",
"Delivery Note" : "public/js/delivery_note.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "price_feat_auto.install.before_install"
# after_install = "price_feat_auto.install.after_install"
after_migrate = "price_feat_auto.migrate.after_migrate"
# Uninstallation
# ------------

# before_uninstall = "price_feat_auto.uninstall.before_uninstall"
# after_uninstall = "price_feat_auto.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "price_feat_auto.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"price_feat_auto.tasks.all"
# 	],
# 	"daily": [
# 		"price_feat_auto.tasks.daily"
# 	],
# 	"hourly": [
# 		"price_feat_auto.tasks.hourly"
# 	],
# 	"weekly": [
# 		"price_feat_auto.tasks.weekly"
# 	]
# 	"monthly": [
# 		"price_feat_auto.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "price_feat_auto.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "price_feat_auto.event.get_events"
# }
# override_whitelisted_methods = {
# 	"erpnext.stock.get_item_details.get_item_details": "price_feat_auto.api.get_latest_price_for_get_item_details"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "price_feat_auto.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"price_feat_auto.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
