from odoo import api, fields, models
from odoo.exceptions import ValidationError

class LibraryBookCategory(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book.category"
    _description = "Library Book Category"

    ######################
    # Fields declaration #
    ######################
    name = fields.Char(required=True,
                       string="Book Category Name")
    
    ###############
    # Constraints #
    ###############
    _sql_constraints = [('name_unique', 'unique(name)', 'The book category name must be unique!')]

    '''
        PYTHON CONSTRAINTS
        OR

        @api.constrains('name')
        def _check_unique_book_category_name(self):
            for record in self:
                if record.name:
                    existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
                    if existing:
                        raise ValidationError("The book category name must be unique!")
    '''
