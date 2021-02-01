# Load Balancer
A simple load balancer using Traefik.

How to start?
Run the next commands one after the other:
```bash
export SERVERS=<SERVER_LIST> # List of servers that need to get the GET and POST requests.
export DOCKER_COMP=<docker_compose_full_path> # Full path to the docker-compose.yml file
export  DYNAMIC=<dynamic.yaml> # Full path to the dynamic.yaml file

python3 update_servers.py # Update the servers list that will get the POST and GET requests

cd app
docker build -t post_api . # Build the image for the docker-compose
cd ..
docker-compose up -d # Run Traefik from image, raise the post_api from the image we created, and configure load balancing.
```

Current metrics are created using Prometheus, in order to display the metrics in Traefik Pilot, add this line to the docker-compose.yml file:
- "--pilot.token=<Token>"

A token can be created here:
https://pilot.traefik.io/


**Some data on the load balancer:**  
In this link: https://doc.traefik.io/traefik/v1.4/benchmarks/  
You'll be able to see some statistics on Traefik, final line is:  
Traefik can serve 28392 requests/sec.  
on a machine with these specs:  
32 GB RAM  
8 CPU Cores  
10 GB SSD  
Ubuntu 14.04 LTS 64-bit  

The POST requests are handled with Flask (Which sends all the post requests to all the servers)
Flask is configured to run parallel (app.run(host='0.0.0.0', port='5000', **threaded**=True))  
A better solution is to use a Gunicorn in front of the Flask app, but I had no time to make it.  

I'm not sure how many threads Flask can handle parallel (Couldn't find any data online).
Using Gunicorn, you'll be able to achieve 100 requests/sec - Link to tutorial: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04  
Please note that you'll need to make some changes in order for it to fit Traefik (Instead of nginx).

Once you raise the container, Traefik's dashboard can be found in this link:
http://localhost:8080/dashboard/#/

Thanks for reading, feel free to contact me with any question.

**For Testing:**
```bash
docker run --network=load_balancer_traefik-network -p 0.0.0.0:5678:5678 hashicorp/http-echo -text="hello world"
# This command will raise an echo server.
# In order for the containers to approach it, run the command:
export SERVERS=<YOUR_LOCAL_IP_ADDRESS>:5678 # Example: export SERVERS=http://192.168.14.180:5678
```

In order to debug the containers run the command:
```bash
docker logs -f <CONTAINER_NAME> # Example: docker logs -f post_api
```

Thank you for reading.
