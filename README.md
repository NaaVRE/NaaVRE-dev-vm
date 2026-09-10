# NaaVRE development VM

TODO

## Prerequisites

- Ubuntu 26.04
- 200 GiB disk
- 4 vCPU, 8 GB RAM (STD-04C008R)
- Network rules SSH: ...

## Configuring the VM

Run ansible

## Using the VM

### Configure wireguard

```
scp ubuntu@<vm ip>:naavre-dev-vm.conf .

# with nmcli (recommended on Ubuntu and other distributions using network-manager)
nmcli connection import type wireguard file naavre-dev-vm.conf
nmcli con up naavre-dev-vm

# OR with wg-quick
sudo wg-quick up naavre-dev-vm.conf
```

### Configure kubectl on your laptop (optional)

only one context

```
mkdir .kube/
scp ubuntu@<vm address>:config_naavre-dev-vm.yaml .kube/config
```

existing contexts in ~/.kube

```
scp ubuntu@<vm address>:config_naavre-dev-vm.yaml .kube/
KUBECONFIG="$(find ~/.kube -name 'config*.yaml' | paste -sd:)" kubectl config view --flatten > ~/.kube/config
```

switching contexts:

```shell
# List contexts 
kubectl config get-contexts

# Use a context explicitely
kubectl --context <context> do something

# Set default context
kubectl config use-contexts <context>
# This context is used by default
# WARNING: use at your own risk, you might inadvertently wipe your production context
kubectl do something
# Unset default context
# (you realized implicit contexts are dangerous)
kubectl config unset current-context
```

### Access web services

- Deploy ingress rules with domain `naavre-dev.minikube.test`. (the NaaVRE-helm minikube deployment values are already configured to use this domain), or any subdomain of `.minikube.test`.
- Open your browser at https://naavre-dev.minikube.test
- Add a security exception for the self-signed SSL certificate (your browser will warn you about it)

The domain name resolution should work out of the box thanks to the wireguard configuration. IF it doesn't work, add the domains to your `/etc/hosts`, or equivalent on non-Linux systems.

```
192.168.51.2 <subdomain>.minikube.test
192.168.51.2 <other subdomain>.minikube.test
```

(The IP address is hard-coded, but if it does not work as expected, verify that it corresponds to the output of `minikube ip` on the VM.)