# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

from notebookutils import mssparkutils
import requests
import pandas as pd

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Ambil secret dari Key Vault
BASEURL = mssparkutils.credentials.getSecret(
    "https://testkeyvaultari.vault.azure.net/",   # Vault URI
    "BASEURL"  # secret name
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

BASEURL

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# API endpoint
# https://jsonplaceholder.typicode.com/posts
# https://jsonplaceholder.typicode.com/comments
# https://jsonplaceholder.typicode.com/users
# https://jsonplaceholder.typicode.com/todos
# https://jsonplaceholder.typicode.com/photos
# https://jsonplaceholder.typicode.com/albums
url = f"{BASEURL}/users"

# GET request
response = requests.get(url)

# Pastikan sukses
if response.status_code == 200:
    data = response.json()
    # print(data)
    df = pd.DataFrame(data)
    display(df)
else:
    print(f"Request gagal, status: {response.status_code}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
