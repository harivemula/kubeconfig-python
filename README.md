# kubeconfig-python
Reading environment and config file using python via kubernetes env var and config maps

For building docker image
```
docker build -t harivemula/kubeconfig-python:0.2 .
```
Push docker image
```
docker push harivemula/kubeconfig-python:0.2
```
To enable HTTP Proxy inside the container use below env variables in deployment

        - name: HTTP_PROXY
          value: <Proxy_URL>
        - name: HTTPS_PROXY
          value: <Proxy URL>
        - name: NO_PROXY
          value: "<No_Proxy IP/URLs comma separated>"
