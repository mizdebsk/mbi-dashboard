from os import environ as env
ARGO_API_URL = f"http://{env['ARGO_SERVER']}/api/v1/workflows/{env['ARGO_NAMESPACE']}"
VERSIONS_URL = "http://versions.kos.kjnet.xyz/versions.json"
