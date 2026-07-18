from pyspark.sql import Row

class AuditManager:
    @staticmethod
    def write_audit(
            spark,
            batch_id,
            pipeline_name,
            notebook_name,
            start_time,
            end_time,
            status,
            error_message=None):

        duration = int(
            (end_time - start_time).total_seconds()
        )

        audit_df = spark.createDataFrame([
            Row(
                batch_id=batch_id,
                pipeline_name=pipeline_name,
                notebook_name=notebook_name,
                start_time=start_time,
                end_time=end_time,
                duration_seconds=duration,
                status=status,
                error_message=error_message
            )
        ])

        audit_df.write.mode(
            "append").saveAsTable(
                "workspace.audit_new.pipeline_audit")