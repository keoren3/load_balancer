# Load Balancer
A simple load balancer using Traefik.

How to start?

1. Enter the directory 'app'.
2. run the command: ```docker build -t post_api .``` - Create the image for the docker-compose file.
3. Go back to the repositories root directory.
4. run the command: ```docker-compose up -d``` - Run Traefik from image, raise the post_api from the image we created, and configure load balancing.  

**Some data on the load balancer:**  
In this link: https://doc.traefik.io/traefik/v1.4/benchmarks/  
You'll be able to see some statistics on Traefik, final line is:  
Traefik can serve 28392 requests/sec.  
on a machine with these specs:  
32 GB RAM  
8 CPU Cores  
10 GB SSD  
Ubuntu 14.04 LTS 64-bit  

The post requests are handled with Flask (Which sends all the post requests to all the servers)
Flask is configured to run parallel (app.run(host='0.0.0.0', port='5000', **threaded**=True))  
A better solution is to use a Gunicorn in front of the Flask app, but I had no time to make it.  

I'm not sure how many threads Flask can handle parallel (Couldn't find any data online).
Using Gunicorn, you'll be able to achieve 100 requests/sec - Link to tutorial: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04  
Please note that you'll need to make some changes in order for it to fit Traefik (Instead of nginx).

Once you raise the container, Traefik's dashboard can be found in this link:
http://localhost:8080/dashboard/#/

Thanks for reading, feel free to contact me with any question.
