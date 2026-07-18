class QuarantineManager:
    @staticmethod
    def quarantine(df,quarantine_table):
        df.write.format("delta")\
                .mode("append")\
                .option("mergeSchema","True")\
                .saveAsTable(quarantine_table)