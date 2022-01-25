import os
import psutil


class CMD:
    def __init__(self, main_cmd, argument=''):
        self.main_cmd = main_cmd
        self.argument = argument

    def cmd(self):
        os.system(f"{self.main_cmd} {self.argument}")


class Shutdown(CMD):
    def __init__(self, argument):
        super().__init__(argument)
        self.main_cmd = 'shutdown'
        self.argument = '/r'

    def shutdown(self):
        self.cmd()

    def restart_for_cpu_usage(self, cpu_usage_threshold=80.0, direction='less_than'):
        cpu_usage = psutil.cpu_percent(4)
        print(f"The CPU usage is: {cpu_usage}")

        if direction == 'greater_than':
            if cpu_usage > float(cpu_usage_threshold):
                # 80.0 by default
                print(f"Executing {self.main_cmd} {self.argument}")
                self.shutdown()
            else:
                print(f"The CPU usage is: {cpu_usage} <= {cpu_usage_threshold}. Exiting....")
        # default condition
        elif direction == 'less_than':
            if cpu_usage <= float(cpu_usage_threshold):
                # 80.0 by default
                print(f"The CPU usage is: {cpu_usage}")
                print(f"Executing {self.main_cmd} {self.argument}")
                self.shutdown()
            else:
                print(f"The CPU usage is: {cpu_usage} > {cpu_usage_threshold}. Exiting....")


if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--main_cmd", required=False,
                    help="main cmd")
    ap.add_argument("-a", "--cmd_argument", required=False, default="",
                    help="cmd argument")
    args = vars(ap.parse_args())

    if args['main_cmd'] != "":
        cmd = CMD(args['main_cmd'], argument=args['cmd_argument'])
        cmd.cmd()
    else:
        print('main_cmd is missing')
