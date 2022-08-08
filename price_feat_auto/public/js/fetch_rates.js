frappe.ui.form.on(cur_frm.doc.doctype + " Item", {
    price_list_rate: function (frm, cdt, cdn) {
        setTimeout(() => {
            let row = locals[cdt][cdn]
            frappe.call({
                method: "price_feat_auto.api.fetch_latest_customer_price",
                args: {
                    'customer': frm.doc.customer,
                    'item_code': row.item_code
                }
            }).then((r) => {
                console.log(r)
                if (r.message && r.message.length > 0) {
                    let last_rate = r.message[0].rate
                    frappe.model.set_value(cdt, cdn, 'rate', last_rate);
                    frappe.show_alert({
                        message: __('Latest Transaction Rate {0} is applied. It replaces system rate {1}', [last_rate, row.price_list_rate]),
                        indicator: 'green'
                    }, 9);
                } else {
                    frappe.show_alert('No Latest Transaction Rate Found. Hence system rate is not changed.', 9);
                }
            });
        }, 450);
    },
})