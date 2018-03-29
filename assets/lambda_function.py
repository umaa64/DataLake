
from web.app import Create_curated_datasets
def lambda_handler(event, context):
    print "calling handler"
    create_curated_datasets()
