> Add this content before the video

**Note:** The solution video has the following differences compared to the instructions on the previous page:

- It loads the customer trusted data from an S3 bucket. This method is not recommended when you have created a table. Since you have created a table, we may benefit from the metadata that you have created by using a Data Source - Data Catalog Node instead.
- The last node only loads files into the S3 bucket; you would need to create the accelerometer_trusted table manually afterwards. The instructions page uses the *Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions* option to automatically create the table as the Glue Job run.
