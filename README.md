# Taming-Big-Data-with-Apache-Spark-Python

# Installing Apache Spark and Python For linux
https://www.sundog-education.com/spark-python/

# anaconda setup for virtual environment
https://docs.anaconda.com/free/anaconda/install/linux/

# conda environment creation
conda create --name {env_name}
conda create --name mlenv

# conda environment with specific python version
conda create --name {env_name} {python==3.8}
conda create --name mlenv python==3.8

# activate conda environment
conda activate {env_name}

# conda deactivate environment
conda deactivate

# conda environment list
conda info --envs

#run below command to not activate code on startup
conda config --set auto_activate_base false


# command to run spark on movies rating dataset
spark-submit ratings-counter.py
