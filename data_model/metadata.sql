CREATE SCHEMA IF NOT EXISTS metadata;

CREATE TABLE IF NOT EXISTS metadata.tables (
    id INT,
    schema_name STRING,
    table_name STRING
);

CREATE TABLE IF NOT EXISTS metadata.datatypes (
    id INT,
    name STRING
);

CREATE TABLE IF NOT EXISTS metadata.datatype_properties (
    id INT,
    name STRING,
    datatype_id INT,
    value STRING
);

CREATE TABLE IF NOR EXISTS metadata.columns (
    id INT,
    column_name STRING,
    datatype INT,
    description_ STRING
    owner_ INT,
    use_case STRING
    creation_date DATETIME,
    delete_date DATETIME
);

CREATE VIEW IF NOT EXISTS metadata.metadata (
    schema_name STRING,
    table_name STRING,
    column_name STRING,
    datatype STRING,
    description_ STRING,
    department STRING,
    use_case STRING,
    version_ INT,
    creation_date DATETIME,
    delete_date DATETIME,
);