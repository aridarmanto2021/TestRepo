# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "8a7c2a6f-74cb-888b-4ed7-c54425e5ada6",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

import wget

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

url = "https://jsonplaceholder.typicode.com/posts"
filename = wget.download(url)

print("\n=== Isi file hasil wget ===")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
