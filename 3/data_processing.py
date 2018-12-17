# Converting the input format is not at all part of the puzzle, but I like figuring out stuff like this, and its not like I have a shot at the leaderboards. Why not take the time to work on new skills/

# desired output:
# [
#     {
#         "claim_num": 1,
#         "from left": 387,
#         "from top": 801,
#         "width": 11,
#         "height": 22
#     }
# ]

import re
import os
import json

here = os.path.dirname(os.path.realpath(__file__))
# source data
data_file = 'day_3_data.txt'
data_filepath = os.path.join(here, data_file)
output_file = 'data_output.py'
output_filepath = os.path.join(here, output_file)

output = open(output_filepath, "w")
input = open(data_filepath, "r")

for item in input:
    data = dict()
    # each of these lines breaks the input line into its component parts and formats the line as a collection of key, value pairs
    data['claim_num'] = int(re.search('#(.*)@', item).group(1))
    data['from_left'] = int(re.search('@(.*),', item).group(1))
    data['from_top'] = int(re.search(',(.*):', item).group(1))
    data['width'] = int(re.search(':(.*)x', item).group(1))
    data['height'] = int(re.search('x(.*)', item).group(1))
    # have to write this out as json strings
    output.write(json.dumps(data))
    # have to add a comma between elements so it can be easily converted to a list (manually)
    output.write(',')

output.close()
input.close()
print('done')
