from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# create materialized view
@dp.materialized_view(name="mv_orders")
def mv_orders():
    df=spark.read.table("dlt.source.orders")
    df=df.withColumn("order_date", to_date(col("order_date"), "MM-dd-yyyy"))
    return df

#create materialized view using above materialized view
@dp.materialized_view(name="mv_enr_orders")
def mv_enr_orders():
    df=spark.read.table("mv_orders")
    return df

#create temporary view
@dp.temporary_view(name="tmpview_enr_orders")
def tmpview_enr_orders():
    df=spark.read.table("mv_enr_orders")
    return df
