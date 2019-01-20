from os import path

import yaml
import kubernetes

from kubernetes import client, config


def main():
    config.load_kube_config()
    k8s_beta = client.CoreV1Api()

    body = kubernetes.client.V1Secret()
    body.metadata = kubernetes.client.V1ObjectMeta(name="secret-test")
    body.string_data = {
        "TWITTER_ACCESS_KEY": "ahax",
        "TWITTER_ACCESS_SECRET": "ahay",
        "TWITTER_CONSUMER_KEY": "test22",
        "TWITTER_CONSUMER_SECRET": "aaaa"
    }

    resp = k8s_beta.create_namespaced_secret(
        body=body, namespace="staging")
    print("Secret created created. status='%s'" % str(resp))


if __name__ == '__main__':
    main()