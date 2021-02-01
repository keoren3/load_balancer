import os

dynamic_file_path = os.getenv('DYNAMIC', '') if os.getenv('DYNAMIC', '') else \
    input("Please enter full path to the dynamic.yaml file\n")
docker_compose_file_path = os.getenv('DOCKER_COMP', '') if os.getenv('DOCKER_COMP', '') else \
    input("Please enter full path to the docker-compose.yml file\n")
SERVERS = os.getenv('SERVERS', '') if os.getenv('SERVERS', '') else input("Please enter the servers, "
                                                                          "separate them with ','")

with open(dynamic_file_path, 'a') as f:
    if SERVERS:
        for server in SERVERS.split(','):
            if server:
                f.write(f'          - url: "{server}"\n')

with open(docker_compose_file_path, 'r+') as f:
    if SERVERS:
        old_file = f.read()
        new_file = old_file.replace('<SERVERS>', SERVERS)

with open(docker_compose_file_path, 'w') as f:
    f.write(new_file)
