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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1691492674989 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_final_landing",
    transformation_ctx="StepTrainerLanding_node1691492674989",
)

# Script generated for node Customer Curated
CustomerCurated_node1691435383648 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_final_curated",
    transformation_ctx="CustomerCurated_node1691435383648",
)

# Script generated for node SQL Query
SqlQuery0 = """
select stl.* from stl
join cc on stl.serialnumber = cc.serialnumber
"""
SQLQuery_node1697558341945 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={
        "stl": StepTrainerLanding_node1691492674989,
        "cc": CustomerCurated_node1691435383648,
    },
    transformation_ctx="SQLQuery_node1697558341945",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.getSink(
    path="s3://stedi-udacity/final_data/step_trainer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="StepTrainerTrusted_node3",
)
StepTrainerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="step_trainer_final_trusted"
)
StepTrainerTrusted_node3.setFormat("json")
StepTrainerTrusted_node3.writeFrame(SQLQuery_node1697558341945)
job.commit()
