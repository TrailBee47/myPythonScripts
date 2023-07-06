# ml_datacollector

command to run:
```
python mlDataColloector.py
```
Once the script starts it will give options to select from the comm ports that are available, to select press the number as per the port you want to select.

Once its selected it will wait for the starting of the capture sequence. And when it has finished capturing the data it will ask to give a tag to the file.
It will store the file with this "tag.csv"

Edge Impulse takes this tag or file name directly and tags the data with the file name.

Note: the Script will continue to collect data unless you stop it with the CTRL+C.
Also, the file format from device has to be specified to EdgeImpulse CSV Wizard.
Read the document here: [TinyML Data Acquisition Phase](https://roambee.atlassian.net/wiki/spaces/HWSPC/pages/2369912897/TinyML+Data+Acquisition+Phase)

One can also upload all the files through command line via a tool: edge-impulse-uploader
```
npm install edge-impulse-uploader 
```
### to upload file with command line
```
edge-impulse-uploader filename.csv
```
you might need to input credentials for your account. 
It will ask to select the project to upload the files to.

