# Encapsulated Windows cmd
restart_on_cpu_usage.py 

"-u", "--cpu_usage_percent", required=False, default="80.0", help="cpu usage percentage")
"-d", "--direction", required=False, default='less_than', help="cpu usage greater_than or less_than")
"-a", "--cmd_argument", required=False, default="", help="cmd argument"

win_cmd.py --main_cmd [main_cmd] --cmd_argument [cmd_argument]

"-m", "--main_cmd", required=True, help="main cmd"

"-a", "--cmd_argument", required=False, default="", help="cmd argument"
