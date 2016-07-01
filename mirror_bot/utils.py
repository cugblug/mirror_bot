import yaml
import subprocess


def docker_version_check(current_version):
    data = get('--version')
    docker_version = data[15:20]
    if current_version > docker_version:
        print('请联系mirror_bot开发者升级脚本！')
        exit()
    elif current_version < docker_version:
        print('请更新mirror_bot至最新版本！')
        exit()


def get(action):
    with open('tmp', 'w') as f:
        subprocess.run(
            [
                'docker',
                action
            ],
            stdout=f
        )
    with open('tmp', 'r') as f:
        # print(f.read())
        return f.read()


def read(file):
    with open(file, 'r') as f:
        data = yaml.load(f.read())
    return data


def write(file, data):
    with open(file, 'w') as f:
        f.write(yaml.dump(data))
