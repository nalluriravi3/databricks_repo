class ColumnMapping:
    @staticmethod
    def col_rename(src_df,col_mapping):
        
        for old_col,new_col in col_mapping.items():
            if old_col in src_df.columns:
                src_df=src_df.withColumnRenamed(old_col,new_col)
        
        return src_df
    
