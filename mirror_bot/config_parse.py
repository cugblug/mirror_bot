import yaml
import mirror_bot.utils as utils

# TODO: 完成配置文件解析，初步确定内容，镜像名称，地址，上游地址，同步用的drive

"""Temptele
name: ubuntu
driver: rsync
upstream: tuna

"""

data = {}


def parse(file):
    data = utils.read(file)
