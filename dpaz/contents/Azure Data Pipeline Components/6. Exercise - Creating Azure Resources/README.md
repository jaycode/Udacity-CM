<details open>
<summary><b>Change 1:</b> Replace the entire page with the following content.</summary>

In this exercise, you'll create the Azure resources necessary to build data pipelines throughout the course. 

You'll need Contributor, Data Factory Contributor and Storage Blob Contributor roles on the Resource Group. These roles have already been granted to your Udacity federated account.

**Make sure you create all your resources within the same Azure region.**

**Step 1.** Create an Azure SQL Database in Azure Portal. This database will used throughout this course for various exercises.

**Select Sample database under Additional settings.** This database will be used throughout this course. Use Query Editor in the Azure Portal or SQL Server Management Studio to make sure the sample database is created, and you can query the tables SalesOrderHeader and Customer from the `SalesLT` schema.

![Pick **Sample** database from **Additional Settings**](sample-data.png)

**Step 2.** Create an Azure Data Lake Gen 2 storage account, 1 container, and 1 directory called Staging. This Staging folder will be used while creating the pipelines.

**Step 3.** Create a Data Factory V2 resource in the Azure Portal.

**Step 4.** Create Synapse Analytics Workspace and the SalesOrderHeader table.

</details>