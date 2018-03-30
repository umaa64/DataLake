from assets.web.app import create_curated_datasets

def lambda_handler(event, context):
	print "calling handler"
	create_curated_datasets()
