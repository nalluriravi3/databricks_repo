from pyspark.sql import Row
from datetime import datetime

class AuditManager:

    @staticmethod
    def log_audit(
        spark,
        pipeline_name,
        layer_name,
        table_name,
        start_time,
        end_time,
        records_read,
        records_written,
        records_rejected,
        status,
        error_message
    ):

        audit_row = [Row(
            pipeline_name=pipeline_name,
            layer_name=layer_name,
            table_name=table_name,
            load_start_time=start_time,
            load_end_time=end_time,
            records_read=records_read,
            records_written=records_written,
            records_rejected=records_rejected,
            status=status,
            error_message=error_message
        )]

        audit_df = spark.createDataFrame(audit_row)

        audit_df.write \
            .mode("append") \
            .saveAsTable("workspace.audit_new.audit_log")