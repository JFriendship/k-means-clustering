# Image Segmentation:
I created this project to exhibit k-means clustering on a single image.

## Commands for Running the Dockerfile
### Set the Working Directory
cd ./Image-Segmentation

### Build the Docker Image
docker build -t image-segmentation .

### Run the Docker Image
docker run -d -p 3000:3000 image-segmentation

### Access the webapp
http://localhost:3000/


## Image Used:
The test image used is Hendrik Voogd's "Italian landscape with Umbrella Pines."

This image is under public domain but I thought I would include it incase anyone was interested.

https://commons.wikimedia.org/wiki/File:Hendrik_Voogd_-_Italian_landscape_with_Umbrella_Pines.jpg