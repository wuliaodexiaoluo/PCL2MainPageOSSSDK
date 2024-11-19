import asyncio
import Setup
import os
import sys
from loguru import logger
import locale
import re

language = locale.getdefaultlocale()[0]

# 初始化数据

# 登录用户名
username = os.environ["PCL2MPOSSUsername"]

# 登录密码
password = os.environ["PCL2MPOSSUsername"]

# 是否为限制输入环境
lmtin = False

# API 根地址
apiroot = os.environ["PCL2MPOSSAPIROOT"]

# API 端口
serverport = os.environ["PCL2MPOSSSERVERPORT"]

localdir = os.environ["PCL2MPOSSDIR"]
remote = apiroot + "/"

for arg in sys.argv[1:]:
        match arg:
            case re.fullmatch(r"--username=(.*)", arg) | re.fullmatch(r"--username (.*)", arg) | re.fullmatch(r"-username=(.*)", arg) | re.fullmatch(r"-username (.*)", arg):
                if "=" in arg:
                    username = arg.split("=")[1]
                else:
                    username = arg.split(" ")[1]
            case re.fullmatch(r"--password=(.*)", arg) | re.fullmatch(r"--password (.*)", arg) | re.fullmatch(r"-password=(.*)", arg) | re.fullmatch(r"-password (.*)", arg):
                if "=" in arg:
                    password = arg.split("=")[1]
                else:
                    password = arg.split(" ")[1]
            case re.fullmatch(r"--limit-input=(true|false)", arg) | re.fullmatch(r"--limit-input (true|false)", arg) | re.fullmatch(r"-limit-input=(true|false)", arg) | re.fullmatch(r"-limit-input (true|false)", arg):
                if "=" in arg:
                    if arg.split("=")[1].lower() == "true":
                        lmtin = True
                else:
                    if arg.split(" ")[1].lower() == "true":
                        lmtin = True
            case re.fullmatch(r"--projectapi=(.*)", arg) | re.fullmatch(r"--projectapi (.*)", arg) | re.fullmatch(r"-projectapi=(.*)", arg) | re.fullmatch(r"-projectapi (.*)", arg):
                if "=" in arg:
                    apiroot = arg.split("=")[1]
                else:
                    password = arg.split(" ")[1]
            case re.fullmatch(r"--projectapi=(.*)", arg) | re.fullmatch(r"--projectapi (.*)", arg) | re.fullmatch(r"-projectapi=(.*)", arg) | re.fullmatch(r"-projectapi (.*)", arg):
                if "=" in arg:
                    apiroot = arg.split("=")[1]
                else:
                    password = arg.split(" ")[1]

logger.add("{time}.log",level="DEBUG", rotation="100 MB")

logger.debug("登录流程开始")