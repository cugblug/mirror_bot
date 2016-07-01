import mirror_bot.utils as utils
import json


# TODO: 检测容器状态，如果当前没有同步容器运行，则开启下一个同步容器；如果当前容器正在运行，则不做任何动作。

# {"name":"AOSP","is_master":true,"status":"success","last_update":"2016-07-01 05:41:40 +0800","last_update_ts":1467322900,"upstream":"https://android.googlesource.com","size":"unknown"},

# state = {"Status": "running",
#          "Running": true,
#          "Paused": false,
#          "Restarting": false,
#          "OOMKilled": false,
#          "Dead": false,
#          "Pid": 12594,
#          "ExitCode": 0,
#          "Error": "",
#          "StartedAt": "2016-07-01T03:13:19.25860488Z",
#          "FinishedAt": "2016-06-12T14:06:47.484940681Z"}


def get_state(container_ID):
    state = json.loads(utils.get("docker inspect --format=\"{{json .State}}\" %s" % (container_ID)))
    return state


def get_finish_time(container_ID):
    state = get_state(container_ID)
    return state['FinishedAt']


def is_running(container_ID):
    state = get_state(container_ID)
    return state['Running']
