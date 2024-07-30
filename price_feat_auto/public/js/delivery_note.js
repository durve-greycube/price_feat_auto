frappe.ui.form.on('Delivery Note', {
    validate (frm) {
        return new Promise(function(resolve, reject) {
            const doc = frm.doc
            frappe.call({
            async: false,
            method: 'price_feat_auto.api.fetch_all_latest_customer_price',
            args: {
                customer: doc.customer,
                items: doc.items
            },
            callback: function (r) {
                const message = r.message
                frappe.confirm(message, 
                    function() {
                        resolve()
                    },
                    function () {
                        reject()
                    }
                )    
            }})
        })
    },
    fetch_latest_customer_price (frm) {
        frm.doc.items.forEach(row => {
            const cdt = row.doctype
            const cdn = row.name
            if (row.item_code){
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
            }
        });
    },
    is_pos: function (frm) {
        if (frm.doc.is_pos==1) {
           setTimeout(() => {
            frm.set_value('update_stock', 0)
           }, 450);
        }
        
    }
})

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