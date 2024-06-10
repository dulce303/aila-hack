import json, boto3, logging
import cfnresponse
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("event: {}".format(event))
    try:
        bucket = event['ResourceProperties']['BucketName']
        logger.info("bucket: {}, event['RequestType']: {}".format(bucket,event['RequestType']))
        if event['RequestType'] == 'Delete':
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(bucket)
            for obj in bucket.objects.filter():
                logger.info("delete obj: {}".format(obj))
                s3.Object(bucket.name, obj.key).delete()

        sendResponseCfn(event, context, cfnresponse.SUCCESS)
    except Exception as e:
        logger.info("Exception: {}".format(e))
        sendResponseCfn(event, context, cfnresponse.FAILED)

def sendResponseCfn(event, context, responseStatus):
    responseData = {}
    responseData['Data'] = {}
    cfnresponse.send(event, context, responseStatus, responseData, "CustomResourcePhysicalID")   
