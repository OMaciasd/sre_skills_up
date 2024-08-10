#!/bin/bash
# Actualiza e instala dependencias adicionales si es necesario
sudo apt-get update
sudo apt-get install -y vim

# Obtener el token del nodo maestro
TOKEN=$(ssh vagrant@192.168.56.5 "sudo cat /var/lib/rancher/k3s/server/node-token")

# Instalar k3s en el nodo trabajador
curl -sfL https://get.k3s.io | K3S_URL=https://192.168.56.5:6443 K3S_TOKEN=$TOKEN sh -
