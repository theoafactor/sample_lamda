import json
import boto3



def lambda_handler(event, context):
    # TODO implement
    client = boto3.client("rekognition") 
    # it is a list of events on seun

    ## get the name of the bucket and object
    bucket = event['Records'][0]['s3']['bucket']['name']
   
    # Get the object placed within the bucket 
    photo = event['Records'][0]['s3']['object']['key']
    # it is ok to pull

    response = client.detect_labels(Image = {"S3Object": {"Bucket": bucket, "Name": photo}}, MaxLabels = 3)
    print('Detected labels for ' + event) 
    print()   
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!' + str(event))
    # }

    # Abdulsalam