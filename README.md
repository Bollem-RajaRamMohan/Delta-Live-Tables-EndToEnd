🚀 Delta Live Tables End-to-End (Medallion Architecture)

This project demonstrates an end-to-end data pipeline using Databricks Delta Live Tables (DLT), following the Medallion Architecture (Bronze → Silver → Gold). It showcases how to build scalable, streaming-first pipelines with built-in data quality, transformations, and automated change data capture (CDC).

🏗️ Architecture

![Medallion Architecture](Flowchart/A_flowchart_diagram_illustrates_the_Medallion_Arch.png)

✨ Features

✅ Bronze Layer:

Ingests raw files using Databricks Auto Loader (Cloud Files format)

Creates streaming Delta tables for incremental processing

✅ Silver Layer:

Implements materialized views for transformations

Cleans, standardizes, and enriches the raw data

✅ Gold Layer:

Produces streaming tables optimized for BI, ML, and reporting

Business-ready curated datasets

✅ Auto CDC Implementation:

Supports Slowly Changing Dimensions (SCD) Type 1 & Type 2

Automatically tracks updates & maintains historical records

⚙️ Tech Stack

Databricks Delta Live Tables (DLT)

Medallion Architecture

Auto Loader (Cloud Files)

Delta Lake

Streaming Pipelines

CDC (SCD Type 1 & Type 2)
