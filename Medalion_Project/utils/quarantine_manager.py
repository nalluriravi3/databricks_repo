class QuarantineManager:

    @staticmethod
    def write_quarantine(df, quarantine_table):

        df.write \
            .format("delta") \
            .option("mergeSchema", "true") \
            .mode("append") \
            .saveAsTable(quarantine_table)