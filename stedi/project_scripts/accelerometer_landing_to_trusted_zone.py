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

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1687270306831 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_final_landing",
    transformation_ctx="AccelerometerLanding_node1687270306831",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1686834787398 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-udacity/final_data/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="CustomerTrusted_node1686834787398",
)

# Script generated for node Join
Join_node1686834684510 = Join.apply(
    frame1=CustomerTrusted_node1686834787398,
    frame2=AccelerometerLanding_node1687270306831,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1686834684510",
)

# Script generated for node Drop Fields
DropFields_node1686835397680 = DropFields.apply(
    frame=Join_node1686834684510,
    paths=[
        "serialNumber",
        "shareWithPublicAsOfDate",
        "birthDay",
        "registrationDate",
        "shareWithResearchAsOfDate",
        "customerName",
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithFriendsAsOfDate",
    ],
    transformation_ctx="DropFields_node1686835397680",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node3 = glueContext.getSink(
    path="s3://stedi-udacity/final_data/accelerometer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AccelerometerTrusted_node3",
)
AccelerometerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="accelerometer_final_trusted"
)
AccelerometerTrusted_node3.setFormat("json")
AccelerometerTrusted_node3.writeFrame(DropFields_node1686835397680)
job.commit()
