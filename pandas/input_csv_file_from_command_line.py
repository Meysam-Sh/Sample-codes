# imports
import os
import pandas as pd
import json

# read the path of CSV file and output file as command-line arguments
sys = os.sys
CSV_file_path = sys.argv[1]
output_path = sys.argv[2]

# save csv file in a dataframe
df = pd.read_csv(CSV_file_path)

hobbies = []
added = []
# each record to a dictionary
for hoby in df.T:
    data = df.T[hoby]
    print(data)
    hobbies.append(data.hoby)
    if data.name not in added:
      dict = {'name' : data.first_name, 'last_name' : data.last_name, 'hobbies' : hobbies}
    added.append(data.name)

# save the dictionary to a JSON file with the path given as a command line argumnet
with open(output_path, 'w') as outfile:
    json.dump(dict, outfile, indent = 2)
outfile.close()

