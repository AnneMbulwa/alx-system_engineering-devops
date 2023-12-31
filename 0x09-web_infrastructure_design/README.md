0x09. Web infrastructure design
-- What to cover.
0. Simple web stack
-Requirements
    1 server
    1 web server (Nginx)
    1 application server
    1 application files (your code base)
    1 database (MySQL)
    1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

    - Required to explain:
What is a server
What is the role of the domain name
What type of DNS record www is in www.foobar.com
What is the role of the web server
What is the role of the application server
What is the role of the database
What is the server using to communicate with the computer of the user requesting the website

>SPOF
>Downtime when maintenance needed (like deploying new code web server needs to be restarted)
>Cannot scale if too much incoming traffic

1. Distributed web infrastructure
-Requirements
    2 servers
    1 web server (Nginx)
    1 application server
    1 load-balancer (HAproxy)
    1 set of application files (your code base)
    1 database (MySQL)

    -Required to explain
• What distribution algorithm your load balancer is configured with and how it works
• Is your load-balancer enabling an Active-Active or Active-Passive setup, explain
the difference between both
• How a database Primary-Replica (Master-Slave) cluster works
• What is the difference between the Primary node and the Replica node in regard to the application

>Where are SPOF
>Security issues (no firewall, no HTTPS)
>No monitoring

2. Secured and monitored web infrastructure
-Requirements
    3 firewalls
    1 SSL certificate to serve www.foobar.com over HTTPS
    3 monitoring clients (data collector for Sumologic or other monitoring services)

    -Required to explain
• What are firewalls for
• Why is the traffic served over HTTPS
• What monitoring is used for
• How the monitoring tool is collecting data
• Explain what to do if you want to monitor your web server QPS

>Why terminating SSL at the load balancer level is an issue
>Why having only one MySQL server capable of accepting writes is an issue
>Why having servers with all the same components (database, web server and
application server) might be a problem

3. Scale up
Requirements
    1 server
    1 load-balancer (HAproxy) configured as cluster with the other one
    Split components (web server, application server, database) with their own
    server
