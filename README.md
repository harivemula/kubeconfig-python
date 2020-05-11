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

## Test the results

```
kubectl get cm,deploy,pods,svc
NAME                                 DATA   AGE
configmap/kubex-sampleconfig         1      101s
configmap/kubex-samplespringconfig   1      101s

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/kubex-kubeconfig-python   1/1     1            1           101s
deployment.apps/kubex-springex            1/1     1            1           101s

NAME                                           READY   STATUS    RESTARTS   AGE
pod/kubex-kubeconfig-python-68c7bbdd77-8zk6x   1/1     Running   0          101s
pod/kubex-springex-6f659bd559-v6zqh            1/1     Running   0          101s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes                ClusterIP   10.96.0.1       <none>        443/TCP          2d6h
service/kubex-kubeconfig-python   ClusterIP   10.107.58.239   <none>        80/TCP           101s
service/kubex-springex            NodePort    10.96.64.202    <none>        8080:30027/TCP   101s
```

```
curl -vs http://<External_IP_of_NodePort_Service>:30027/api/demo
```
Note: In my case i captured this output from minikube, so i have to use minikube ip
```
curl -vs http://192.168.99.103:30027/api/demo
*   Trying 192.168.99.103...
* TCP_NODELAY set
* Connected to 192.168.99.103 (192.168.99.103) port 30027 (#0)
> GET /api/demo HTTP/1.1
> Host: 192.168.99.103:30027
> User-Agent: curl/7.64.1
> Accept: */*
>
< HTTP/1.1 200
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 129
< Date: Mon, 11 May 2020 14:16:15 GMT
<
demo.env.prop:[mydemoenvproperty]
httpProxy:[not set]
httpsProxy:[not set]
demoFileProp:[ValueFromConfig]
ENV_PROP:[justenvprop]
* Connection #0 to host 192.168.99.103 left intact
* Closing connection 0
```

Check the logs of python app pod, this should show something like below

```
kubectl logs -f pod/kubex-kubeconfig-python-68c7bbdd77-8zk6x
Testing PycURL/7.43.0.5 libcurl/7.64.0 OpenSSL/1.1.1d zlib/1.2.11 libidn2/2.0.5 libpsl/0.20.2 (+libidn2/2.0.5) libssh2/1.8.0 nghttp2/1.36.0 librtmp/2.3
---------- Python script variables (ENV, PROP) ------------
dbname:[unitTest-dummy]
API_USER:[test-api-user]
API_PASSWORD:[None]
HTTP_PROXY:[None]
HTTPS_PROXY:[None]
NO_PROXY:[None]

-------------KUBECONFIG SPRING APP Contents-------------
demo.env.prop:[mydemoenvproperty]
httpProxy:[not set]
httpsProxy:[not set]
demoFileProp:[ValueFromConfig]
ENV_PROP:[justenvprop]

-------------JSON Content from Internet------------------
{
    "countries": [
        {
            "name": "Afghanistan",
            "isoCode": "AF"
        },
        {
            "name": "Albania",
            "isoCode": "AL"
        },
        {
            "name": "Algeria",
            "isoCode": "DZ"
      ....
```
