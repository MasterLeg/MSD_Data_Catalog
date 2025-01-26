CREATE SCHEMA IF NOT EXISTS metadata;

CREATE TABLE IF NOT EXISTS metadata.schemas (
    id INT PRIMARY KEY,
    name STRING
);

CREATE TABLE IF NOT EXISTS metadata.tables (
    id INT PRIMARY KEY,
    schema_id INT,
    table_name STRING,
    FOREIGN KEY (schema_id) REFERENCES metadata.schema (id)
);

CREATE TABLE IF NOT EXISTS metadata.datatypes (
    id INT PRIMARY KEY,
    name STRING
);

CREATE TABLE IF NOT EXISTS metadata.datatype_properties (
    id INT PRIMARY KEY,
    name STRING,
    datatype_id INT,
    value STRING,
    FOREIGN KEY (datatype_id) REFERENCES metadata.datatypes (id)
);

CREATE TABLE IF NOT EXISTS metadata.columns (
    id INT PRIMARY KEY,
    column_name STRING,
    table_id INT,
    datatype INT,
    description_ STRING,
    owner_ INT,
    use_case STRING,
    creation_date DATETIME,
    delete_date DATETIME,
    FOREIGN KEY (table_id) REFERENCES metadata.tables (id),
    FOREIGN KEY (datatype) REFERENCES metadata.datatypes (id)
);

CREATE OR REPLACE VIEW metadata.metadata AS
    SELECT *
    FROM metadata.columns
    JOIN metadata.datatypes ON metadata.columns.datatype = metadata.datatypes.id
    JOIN metadata.datatype_properties ON metadata.datatype_properties.datatype_id = metadata.datatypes.id
    JOIN metadata.tables ON metadata.tables.id = metadata.columns.table_id
    JOIN metadata.schemas ON metadata.schemas.id = metadata.tables.schema_id;