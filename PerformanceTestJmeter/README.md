# grafana-dashboards




## Grafana action botton run bash command with simple python webservice via rest

[Screenshot](https://github.com/mehrdad2000/grafana-dashboards/assets/26499665/924261db-123d-4751-ba52-334818fa05f9)

Jmeter > Nod1 > Nod2

1- run ([simple python web server](https://github.com/mehrdad2000/grafana-dashboards/blob/52111b8b725b6a4694a89e7c1bd0060a046d7406/PerformanceTestJmeter/simple_server.py)) on your jmeter server.
```
nohup simple_server.py &
```
2- add this plugin [cloudspout-button-panel](https://grafana.com/grafana/plugins/cloudspout-button-panel) to your grafana 
config this botton to send a get request to your server that run simple_server.py
```
get http://192.168.1.1:8000/c1
```
you can add three botton like this to run different commands.

in this example i have 3 botton that each of them run specific performance test via jmeter.
