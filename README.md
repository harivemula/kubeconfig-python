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


## Using helm to deploy the applications
Download the Let's encrypt intermediate certificate from (https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem.txt).
Run the below command to add helm repository
```
helm repo add --ca-file lets-encrypt-x3-cross-signed.pem harivemula-harbor https://harbor.galaxy.env2.k8scloud.cf/chartrepo/library
```
Update the helm repo
```
helm repo update
```

If required you may have to run the dependent charts update
```
helm dep update
```

Run the below command to install kubeconfig-python and its dependent chart kubeconfigexample-spring
```
helm install kubex harivemula-harbor/kubeconfig-python
```
