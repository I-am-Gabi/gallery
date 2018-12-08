from django.shortcuts import render
from django.forms import modelformset_factory
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from base64 import b64encode
from .models import Photo  
import boto3  
import os
import uuid

s3 = boto3.resource(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

BUCKET_NAME = "galery-challenge"

def gallery(request):
    bucket_gallery = s3.Bucket(name=BUCKET_NAME) 
    
    # photos = [obj.key for obj in bucket_gallery.objects.all() if Photo.objects.filter(key=obj.key, is_approved=True)]
    photos = []

    for file in bucket_gallery.objects.all(): 
        metadata = s3_client.head_object(Bucket=BUCKET_NAME, Key=file.key)["Metadata"]
        uuid_ = uuid.UUID(metadata["uuid"]) 
        if Photo.objects.filter(key=uuid_, is_approved=True).first():
            params = {'Bucket': BUCKET_NAME, 'Key': file.key}
            photos.append(s3_client.generate_presigned_url('get_object', params)) 

    return render(request, 'photo_gallery/index.html', { 'photos' : photos})

def upload_photo(request): 
    if request.method == 'POST':    
        for file in request.FILES.getlist('files'):   
            content_file = ContentFile(file.read())
            uuid_ = str(uuid.uuid4())
            # key_file = f"{str(uuid_)}.{file.name.split('.')[-1]}" 
            s3.Bucket(BUCKET_NAME).put_object(Key=file.name, 
                Body=content_file, 
                Metadata={'uuid': uuid_}, 
                ACL='public-read')
            photo = Photo.objects.create(key=uuid_, is_approved=False)
        
        messages.success(request, 'Imagem adicionada.')  
        return render(request, 'photo_gallery/uppload.html', {messages: messages})
    elif request.method == 'GET': 
        return render(request, 'photo_gallery/uppload.html', {messages: messages})


#@login_required(login_url='/admin/login/')
def approve(request): 
    bucket_gallery = s3.Bucket(name=BUCKET_NAME) 
    
    if request.method == 'POST':  
        if request.POST.get("desaprovar"):
            uuid_ = request.POST.get("desaprovar") 
            photo = Photo.objects.filter(key=uuid_, is_approved=True).first().update(is_approved=False)
            photo.is_approved = False
        elif request.POST.get("aprovar"): 
            uuid_ = request.POST.get("aprovar") 
            photo = Photo.objects.filter(key=uuid_, is_approved=False).first().update(is_approved=True)
            photo.is_approved = True
        

    photos = []

    for file in bucket_gallery.objects.all():
        metadata = s3_client.head_object(Bucket=BUCKET_NAME, Key=file.key)["Metadata"]
        uuid_ = uuid.UUID(metadata["uuid"]) 

        photo = Photo.objects.filter(key=uuid_).first()
        params = {'Bucket': BUCKET_NAME, 'Key': file.key}
        photos.append({ 
            'url': s3_client.generate_presigned_url('get_object', params),
            'is_approved': photo.is_approved,
            'uuid': uuid_ }) 

    return render(request, 'photo_gallery/approve_dashboard.html', { 'photos': photos }) 