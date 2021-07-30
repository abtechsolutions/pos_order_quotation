
{
    'name': 'Point of Sale Quotations',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Save & Load Quotations in Point Of Sale',
    'description': """

This module allows the user to save and load the quotation in pos.

""",
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/assests.xml',
        'views/pos_quotation.xml',
        'data/ir_sequence.xml',
        'views/pos_order.xml',
    ],
    'qweb': [
        'static/src/xml/LoadQuotationButton.xml',
        'static/src/xml/CreateQuotationButton.xml',
        'static/src/xml/SaveQuotationPopUp.xml',
        'static/src/xml/LoadQuotationPopup.xml',
        'static/src/xml/OrderReceipt.xml',
        'static/src/xml/AlertPopups.xml',
    ],
    'installable': True,
}
