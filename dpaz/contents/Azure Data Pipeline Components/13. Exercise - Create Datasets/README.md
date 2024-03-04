<details open>

<summary><b>Change 1:</b> Replace the entire content to this</summary>

In this exercise, you will be creating the Datasets in Azure Data Factory for the following data sources:

1. SalesOrderHeader, Customer database tables on the SQL Database
2. SalesOrderHeader, Customer database external tables on Synapse built-in SQL Pool (Note: Use scripts below to create the SalesOrderHeader, Customer tables in Synapse before attempting to create the datasets in ADF)

## How to Create EXTERNAL Tables in Synapse Analytics Workspace

### Step 1. Create a storage and directories in data lake 

in your Azure Data Lake Storage:

- Create a storage 
- Create directories in that will store the final tables' data.

You may name these directories `customer` and `sales_order_header`, the same names as your tables but with a different naming convention.

### Step 2. Create a serverless database in Azure Synapse Analytics

Open up your Synapse Analytics, and then create a new serverless database.

### Step 3. Prepare an external file format and an external data source

Create an SQL query document. Copy-paste the following queries and run them in the serverless database you've just created:

```
-- Use the same file format as used for creating the External Tables during the LOAD step.
IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat')
   CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat]
   WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
          FORMAT_OPTIONS (
            FIELD_TERMINATOR = ',',
            USE_TYPE_DEFAULT = FALSE,
            FIRST_ROW = 2
           ))
GO


-- Storage path where the result set will persist
IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'ExtDataSource')
   CREATE EXTERNAL DATA SOURCE [ExtDataSource]
   WITH (
       LOCATION = 'abfss://synapsefilesystem1@synapsestorageacct1.dfs.core.windows.net'
   )
GO
```

The above queries do two things:

- Create an external file format called `SynapseDelimitedTextFormat` if it doesn't already exist. This file format will be used to read the data from storage directories.
- Create an external data source called `extDataSource` if it desn't already exist. It reads data from a container filesystem `synapsefilesystem1` in the storage account `synapsestorageacct1`. Please update the path according to your settings.

**Note:** Make sure to pick the database you have just created in the previous step or your queries won't run. This applies for other Synapse Analytics queries as well.

![Pick the appropriate database](usedb.png)

### Step 4. Create external tables

Create external tables that are connected to the appropriate directories in the external data sources you have specified above.

```
CREATE EXTERNAL TABLE SalesOrderHeader(
[SalesOrderID] [int],
[RevisionNumber] [tinyint],
[OrderDate] [datetime],
[DueDate] [datetime],
[ShipDate] [datetime],
[Status] [tinyint],
[OnlineOrderFlag] [BIT],
[SalesOrderNumber]  [nvarchar](23),
[PurchaseOrderNumber] [nvarchar](23),
[AccountNumber] [nvarchar](23),
[CustomerID] [int],
[ShipToAddressID] [int],
[BillToAddressID] [int],
[ShipMethod] [nvarchar](50),
[CreditCardApprovalCode] [varchar](15),
[SubTotal] [money],
[TaxAmt] [money],
[Freight] [money],
[TotalDue] [money],
[Comment] [nvarchar](1000),
[rowguid] [uniqueidentifier],
[ModifiedDate] [datetime]
)
WITH (
   LOCATION = '/sales_order_header/',
   DATA_SOURCE = [ExtDataSource],
   FILE_FORMAT = [SynapseDelimitedTextFormat]
)
GO

CREATE EXTERNAL TABLE Customer(
    [CustomerID] [int],
    [NameStyle]  [bit],
    [Title] [nvarchar](8),
    [FirstName] [nvarchar](128),
    [MiddleName] [nvarchar](20),
    [LastName] [nvarchar](128),
    [Suffix] [nvarchar](10),
    [CompanyName] [nvarchar](128),
    [SalesPerson] [nvarchar](256),
    [EmailAddress] [nvarchar](50),
    [Phone] [nvarchar](20),
    [PasswordHash] [varchar](128),
    [PasswordSalt] [varchar](10),
    [rowguid] [uniqueidentifier],
    [ModifiedDate] [datetime]
)
WITH (
   LOCATION = '/customer/',
   DATA_SOURCE = [ExtDataSource],
   FILE_FORMAT = [SynapseDelimitedTextFormat]
)
GO
```

To verify that the tables are created properly, you may run a SELECT code on your database and verify that you get an empty table e.g.

![Output of a properly set up external table](external-tables-correct.png)

</details>