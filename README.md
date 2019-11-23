# pandoc generated websites for the output of quantum equations.
Using pandoc to generate html pages with output equations coming from the quantAl package. This is then realised using a raspberry pi3 running on fruitOs. NGINX is then used to set up a webserver, which may eventually be balanced over numerous pi's using haproxy.

## setting up nginx remotely
Need to setup nginx when we startup the pi, involves adding a user `www', directories, updating priveleges, send the index.html file, update priveleges of relevant files, restart nginx serer.

If you have a pi setup running fruitOs, then all you need to do is run
```sudo python setup-website.py```
you will need to change the ip adress (inside the setup-website.py script) accordingly, this can be found by logging into the router. The script will generate the html file using pandoc from a latex file, then ssh into the pi setting up an nginx server displaying the site you just created.

The next step in the project is to link quanTal to the script, then you can change the type of quantum system you are generating equations for.