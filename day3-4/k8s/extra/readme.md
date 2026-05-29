```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

``` bash
kubectl patch deployment metrics-server \
  -n kube-system \
  --type='json' \
  -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
  ```


# load sim
```bash
# -n = total requests, -c = concurrent users.
docker run --rm jordi/ab -n 100000 -c 200 http://127.0.0.1:8081
```