
import numpy as np
import cv2 as cv
import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import time as time
import datetime
from sklearn.cluster import DBSCAN


def postal_vote(first_name, surname, postcode, date_of_birth,
               home_address1, home_address2, home_address3,
               telephone , email, 
               ballot_address1, ballot_address2,ballot_address3,
               ballot_postcode,
               ballot_reason,
               next_election_only,
               postal_path,
               font_path ):
    """
    Populate text on postal vote application form.
    
    first_name: string
    surname: string 
    postcode: string
    date_of_birth: string in form DDMMYYYY
    home_address(n): string, nth line of address
    telephone: int 
    email: string
    ballot_address(n):string, nth line of ballot address
    ballot_postcode: string, postcode for alternate ballot address
    ballot_reason: reason for alternate ballot address
    next_election_only: boolean, if False tick until further notice box, if True set to next election only
    postal_path: file path to postal vote form
    
    
    
    """
    today = time.strftime("%d%m%Y")
        
    large_font = ImageFont.truetype(font_path, 48)
    font = ImageFont.truetype(font_path, 28)
    small_font = ImageFont.truetype(font_path, 18)
    
    image = Image.open(postal_path)
    draw = ImageDraw.Draw(image)

    # draw.text((x, y),"Sample Text",(r,g,b))

    #First name(s) in full
    if len(first_name)<=30:
        draw.text((150, 690),first_name,(0,0,0),font=font)
    else:
        draw.text((150, 690),first_name,(0,0,0),font=small_font)
    #Surname
    if len(surname)<=30:
        draw.text((150, 580),surname,(0,0,0),font=font)
    else:
        draw.text((150, 580),surname,(0,0,0),font=small_font)
    #home_address
    draw.text((150, 810),home_address1,(0,0,0),font=font) 
    draw.text((150, 870),home_address2,(0,0,0),font=font) 
    draw.text((150, 930),home_address3,(0,0,0),font=font)
    #postcode
    draw.text((550, 980),postcode,(0,0,0),font=font)
    #Telephone
    draw.text((150, 1095),telephone,(0,0,0),font=font) 
    
    #Email
    
    if len(email)<=60:
        if len(email)<=30:
            draw.text((140, 1210),email,(0,0,0),font=font)
        else:
            draw.text((140, 1210),email[:30],(0,0,0),font=font)
            draw.text((140, 1270),email[30:],(0,0,0),font=font)
    else:
        draw.text((140, 1210),email[:45],(0,0,0),font=small_font)
        draw.text((140, 1270),email[45:],(0,0,0),font=small_font)
    
    #Until further notice
    if next_election_only == False:
        draw.text((133, 1600),"X",(0,0,0),font=font) 
    
    if next_election_only:
        election_date = '12122019'
        draw.text((180, 1725),election_date[0],(0,0,0),font=font) 
        draw.text((220, 1725),election_date[1],(0,0,0),font=font) 
        draw.text((280, 1725),election_date[2],(0,0,0),font=font) 
        draw.text((320, 1725),election_date[3],(0,0,0),font=font) 
        draw.text((385, 1725),election_date[4],(0,0,0),font=font) 
        draw.text((425, 1725),election_date[5],(0,0,0),font=font) 
        draw.text((465, 1725),election_date[6],(0,0,0),font=font) 
        draw.text((505, 1725),election_date[7],(0,0,0),font=font)
        draw.text((133, 1665),"X",(0,0,0),font=font)

    #Address for ballot paper (if diff from home address)
    draw.text((910, 620),ballot_address1,(0,0,0),font=font) 
    draw.text((910, 680),ballot_address2,(0,0,0),font=font)
    draw.text((910, 730),ballot_address3,(0,0,0),font=font)

    #Postcode for ballot paper (if diff from home address)
    
    draw.text((1330, 785),ballot_postcode,(0,0,0),font=font)

    #Reason 
    if len(ballot_reason)<=60:
        if len(ballot_reason)<=30:
            draw.text((910, 940),ballot_reason,(0,0,0),font=font)
        else:
            draw.text((910, 940),ballot_reason[:30],(0,0,0),font=font)
            draw.text((910, 990),ballot_reason[30:],(0,0,0),font=font)
    else:
        draw.text((910, 940),ballot_reason[:45],(0,0,0),font=small_font)
        draw.text((910, 990),ballot_reason[45:],(0,0,0),font=small_font)

    #Date of birth
    #day
    draw.text((930, 1440),date_of_birth[0],(0,0,0),font=large_font) 
    draw.text((995, 1440),date_of_birth[1],(0,0,0),font=large_font)
    #month
    draw.text((1100, 1440),date_of_birth[2],(0,0,0),font=large_font) 
    draw.text((1165, 1440),date_of_birth[3],(0,0,0),font=large_font) 
    #year
    draw.text((1270, 1440),date_of_birth[4],(0,0,0),font=large_font)
    draw.text((1340, 1440),date_of_birth[5],(0,0,0),font=large_font)
    draw.text((1400, 1440),date_of_birth[6],(0,0,0),font=large_font)
    draw.text((1480, 1440),date_of_birth[7],(0,0,0),font=large_font)

    #Todays date
    #day
    draw.text((1110, 2155),today[0],(0,0,0),font=large_font)
    draw.text((1150, 2155),today[1],(0,0,0),font=large_font)
    #month
    draw.text((1210, 2155),today[2],(0,0,0),font=large_font)
    draw.text((1250, 2155),today[3],(0,0,0),font=large_font)
    #year
    draw.text((1315, 2155),today[4],(0,0,0),font=large_font)
    draw.text((1355, 2155),today[5],(0,0,0),font=large_font)
    draw.text((1390, 2155),today[6],(0,0,0),font=large_font)
    draw.text((1430, 2155),today[7],(0,0,0),font=large_font)
    
    
    return image



def add_signature(postal_form, signature_path, resize = 1):
    """
    Populates signature on postal vote application form
    
    postal_form: output of postal_vote function
    signature_path: path to signature image
    resize = int, must be 1>= resize > 0"""
    
    if resize>1:
        print('Max resize is 1')
    assert(resize<=1)
    
    signature= cv.imread(signature_path)
    
    #take picture threshold to only very dakr pixels
    ret,bw_array = cv.threshold(signature,80,255,cv.THRESH_BINARY)
    bw_signature =Image.fromarray(bw_array)
    
    
    #makes dataframe of non white pixels for removal of stray black pixels
    height = bw_array.shape[0]
    width = bw_array.shape[1]

    im_list=[]
    for i in range(height):
        for j in range(width):
            if bw_array[i][j][0] == 0:
                im_list.append([i,j])
    as_tab=pd.DataFrame(im_list)
    as_tab.columns=['height', 'width']
    
    
    #identify  rogue black pixels with dbscan 
    #dbscan checks if black pixels isnt close to at least 5 other black pixels in
    #a 3 pixel (if this is pixel wont be assigned to cluster)
    dbscan = DBSCAN(eps = 3, min_samples = 5)
    dbscan.fit(as_tab[['width','height']])
    as_tab['labels'] = dbscan.labels_
    
    
    #find height and width of signature, crop it
    max_h = max(as_tab[as_tab.labels!=-1]['height'])
    min_h = min(as_tab[as_tab.labels!=-1]['height'])
    max_w =max(as_tab[as_tab.labels!=-1]['width'])
    min_w = min(as_tab[as_tab.labels!=-1]['width'])
    
    #crop signature
    bw_sig_cropped = Image.fromarray(bw_array[min_h:max_h,min_w:max_w])

    #identify height, width (to be used to insert image into form)
    height = max_h-min_h
    width = max_w - min_w

    #height of signature box  is 190 pixels , i expect height is better restrictor than width
    #set height to 190 * scaling factor
    crop_height = round(190*resize)
    if crop_height%2==1:
        crop_height=crop_height-1
    #set width to preserve ratio of width to height given new height dimension
    crop_width = round(width/(height/crop_height))
    if crop_width%2==1:
        crop_width=crop_width-1
    
    if crop_width>620:
        return add_signature(postal_form, signature_path, resize = resize*.85)
     
    #resize signature
    bw_resized = bw_sig_cropped.resize((crop_width,crop_height), resample=4)
    
    #set resized signature and form as arrays
    sig_array = np.array(bw_resized)
    form_array = np.array(postal_form)
    
    #replace signature box array with siganture array
    half_crop_w= crop_width//2
    half_crop_h= crop_height//2
    form_array[1775-half_crop_h:1775+half_crop_h,1200-half_crop_w:1200+half_crop_w,:] = sig_array
    
    #recast as image
    form_w_signature = Image.fromarray(form_array)
    
    
    return form_w_signature

def export_as_pdf(pdf_name, image):
    """Save image as pdf.
    Do not add .pdf to pdf file name, it is added automatically.

    pdf_name : file name
    image: output from add_signatue"""
    image.save(pdf_name+'.pdf', "PDF" ,resolution=100.0, save_all=True)

