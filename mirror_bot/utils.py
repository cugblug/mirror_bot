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


x = '''CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                    NAMES
be6a862ac7be        google/cadvisor:latest   "/usr/bin/cadvisor -l"   5 days ago                              0.0.0.0:8080->8080/tcp   cadvisor
be6a862ac7be        google/cadvisor:latest   "/usr/bin/cadvisor -l"   5 days ago                              0.0.0.0:8080->8080/tcp   cadvisor
be6a862ac7be        google/cadvisor:latest   "/usr/bin/cadvisor -l"   5 days ago                              0.0.0.0:8080->8080/tcp   cadvisor'''


def docker_ps_output_load(input_data):
    tmpdata = input_data.split('\n')
    # print(tmpdata)
    contains_key = [
        'CONTAINER ID',
        'IMAGE',
        'COMMAND',
        'CREATED',
        'STATUS',
        'PORTS',
        'NAMES'
    ]
    data = {
        'contains': []
    }
    for i in tmpdata[1:]:
        contains_data = {}
        prev = tmpdata[0].find(contains_key[0])
        for j in range(1, 7):
            cur = tmpdata[0].find(contains_key[j])
            x = i[prev:cur]
            prev = cur
            contains_data[contains_key[j - 1]] = x.strip()
        contains_data[contains_key[6]] = i[prev:].strip()
        data['contains'].append(contains_data)
    return data


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
        
docker_ps_output_load(x)
