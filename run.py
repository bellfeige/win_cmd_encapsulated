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
ap.add_argument("-a", "--shutdown_argument", required=False, default="/r",
                help="shutdown argument, default is /r /s /l")
ap.add_argument("-t", "--execute_in_second", required=False, default="1",
                help="shutdown /t value")
args = vars(ap.parse_args())

# print("The CPU usage is : ", cpu_usage)
cpu_usage = psutil.cpu_percent(4)

if args['direction'] == 'greater_than':
    if cpu_usage > float(args['usage_percent']):
        # 80.0 by default
        print(f"The CPU usage is: {cpu_usage}")
        print(f"Executing {args['shutdown_argument']} in {args['execute_in_second']} seconds")
        os.system(f"shutdown {args['shutdown_argument']} /t {args['execute_in_second']}")
    else:
        print(f"The CPU usage is: {cpu_usage} < {args['usage_percent']}. Exiting....")
# default condition
elif args['direction'] == 'less_than':
    if cpu_usage <= float(args['usage_percent']):
        # 80.0 by default
        print(f"The CPU usage is: {cpu_usage}")
        print(f"Executing {args['shutdown_argument']} in {args['execute_in_second']} seconds")
        os.system(f"shutdown {args['shutdown_argument']} /t {args['execute_in_second']}")
    else:
        print(f"The CPU usage is: {cpu_usage} > {args['usage_percent']}. Exiting....")
