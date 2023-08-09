import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


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

# Script generated for node SQL Query
SqlQuery1205 = """
select * from cl
WHERE sharewithresearchasofdate IS NOT NULL
"""
SQLQuery_node1691350911480 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1205,
    mapping={"cl": CustomerLanding_node1},
    transformation_ctx="SQLQuery_node1691350911480",
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
S3bucket_node3.writeFrame(SQLQuery_node1691350911480)
job.commit()
