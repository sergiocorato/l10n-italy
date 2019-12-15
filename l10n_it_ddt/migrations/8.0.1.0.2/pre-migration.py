
from openerp.openupgrade import openupgrade

xmlid_renames = [
    ('omnia_ddt.seq_type_ddt', 'l10n_it_ddt.seq_type_ddt'),
    ('omnia_ddt.seq_ddt', 'l10n_it_ddt.seq_ddt'),
    ('omnia_ddt.ddt_type_ddt', 'l10n_it_ddt.ddt_type_ddt'),
    ('omnia_ddt.carriage_condition_PF', 'l10n_it_ddt.carriage_condition_PF'),
    ('omnia_ddt.carriage_condition_PA', 'l10n_it_ddt.carriage_condition_PA'),
    ('omnia_ddt.carriage_condition_PAF', 'l10n_it_ddt.carriage_condition_PAF'),
    ('omnia_ddt.goods_description_CAR', 'l10n_it_ddt.goods_description_CAR'),
    ('omnia_ddt.goods_description_BAN', 'l10n_it_ddt.goods_description_BAN'),
    ('omnia_ddt.goods_description_SFU', 'l10n_it_ddt.goods_description_SFU'),
    ('omnia_ddt.goods_description_CBA', 'l10n_it_ddt.goods_description_CBA'),
    ('omnia_ddt.transportation_reason_VEN', 'l10n_it_ddt.transportation_reason_VEN'),
    ('omnia_ddt.transportation_reason_VIS', 'l10n_it_ddt.transportation_reason_VIS'),
    ('omnia_ddt.transportation_reason_RES', 'l10n_it_ddt.transportation_reason_RES'),
    ('omnia_ddt.transportation_method_MIT', 'l10n_it_ddt.transportation_method_MIT'),
    ('omnia_ddt.transportation_method_DES', 'l10n_it_ddt.transportation_method_DES'),
    ('omnia_ddt.transportation_method_COR', 'l10n_it_ddt.transportation_method_COR'),
]


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_xmlids(cr, xmlid_renames)
