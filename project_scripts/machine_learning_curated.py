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

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1691518756567 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_final_trusted",
    transformation_ctx="StepTrainerTrusted_node1691518756567",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1691518847319 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_final_trusted",
    transformation_ctx="AccelerometerTrusted_node1691518847319",
)

# Script generated for node Join
Join_node1691519238020 = Join.apply(
    frame1=StepTrainerTrusted_node1691518756567,
    frame2=AccelerometerTrusted_node1691518847319,
    keys1=["sensorreadingtime"],
    keys2=["timestamp"],
    transformation_ctx="Join_node1691519238020",
)

# Script generated for node SQL Query
SqlQuery81 = """
select DISTINCT serialnumber, distancefromobject, sensorreadingtime, user, x, y, z
from myDataSource
"""
SQLQuery_node1691520649781 = sparkSqlQuery(
    glueContext,
    query=SqlQuery81,
    mapping={"myDataSource": Join_node1691519238020},
    transformation_ctx="SQLQuery_node1691520649781",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://stedi-udacity/final_data/step_trainer/curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)
S3bucket_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="machine_learning_curated"
)
S3bucket_node3.setFormat("json")
S3bucket_node3.writeFrame(SQLQuery_node1691520649781)
job.commit()
