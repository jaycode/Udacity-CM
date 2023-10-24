> Add this content before the video

**Note:** The solution video has the following differences compared to the instructions in the previous page:

- It loads the customer trusted data from an S3 bucket. This method is not recommended when you have created a table. Since you have created a table, we may benefit from the metadata that you have created by using a Data Source - Data Catalog Node instead.
- It uses prebuilt Nodes such as the Transform - Join Node and Transform Drop Fields Nodes. While it is okay to use them, keep in mind the following considerations:
  - The more nodes you have, the longer it takes for the Glue Job to run (although not significantly so for very large datasets).
  - Some prebuilt nodes may not behave as consistently as the SQL Query node. For example, the Join node may sometimes produce unexpected results when the parent nodes have duplicate. Amazon may or may not have corrected this feature by now, but it is generally safer to use SQL node.
  - On the other hand, some of these prebuilt nodes offer you quicker data previews and output schema, allowing for a faster development time.
- The last node only loads files into the S3 bucket, and you would need to create the accelerometer_trusted table manually afterwards. This is not ideal, since:
  - We can create the table right away in a Data target node.
  - One of the project rubric items requires you to select the *Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions* option, which means you would need to automatically create the table anyway.
