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

# Script generated for node Join
Join_node1691417718087 = Join.apply(
    frame1=CustomerCurated_node1691435383648,
    frame2=StepTrainerLanding_node1691492674989,
    keys1=["serialnumber"],
    keys2=["serialnumber"],
    transformation_ctx="Join_node1691417718087",
)

# Script generated for node Drop Fields Manually
SqlQuery104 = """
select DISTINCT serialnumber, sensorreadingtime, distancefromobject 
from myDataSource
"""
DropFieldsManually_node1691497037355 = sparkSqlQuery(
    glueContext,
    query=SqlQuery104,
    mapping={"myDataSource": Join_node1691417718087},
    transformation_ctx="DropFieldsManually_node1691497037355",
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
StepTrainerTrusted_node3.writeFrame(DropFieldsManually_node1691497037355)
job.commit()
