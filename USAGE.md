# Using the dev VM

Assuming you have configured the VM and your device.

## Deploying NaaVRE

### Quick start

Deploy from your device:

```shell
git clone https://github.com/NaaVRE/NaaVRE-helm
cd NaaVRE-helm
./deploy.sh repo-add
./deploy.sh --kube-context minikube -n new-naavre install-keycloak-operator
./deploy.sh --kube-context minikube -n new-naavre -f values/values-deploy-minikube.yaml upgrade --install
```

Check the deployment status and wait for completion:

```shell
watch kubectl --context minikube -n new-naavre get po
# OR
k9s --context minikube -n new-naavre
```

Open NaaVRE: https://naavre-dev.minikube.test/

To reset a deployment, and get back to a clean state, it is often sufficient to delete the namespace:

```shell
kubectl --context minikube delete namespace new-naavre
```

If cluster-level resources were created and also need to be reset, use `sudo systemctl stop minikube.service` (see [Managing the minikube cluster](#managing-the-minikube-cluster)).

### More info

Go to [NaaVRE-helm](https://github.com/NaaVRE/NaaVRE-helm).

## Managing the minikube cluster

Minikube is started by systemd. You can manage it using the usual systemd commands on the VM. To view the status and logs:

```shell
sudo systemctl status minikube.service
sudo journalctl -u minikube.service -f
```

To reset the minikube cluster (everything will be deleted):

```shell
sudo systemctl stop minikube.service
sudo systemctl start minikube.service
```

Alternatively, you can use the `minikube` command:

```console
ubuntu@naavre-dev-sam-1:~$ minikube status
ubuntu@naavre-dev-sam-1:~$ minikube stop
ubuntu@naavre-dev-sam-1:~$ minikube delete
```

**Pitfall:** always _start_ the cluster with `sudo systemctl start minikube.service`. Do not use `minikube start`, as the created cluster will not have the appropriate configuration to allow kubectl and ingress access through WireGuard.

## Switching kubeconfig contexts

The kubeconfig file imported from the VM defines the `minikube` context, but does not activate it by default.

To control the cluster, it is recommended to set the context explicitly on each command:

```shell
kubectl --context minikube ...
k9s --context minikube
helm --kube-context minikube
```

It is also possible to use this context by default: `kubectl config use-context minikube`.

**Pitfall**: if you manage several contexts, setting a default one with `use-context` is risky. This is because there is no visible indication of the active context in the shell prompt by default. This makes it easy run a command against `production-1` while intending to run it against `minikube`, and wipe your production. If you have several contexts and are not feeling reckless, run `kubectl config unset current-context` and use explicit contexts instead.
