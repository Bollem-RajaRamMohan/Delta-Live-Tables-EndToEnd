import dlt 

#INGEST STORES DATA

# @dlt.table(
#     name = 'bronze_sales'
# )
# def ingest_sales():
#     df=spark.readStream.format("cloudFiles")\
#         .option("cloudFiles.format", "csv")\
#         .load("/Volumes/databricksram/bronze/bronze_volume/sales/")
#     return df
    
#INGEST SALES DATA

@dlt.table(
    name = 'sales_bronze'
)
def ingest_sales():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/databricksram/bronze/bronze_volume/sales/")
    return df
    
#INGEST STORES DATA

@dlt.table(
    name = 'stores_bronze'
)
def ingest_sales():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/databricksram/bronze/bronze_volume/stores/")
    return df

#INGEST PRODUCTS DATA

@dlt.table(
    name = 'products_bronze'
)
def ingest_sales():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/databricksram/bronze/bronze_volume/products/")
    return df

#INGEST CUSTOMERS DATA

@dlt.table(
    name = 'customers_bronze'
)
def ingest_sales():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/databricksram/bronze/bronze_volume/customers/")
    return df