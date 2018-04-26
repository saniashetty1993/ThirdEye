import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

imgurl = 'https://clyffordstillmuseum.org/wp-content/uploads/2014/05/Rstumpf__VisitDenver_IMG_6826_web_2x1-1024x512.jpg'
imgbytes = image_helpers.get_image_from_url(imgurl)
rekresp = client.detect_labels(Image={'Bytes': imgbytes })

pprint(rekresp)

