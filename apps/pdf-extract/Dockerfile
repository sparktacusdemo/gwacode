# get the parent image
FROM python:3.9
 
# copy our local files to the container
COPY . /app

# define the root working directory from the container
WORKDIR /app

# Install required packages in the container
RUN pip install -r requirements.txt
 
# add the path where the training code is located
ENTRYPOINT ["python",  "src/myprogram.py"]
