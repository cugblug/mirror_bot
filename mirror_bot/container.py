import mirror_bot
import utils


# TODO: 检测容器状态，如果当前没有同步容器运行，则开启下一个同步容器；如果当前容器正在运行，则不做任何动作。

def is_running(container_id):
    data = utils.docker_output_load()
    for i in data:
        if i['CONTAINER ID'] is 'be6a862ac7be':
            return True
    return False
