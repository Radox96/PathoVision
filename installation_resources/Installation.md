# Installation instructions
### In order to install NumPy, Matplotlib and other necessary packages Miniconda needs to be installed. Following instructions are for Python 2.7.x.

To install Miniconda go through following commands in the bash console:
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
