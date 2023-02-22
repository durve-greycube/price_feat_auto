from distutils.log import debug
import frappe
import json
from frappe import _
from erpnext.stock.get_item_details import get_item_details


# @frappe.whitelist()
# def get_latest_price_for_get_item_details(args, doc,for_validate=False, overwrite_warehouse=True):
#     args_data=json.loads(args)
#     doc_data=json.loads(doc)
#     print('args_data',args_data)
#     print('doc_data',doc_data)
#     if (args_data and doc_data and len(doc_data['items'])>0 
#     and (args_data['doctype'] in ['Sales Invoice','Sales Order','Quotation']) 
#     and doc_data['items'] and (doc_data['items'][0]['doctype'] in ['Sales Invoice Item','Sales Order Item','Quotation Item'])
#     and  args_data['customer']):
#         custom_rate=fetch_latest_customer_price(args_data['customer'], args_data['item_code'])
#         print('custom_rate',custom_rate)
#         if len(custom_rate)>0:
#             result=get_item_details(args, doc,for_validate, overwrite_warehouse)
#             frappe.msgprint(_("Latest Transaction Rate {0} is applied. It replaces system rate {1}")
#             .format(frappe.bold(custom_rate[0].rate),result.price_list_rate, alert=True))

#             result.price_list_rate=result.price_list_rate
#             return result
#         else:
#             frappe.msgprint(_("No Latest Transaction Rate Found. Hence system rate applied."))
#             return get_item_details(args, doc,for_validate, overwrite_warehouse)    
#     else:
#         frappe.msgprint(_("Not eligibile. Hence system rate applied."))
#         return get_item_details(args, doc)

@frappe.whitelist()
def fetch_latest_customer_price(customer,item_code):
    result=frappe.db.sql("""SELECT child_item.rate  from `tabSales Invoice` as main inner join `tabSales Invoice Item` as child_item 
            on main.name=child_item.parent where main.customer= %s and child_item.item_code = %s 
            and main.docstatus = 1  order by main.posting_date  Desc, main.name Desc limit 1""",(customer,item_code),as_dict=1)
    return result


@frappe.whitelist()
def fetch_all_latest_customer_price(customer, items):
        '''Return Latest Customer Price for all items'''
        last_rates = {}
        items = json.loads(items)
        for row in items:
            row = frappe._dict(row)
            latest_customer_price = fetch_latest_customer_price(customer, row.item_code)
            if len(latest_customer_price):
                latest_customer_price = latest_customer_price[0].rate
            else:
                latest_customer_price = 'Not Found'

            if hasattr(row, 'item_code') and row.item_code:
                if row.set_latest_customer_price:
                        last_rates[(row.idx, row.item_code)] = (row.rate, latest_customer_price)
                else:
                    last_rates[(row.idx, row.item_code)] = (row.rate, f'{latest_customer_price} - Ignored')
        
        rows_msg = ''
        for key, value in last_rates.items():
            if value[0] == value[1]:
                continue
            
            # Color of the Customer Rate
            color = 'red' if value[0] != value[1] else 'black'
            if 'Ignored' in str(value[1]):
                color = 'green'

            rows_msg += f'''
            <tr>
                <td style="border: 1px solid black; text-align: center;">{key[0]}</td>
                <td style="border: 1px solid black; text-align: center;">{key[1]}</td>
                <td style="border: 1px solid black; text-align: center;">{value[0]}</td>
                <td style="border: 1px solid black; text-align: center; color: {color};">{value[1]}</td>
            </tr>
            '''

        if len(rows_msg) == 0:
            rows_msg = '''
                <tr><td colspan="4" style="border: 1px solid black; text-align: center; color: green;">No data to verify</td></tr>
            '''
        table_msg = f'''
            <div><b>Are you sure the values are correct</b></div><br>
            <table style="width: 100%;">
                <thead>
                    <tr>
                        <th style="border: 1px solid; text-align: center;">Row#</th>
                        <th style="border: 1px solid; text-align: center;">Item Code</th>
                        <th style="border: 1px solid; text-align: center;">Set Rate</th>
                        <th style="border: 1px solid; text-align: center;">Customer Rate</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_msg}
                </tbody>
            </table>
        '''
        return table_msg