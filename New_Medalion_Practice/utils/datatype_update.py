from pyspark.sql.functions import col

class DatatypeUpdate:
    @staticmethod
    def update_datatype(src_df,tgt_df):
        tgt_datatypes=dict(tgt_df.dtypes)
        src_datatypes=dict(src_df.dtypes)

        for cname,datatype in tgt_datatypes.items():
            if cname in src_datatypes and datatype!=src_datatypes[cname]:
                src_df=src_df.withColumn(cname,col(cname).cast(tgt_datatypes[cname]))
        return src_df
