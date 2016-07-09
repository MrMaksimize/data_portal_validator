import pandas_validator as pv

# Validator Class
class baseDFValidator(pv.DataFrameValidator):
    min_row_num = None
    ## Override the class to allow a min row number
    def _check_dataframe_size(self, df):
        if self.column_num is not None and len(df.columns) != self.column_num:
            raise pv.core.exceptions.ValidationError('DataFrame columns number is not %s'
                                  % self.column_num)

        if self.row_num is not None and len(df.index) != self.row_num:
            raise pv.core.exceptions.ValidationError('DataFrame rows number is not %s'
                                  % self.row_num)

        if self.min_row_num is not None and len(df.index) < self.min_row_num:
            raise pv.core.exceptions.ValidationError('DataFrame rows number less than %s'
                                  % self.row_num)
