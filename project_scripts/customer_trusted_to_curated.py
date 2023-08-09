import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1691353798161 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_final_trusted",
    transformation_ctx="AmazonS3_node1691353798161",
)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_final_trusted",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Join
Join_node1691353820190 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1691353798161,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1691353820190",
)

# Script generated for node Drop Fields
DropFields_node1691353866286 = DropFields.apply(
    frame=Join_node1691353820190,
    paths=["user", "z", "y", "x", "timestamp"],
    transformation_ctx="DropFields_node1691353866286",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1691425949373 = DynamicFrame.fromDF(
    DropFields_node1691353866286.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1691425949373",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://stedi-udacity/final_data/customer/curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)
S3bucket_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="customer_final_curated"
)
S3bucket_node3.setFormat("json")
S3bucket_node3.writeFrame(DropDuplicates_node1691425949373)
job.commit()
