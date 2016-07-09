import sauron
baseDFValidator = sauron.baseDFValidator


# Validator for Dispo Code Files Only
class dispoCodeValidator(baseDFValidator):
    min_row_num = 40
    dispo_code = pv.CharColumnValidator('dispo_code')
    description = pv.CharColumnValidator('description')
