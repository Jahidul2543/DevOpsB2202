
######LETS DO A PROJECT THAT USES BOTO3 AND AWS SERVICE REKOG TO CONVERT ANY PICTURE INTO TEXTS####

# #########lets start by making a function that creates a bucket #########

bucketname='bucket2022abc'

def make_bucket(variable):
    import boto3
    s3=boto3.client('s3')
    response=s3.create_bucket(Bucket=bucketname)
    print(response)

# # make_bucket(bucketname)

# amarbucketnames=["bucketabc21","mohiuddingbucket21","dipbucket21",'bucket2022abc']

def make_buckets(variable):
    import boto3
    s3=boto3.client('s3')

    for bucket in variable:
        response=s3.create_bucket(Bucket=bucket)
        print(response)

# # make_buckets(amarbucketnames)

def delete_bucket(arguments):  
    for x in arguments:
        response=s3.delete_bucket(Bucket=x)
        print(response)
x=["bucketabc21","mohiuddingbucket21","dipbucket21",'bucket2022abc']
# delete_bucket(x)

# make_bucket("mentoringsessionai")
import boto3
s3=boto3.client('s3')
def upload_file_to_s3(filen,keyn,bucketnames):
    s3.upload_file(Filename=filen,Key=keyn,Bucket=bucketnames)

upload_file_to_s3(filen="workhard.jpg",keyn="file/report.jpg",bucketnames="bucket2022abc")

def recognizemypicture():
    rekog=boto3.client('rekognition')
    response=rekog.detect_text(Image={'S3Object':{'Bucket': 'bucket2022abc','Name': 'file/report.jpg'}})
    for x in response["TextDetections"]: 
        print(x['DetectedText'])
    # print(response)
# recognizemypicture()




#########lets do another project that can convert any audio files into text###########
# records=[{a},{b},{c}]
######Sample response from s3 object creation to be sent over to lambda######
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "example-bucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::example-bucket"
          "object": {
          "key": "test%2Fkey",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
} },
        "object": {
          "key": "test%2Fkey",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}

########the lambda code we will create ############
import boto3
import uuid
import json

def lambda_handler(event, context):

    print(json.dumps(event))
    
    record = event['Records'][0]
    
    s3bucket = record['s3']['bucket']['name']
    s3object = record['s3']['object']['key']
    
    s3Path = f's3://{s3bucket}/{s3object}'
    jobName = f'{s3object}--{str(uuid.uuid4())}'
    outputKey = f'transcripts/{s3object}-transcript.json'
    
    client = boto3.client('transcribe')
    
    response = client.start_transcription_job(
        TranscriptionJobName=jobName,
        LanguageCode='en-US',
        Media={'MediaFileUri': s3Path},
        OutputBucketName=s3bucket,
        OutputKey=outputKey
    )
    
    print (json.dumps(response, default=str))
    
    return {
        'TranscriptionJobName': response['TranscriptionJob']['TranscriptionJobName']
    }
    
jsonstuff={"jobName":"ImportantBusiness.mp3.mp3--f9361f1c-971c-4477-98ad-dd160eea9131","accountId":"744451519362","results":{"transcripts":[{"transcript":"Today we will accomplish important business."}],"items":[{"start_time":"0.0","end_time":"0.31","alternatives":[{"confidence":"1.0","content":"Today"}],"type":"pronunciation"},{"start_time":"0.31","end_time":"0.43","alternatives":[{"confidence":"1.0","content":"we"}],"type":"pronunciation"},{"start_time":"0.43","end_time":"0.6","alternatives":[{"confidence":"1.0","content":"will"}],"type":"pronunciation"},{"start_time":"0.6","end_time":"1.06","alternatives":[{"confidence":"1.0","content":"accomplish"}],"type":"pronunciation"},{"start_time":"1.06","end_time":"1.49","alternatives":[{"confidence":"0.9997","content":"important"}],"type":"pronunciation"},{"start_time":"1.49","end_time":"1.97","alternatives":[{"confidence":"1.0","content":"business"}],"type":"pronunciation"},{"alternatives":[{"confidence":"0.0","content":"."}],"type":"punctuation"}]},"status":"COMPLETED"}

for key in jsonstuff["results"]["transcripts"]:
    print(key)
