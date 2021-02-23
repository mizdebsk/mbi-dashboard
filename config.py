from os import environ as env
API_URL = f"http://{env.get('ARGO_SERVER')}/api/v1/workflows/{env.get('ARGO_NAMESPACE')}"
