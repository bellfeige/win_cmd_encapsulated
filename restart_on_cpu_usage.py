import argparse
from win_cmd import win_cmd

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--cpu_usage_percent", required=False, default="80.0",
                help="cpu usage percentage")
ap.add_argument("-d", "--direction", required=False, default='less_than',
                help="cpu usage greater_than or less_than")
ap.add_argument("-a", "--cmd_argument", required=False, default="",
                help="cmd argument")
args = vars(ap.parse_args())

if __name__ == '__main__':
    if args['cmd_argument'] != "":
        sd = win_cmd.Shutdown(argument='/r /t 1')
    else:
        sd = win_cmd.Shutdown(argument=args['cmd_argument'])

    sd.restart_for_cpu_usage(cpu_usage_threshold=args['cpu_usage_percent'], direction=args['direction'])
