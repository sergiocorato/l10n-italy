# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, _


class SplitInvoiceLines(models.TransientModel):
    _name = 'wizard.account.invoice.split.line'
    _description = "Wizard to split invoice lines"

    @api.multi
    def split_invoice_line(self):
        if self.env.context.get('active_ids'):
            invoices = self.env['account.invoice'].browse(
                self.env.context.get('active_ids')
            )
            for invoice in invoices:
                if any(x for x in invoice.invoice_line if len(x.name) > 1000):
                    s = 0
                    for line in invoice.invoice_line.sorted(
                            key=lambda x: (x.sequence or x.id)):
                        s += 1
                        a = 0
                        if len(line.name) > 1000:
                            line_list_985 = \
                                [line.name[i:i + 985] for i in
                                 range(0, len(line.name), 985)]
                            for inv_line985 in line_list_985:
                                a += 1
                                if a == 1:
                                    line.sequence = (line.sequence and
                                                     line.sequence + s or s) * 100 + a
                                    continue
                                line.copy(
                                    default={
                                        'name': _('(...follow) %s') % inv_line985,
                                        'sequence': line.sequence + a,
                                        'quantity': 0,
                                        'price_unit': 0,
                                        'price_subtotal': 0,
                                        'product_id': False,
                                        'invoice_id': line.invoice_id.id,
                                    }
                                )
                            line.name = line.name[:985]
                        else:
                            a += 1
                            line.sequence = (line.sequence and
                                             line.sequence + s or s) * 100 + a