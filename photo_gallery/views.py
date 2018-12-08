from django.shortcuts import render
from base64 import b64encode
from .models import Photo
import boto3  
import os

s3 = boto3.resource(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

BUCKET_NAME = "galery-challenge"

def gallery(request):
    bucket_gallery = s3.Bucket(name=BUCKET_NAME) 

    photos = [obj.key for obj in bucket_gallery.objects.all() if Photo.objects.filter(key=obj.key, is_approved=True)]

    #for obj in bucket_gallery.objects.all():  
    #    if (Photo.objects.filter(key=obj.key, is_approved=True)): 
    #        photos.append(obj.key)

    return render(request, 'photo_gallery/index.html', { 'photos' : photos})

#[obj.key for obj in bucket_gallery.objects.all() if Photo.objects.filter(key=obj.key, is_approved=True)]