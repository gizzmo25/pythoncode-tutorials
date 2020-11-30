from tqdm import tqdm
import requests
import sys

# the url of file you want to download, passed from command line arguments
url = sys.argv[1]
# read 1024 bytes every time 
buffer_size = 1024
# download the body of response by chunk, not immediately
response = requests.get(url, stream=True)

# get the total file size
file_size = int(response.headers.get("Content-Length", 0))

# get the file name
filename = url.split("/")[-1]

# progress bar, changing the unit to bytes instead of iteration (default by tqdm)
progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for data in progress:
        # write data read to the file
        f.write(data)
        # update the progress bar manually
        progress.update(len(data))