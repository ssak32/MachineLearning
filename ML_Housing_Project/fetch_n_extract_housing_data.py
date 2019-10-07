import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_n_extract_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path, exist_ok=True)

    tgz_path = os.path.join(housing_path, "housing.tgz")

    try:
        print("Downloading the file from - {}".format(HOUSING_URL))
        urllib.request.urlretrieve(housing_url, tgz_path)
        print("File downloaded successfully")
    except:
        print("Exception raised while downloading the file")

    # tgz_path = os.path.abspath(tgz_path)
    housing_tgz = tarfile.open(tgz_path)

    try:
        print("Extracting the file - {}".format(tgz_path))
        housing_tgz.extractall(path=housing_path)
        print("File extracted successfully")
    except:
        print("Exception raised while extracting the file")
    finally:
        housing_tgz.close()

#Invoking the method
fetch_n_extract_housing_data()