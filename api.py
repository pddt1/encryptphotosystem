import re
import requests
import json
import base64

from requests.api import request
import rsacrypto
import numpy as np
from PIL import Image
import time
import os
import ast
BASE="https://test-eflask-crypto.herokuapp.com/"

def makedir(user):
    if not os.path.exists(user):
            os.makedirs(user+'/encrypted')
            os.makedirs(user+'/images')
            os.makedirs(user+'/npy')
def login_verify(user,pw):
    json_data = json.dumps({'username':user,'password':pw})
    response = requests.post(BASE+'users/login',json=json_data)
    if(response.status_code==200):
        # print(response.json())
        return True#, None #,response.json()
    elif(response.status_code==404):
        return False#, None
    
def register_user(user,pw,n,e):
    json_data = json.dumps({'username':user,'password':pw,'n_publickey':n,'e_publickey':e})
    response = requests.post(BASE+'users/register',json=json_data)
    if(response.status_code==200):
        return True
    elif(response.status_code==404):
        return False
    
def getKey(username):
    x = requests.get(BASE+username)
    if(x.status_code==200):
        data=dict(x.json())
        E=data['e_publickey']
        N=data['n_publickey']
        return True,E,N
    elif(x.status_code==404):
        return False,None,None
def postImgae(img,username):
    
    timestr = time.strftime("%Y%m%d%H%M%S")
    makedir(username)
    data = np.asarray(img)
    _,e,n=getKey(username)
    if(_==False): return False
    enc_img, enc = rsacrypto.encrypt(data, e, n)
    image1 = Image.fromarray(enc_img, 'RGB')
    image1 = image1.save(username+"/encrypted/"+timestr+".png")
    np.save(username+"/npy/"+timestr+".npy", enc)
    files = {
    'file': open(username+"/npy/"+timestr+".npy", "rb"),
    }
    response = requests.post(BASE+username+'/'+timestr+'.png/',files=files)
    print(response.status_code)
    if(response.status_code==200):
        return True,username+"/encrypted/"+timestr+".png"
    elif(response.status_code==404):
        return False


def retriveimages(username):
    x = requests.get(BASE+username+'/images_list/')
    print(x.status_code)
    if(x.status_code==200):
        data=x.json()['names']
        data=ast.literal_eval(data)
        return True,data
    elif(x.status_code==404):
        return False,None

def downloadAImage(imgname,url,username):
    request=requests.get(BASE+username+'/'+imgname+'/')
    
    open(url+'/'+imgname.split('.',1)[0]+'.npy', 'wb').write(request.content)

    print(request.status_code)
    if(request.status_code==200):
        return True
    elif(request.status_code==404):
        return False

def downloadAll(url,username):
    request=requests.get(BASE+username+'/images/')
    chunk_size=128
    with open(url+'/Images.zip','wb') as fd:
        for chunk in request.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    print(request.status_code)
    if(request.status_code==200):
        return True
    elif(request.status_code==404):
        return False

def decrypt(npy_url,save_url,D,username):
    data=np.load(npy_url)
    _,e,N=getKey(username)
    
    if(_==False): return False
    
    try:
        raw=rsacrypto.decrypt(data,D,N)
        image1 = Image.fromarray(raw, 'RGB')
        image1 = image1.save(save_url+'/'+(npy_url.split('/')[-1]).split('.')[0]+'.png')
        return True
    except:
        return False
    
def shareImg(imgname,D,username,receiver):
    request=requests.get(BASE+username+'/'+imgname+'/')
    
    open(username+"/npy/"+imgname.split('.',1)[0]+".npy", 'wb').write(request.content)
    data=np.load(username+"/npy/"+imgname.split('.',1)[0]+".npy",allow_pickle=True)
    _,e,N=getKey(username)
    
    if(_==False): return False
    
    try:
        raw=rsacrypto.decrypt(data,D,N)
        image1 = Image.fromarray(raw, 'RGB')
        isDone=postImgae(image1,receiver)
        if isDone:
            print("success")
            return True
        else: return False
    except:
        return False
