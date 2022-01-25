import argparse

from cmd import Shutdown

ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--debug", required=False, default='0',
#                 help="enable debug mode")
ap.add_argument("-u", "--cpu_usage_percent", required=False, default=80.0,
                help="cpu usage percentage")
ap.add_argument("-d", "--direction", required=False, default='less_than',
                help="cpu usage greater_than or less_than")
ap.add_argument("-m", "--main_cmd", required=True,
                help="main cmd")
ap.add_argument("-a", "--cmd_argument", required=False, default="",
                help="cmd argument")
args = vars(ap.parse_args())

if __name__ == '__main__':
    if args['direction'] != "":
        sd = Shutdown(argument='/r /t 1')
    else:
        sd = Shutdown(argument=args['direction'])

    sd.restart_for_cpu_usage(cpu_usage_threshold=args['cpu_usage_percent'], direction=args['direction'])

