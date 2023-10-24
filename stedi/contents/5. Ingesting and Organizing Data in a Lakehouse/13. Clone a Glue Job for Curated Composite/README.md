> Change 1: Replace the image

![Clone Job](1-clone.png)

> Change 2: Update the **Modify the Job** section

### Modify the Job
- Update the SQL Query transform to get only customer fields.
- Rename the last Node to Customer Curated.
- Change the destination to the /customer/curated/ subdirectory of the S3 bucket
- Change the destination table name.
- Run the job
- Save the generated python as `customer_trusted_to_curated.py` in the workspace below.
- **Keep** your Glue Table and S3 bucket for the customer curated zone when you are done with this exercise.
