# Postal vote application form (WIP)

The code in this repo can be used to populate a postal vote application form when provided with the necessary text input and an image of a signature on a white back ground. The intention of this code is to provide the back end for a tool that allows a user to populate and submit a postal vote application form using just a smart phone.

### [JUMP TO DEMO](https://github.com/richchad/postal_vote_filler/blob/master/Demo.ipynb)


### Repo files
- 'arial.ttf': the font library used to populate text on form 
- 'postal_vote_application_form.jpg' : jpeg of the postal vote application form 
- 'signature.jpg' : sample signature for demonstration
- 'postal_vote.py' : code base
- 'demo' : demo of functions

### Required libraries
- numpy
- pandas
- PIL
- cv2
- datetime/time
- sklearn


### User notes
#### Signature
The signature must be provided with the correct orientation. The signature is automatically resized to fit the signature box. The signature function includes the option to resize the signature. The requirement for a white background is forgiving, pictures with shadows will still process correctly. The signature must be made using a black pen (blue should also work). 

#### Optional parts of postal vote form
Where parts of the postal vote form are optional an empty string (or string of blank spaces) should be provided as an argument.

#### Word length restriction
There are restrictions on lengths of names and emails etc (i.e. text wont keep to boxes where strings are too long), but exceeding these limits will not throw errors and limits vary depending on characters used (limits are based on using all capital letters, using capital letters only where necessary increases limits by approximately one third). These restrictions should be imposed during submission of info (so if collecting arguments using online form, impose character count in form). Adjusting the text size to accommodate longer strings is a simple change.

#### Input arguements
All arguments are type string, except next_election_only which is type boolean (True or False). Dates must be in form ddmmYYYY, where a day is single digit, it must be expressed as two digits, so 5th of November is "05112019".



### How it works
#### Adding text to form
Coordinates of text boxes have been hard coded. Using the PIL draw feature add text to the form as necessary, in some instances where strings are too long, reduce font size.

#### Processing signature
Take the threshold of the image (pick a darkness threshold on rgb scale, anything  lighter becomes white, anything darker becomes black). Produce a table of the image (x,y coordinate of every black pixel). Using DBScan (a clustering algorithm) identify any black pixels that do not have at least 4 other black pixels in a 3 pixel range (without this step a stray black pixels can result in incorrect crop coordinates). Ignoring the stray black pixels, crop the image using the max and min black pixel coordinates in both directions. Resize image to fit inside signature box, replace signature box with image.


###### Please send comments/questions to rdchadwick64@gmail.com
