import os
import psutil
import argparse

ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--debug", required=False, default='0',
#                 help="enable debug mode")
ap.add_argument("-u", "--usage_percent", required=False, default=80.0,
                help="cpu usage percentage")
ap.add_argument("-d", "--direction", required=False, default='less_than',
                help="greater_than or less_than")
ap.add_argument("-t", "--restart-in-second", required=False, default="1",
                help="shutdown in x seconds")
args = vars(ap.parse_args())

# print("The CPU usage is : ", cpu_usage)
cpu_usage = psutil.cpu_percent(4)
print('The CPU usage is: ', cpu_usage)

if args['direction'] == 'greater_than':
    if cpu_usage > float(args['usage_percent']):
        # 80.0 by default
        print(f"restart in {args['restart-in-second']} seconds")
        os.system(f"restart /r /t {args['restart-in-second']}")

# default condition
if args['direction'] == 'less_than':
    if cpu_usage <= float(args['usage_percent']):
        # 80.0 by default
        print(f"restart in {args['restart-in-second']} seconds")
        os.system(f"restart in {args['restart-in-second']} seconds")
