from os import path

import yaml

from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "config-prabowo.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.CoreV1Api()
        resp = k8s_beta.create_namespaced_config_map(
            body=dep, namespace="staging")
		#resp = k8s_beta.delete_namespaced_config_map(name={name di config}, namespace="staging")
        print("Deployment created. status='%s'" % str(resp))


if __name__ == '__main__':
    main()