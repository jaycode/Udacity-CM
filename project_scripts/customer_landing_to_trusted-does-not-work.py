import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Landing
CustomerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-udacity/final_data/customer/landing/"],
        "recurse": True,
    },
    transformation_ctx="CustomerLanding_node1",
)

# Script generated for node Filter by Opt-in
FilterbyOptin_node1686217371770 = Filter.apply(
    frame=CustomerLanding_node1,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="FilterbyOptin_node1686217371770",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://stedi-udacity/final_data/customer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)
S3bucket_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="customer_final_trusted"
)
S3bucket_node3.setFormat("json")
S3bucket_node3.writeFrame(FilterbyOptin_node1686217371770)
job.commit()
