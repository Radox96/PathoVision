# Installation instructions
In order to install NumPy, Matplotlib and other necessary packages Miniconda needs to be installed. Following instructions are for Python 2.7.x.

To install Miniconda go through the following commands in the bash console:
- wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
- chmod a+x Miniconda2-latest-Linux-x86_64.sh
- ./Miniconda2-latest-Linux-x86_64.sh

After having installed Miniconda we can now check for updates with the following command:
- pip install --upgrade pip

It will now either update or tell you it is already the newest version.
After this we can retrieve the needed packages:
- pip install argparse
- pip install matplotlib
- pip install numpy   
- pip install pandas
- pip install pytest
- pip install python-dateutil
- pip install --no-cache-dir scikit-image
- pip install --no-cache-dir scipy

Having retrieved the required packages now we are able to install OpenCV via the following command:
- conda install -c menpo opencv=2.4.11

This will take some time and require a few inputs from you.

And at last we are going to install PlantCV as follows:
First we are going to clone the GitHub Repository into our project folder:
- git clone https://github.com/danforthcenter/plantcv.git
Then changeing our working directory into the new plantcv folde with:
- cd plantcv

And in the end starting the installation with this command:
- python2 setup.py install
