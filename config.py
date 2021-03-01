from os import environ as env
API_URL = f"http://{env['ARGO_SERVER']}/api/v1/workflows/{env['ARGO_NAMESPACE']}"
