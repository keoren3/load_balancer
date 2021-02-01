import os

dynamic_file_path = input("Please enter full path to the dynamic.yaml file\n")
with open(dynamic_file_path, 'a') as f:
    if os.getenv('SERVERS', None):
        for server in os.getenv('SERVERS', None).split(','):
            if server:
                f.write(f'          - url: "{server}"')
