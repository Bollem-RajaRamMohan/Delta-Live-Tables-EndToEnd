import dlt 
from pyspark.sql.functions import *
#CREATING GOLD STREAMING ON TOP OF SILVER STREAMING VIEW(NOT ON MAT VIEW)

@dlt.view(
    name = 'sales_gold_view'
)

def sales_gold_view():
    df = spark.readStream.table('sales_silver_view')
    return df 

dlt.create_streaming_table("fact_sales")

dlt.create_auto_cdc_flow(
    target = "fact_sales",
    source = "sales_gold_view",
    keys = ["sales_id"],
    sequence_by=col("processDate"),
    stored_as_scd_type=1
)
    
    
  