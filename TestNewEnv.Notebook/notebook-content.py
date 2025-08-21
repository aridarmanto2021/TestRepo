# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "25e5ada6-c544-4ed7-888b-74cb8a7c2a6f",
# META       "workspaceId": "abb0ad34-7018-48f6-b5c4-a0fbe579c935"
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
