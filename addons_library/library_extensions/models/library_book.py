from odoo import fields, models


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _inherit = "library.book"

    ######################
    # Fields declaration #
    ######################
    author_id = fields.Many2one(comodel_name="res.partner",
                                required=True,
                                string="Author")

    category_id = fields.Many2many(string="Category", 
                                    comodel_name="library.book.category")