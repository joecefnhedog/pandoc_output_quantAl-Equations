# pandoc generated websites for the output of quantum equations.
Using pandoc to generate html pages with output equations coming from the quantAl package. This is then realised using a raspberry pi3 running on fruitOs. NGINX is then used to set up a webserver, which may eventually be balanced over numerous pi's using haproxy.

## setting up nginx remotely
Need to setup nginx when we startup the pi, involves adding a user `www', directories, updating priveleges, send the index.html file, update priveleges of relevant files, restart nginx serer.