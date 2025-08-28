🚀 Delta Live Tables End-to-End (Medallion Architecture)

This project demonstrates an end-to-end data pipeline using Databricks Delta Live Tables (DLT), following the Medallion Architecture (Bronze → Silver → Gold). It showcases how to build scalable, streaming-first pipelines with built-in data quality, transformations, and automated change data capture (CDC).

🏗️ Architecture

                Cloud Storage (Source Files)
                          │
                          ▼
        ┌───────────── Bronze Layer ─────────────┐
        │ Raw data ingestion via Streaming Tables│
        │ using Cloud Files Auto Loader           │
        └────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────── Silver Layer ─────────────┐
        │ Materialized Views with                │
        │ cleansing, transformations & business  │
        │ logic applied                          │
        └────────────────────────────────────────┘
                          │
                          ▼
        ┌────────────── Gold Layer ──────────────┐
        │ Curated Streaming Tables for            │
        │ analytics, reporting & downstream apps │
        └────────────────────────────────────────┘
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
