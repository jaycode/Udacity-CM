# Changes to the [Project Instructions](https://learn.udacity.com/nanodegrees/nd027/parts/cd12441/lessons/b872a5b3-25f5-436a-bf68-c2c35a1ec626/concepts/a9b97ccf-af67-4e99-a10e-41f06ecb15f5) Page

> Include the following content just under the **Project Instructions** section right above the **Requirements** section:

![flowchart](./images/flowchart.png)


> Include the following content at the very bottom of the page before the **Check your work!** section:

The following diagram shows how the tables in this project should be mapped:
![dataset](./images/dataset.png)

## Check your work!

After each stage of your project, check if the row count in the produced table is correct. You should have the following number of rows in each table:

- Landing
  - Customer: 956
  - Accelerometer: 81273
  - Step Trainer: 28680
- Trusted
  - Customer: 482
  - Accelerometer: 40981
  - Step Trainer: 14460
- Curated
  - Customer: 482
  - Machine Learning: 43681

**Hint:** Use Transform - SQL Query nodes whenever you can. Other node types may give you unexpected results.

For example, rather than a Join node, you may use a SQL node that has two parents, then join them through a SQL query.
