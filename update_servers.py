import os

DYNAMIC_FILE_PATH = os.getenv('DYNAMIC', '') if os.getenv('DYNAMIC', '') else \
    input("Please enter full path to the dynamic.yaml file\n")
DOCKER_COMPOSE_FILE_PATH = os.getenv('DOCKER_COMP', '') if os.getenv('DOCKER_COMP', '') else \
    input("Please enter full path to the docker-compose.yml file\n")
SERVERS = os.getenv('SERVERS', '') if os.getenv('SERVERS', '') else input("Please enter the servers, "
                                                                          "separate them with ','")


def check_if_http_in_server(server):
    if 'http://' in server or 'https://' in server:
        return True


def update_servers_list(servers):
    updated_servers = []

    for server in servers.split(','):
        if check_if_http_in_server(server):
            updated_servers.append(server)
        else:
            updated_servers.append(f'http://{server}')

    return updated_servers


def update_dynamic_file(updated_servers_list, dynamic_file_path):
    with open(dynamic_file_path, 'a') as f:
        if updated_servers_list:
            for server in updated_servers_list:
                if check_if_http_in_server:
                    f.write(f'          - url: "{server}"\n')


def update_docker_compose_file(updated_servers_list, docker_compose_file_path):
    with open(docker_compose_file_path, 'r+') as f:
        if updated_servers_list:
            server_list = ','.join(updated_servers_list)
            old_file = f.read()
            new_file = old_file.replace('<SERVERS>', server_list)

    with open(docker_compose_file_path, 'w') as f:
        if new_file:
            f.write(new_file)


def main():
    updated_servers_list = update_servers_list(SERVERS)

    update_dynamic_file(updated_servers_list, DYNAMIC_FILE_PATH)
    update_docker_compose_file(updated_servers_list, DOCKER_COMPOSE_FILE_PATH)


if __name__ == "__main__":
    main()
