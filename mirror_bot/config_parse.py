import yaml
import mirror_bot.utils as utils

# TODO: 完成配置文件解析，初步确定内容，镜像名称，地址，上游地址，同步用的drive

"""Temptele
name: ubuntu
driver: rsync
upstream: rsync://mirrors6.tuna.tsinghua.edu.cn/deepin-cd

"""

data = {}

"""
docker run -d -v /mnt/mirror/deepin-cd:/data -v /mnt/log:/log --net=host --name=rsync-deepin-cd --privileged=true mirror-rsync /bin/ash -c "rsync --archive --links --hard-links --times --verbose --timeout=60 --delete --recursive --exclude .~tmp~/ --delete-excluded rsync://mirrors6.tuna.tsinghua.edu.cn/deepin-cd /data >> /log/deepin-cd-$(date "+%Y-%m-%d").log"
"""


def parse(file):
    data = utils.read(file)
    return data