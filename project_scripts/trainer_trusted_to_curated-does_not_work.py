import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Curated
CustomerCurated_node1691417660451 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_final_curated",
    transformation_ctx="CustomerCurated_node1691417660451",
)

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_final_landing",
    transformation_ctx="StepTrainerLanding_node1",
)

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1691422257764 = ApplyMapping.apply(
    frame=CustomerCurated_node1691417660451,
    mappings=[("serialnumber", "string", "right_serialnumber", "string")],
    transformation_ctx="RenamedkeysforJoin_node1691422257764",
)

# Script generated for node Join
Join_node1691417718087 = Join.apply(
    frame1=StepTrainerLanding_node1,
    frame2=RenamedkeysforJoin_node1691422257764,
    keys1=["serialnumber"],
    keys2=["right_serialnumber"],
    transformation_ctx="Join_node1691417718087",
)

# Script generated for node Drop Fields
DropFields_node1691417911741 = DropFields.apply(
    frame=Join_node1691417718087,
    paths=["right_serialnumber"],
    transformation_ctx="DropFields_node1691417911741",
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
StepTrainerTrusted_node3.writeFrame(DropFields_node1691417911741)
job.commit()
