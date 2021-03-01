import requests
from config import ARGO_API_URL, VERSIONS_URL
from model import Pod, Phase, ModuleBuild


def parse_module_build(item):
    name = {
        param['name']: param['value']
        for param in item['spec']['arguments']['parameters']
    }['module']

    pods = [
        Pod(
            id=node.get('id'),
            name=node.get('displayName'),
            template=node.get('templateName'),
            host=node.get('hostNodeName'),
            started=node.get('startedAt'),
            finished=node.get('finishedAt'),
            state=node.get('phase'),
            reason=node.get('message'),
            params={
                param['name']: param['value']
                for param in node['inputs']['parameters']
            },
        )
        for node in item['status'].get('nodes', {}).values()
        if node['type'] == 'Pod'
    ]

    srpms = [pod for pod in pods if pod.template == 'srpm']

    tasks = [template for template in item['spec']['templates'] if template['name'] == 'module'][0]['dag']['tasks']
    phase_names = [repo[:-5] for repo in tasks[0]['dependencies']]
    phases = [
        Phase(
            name=phase,
            rpms=[pod for pod in pods if pod.phase == phase and pod.template == 'rpm'],
            repo=next((pod for pod in pods if pod.phase == phase and pod.template == 'repo'), None),
        )
        for phase in phase_names
    ]

    compose = next((pod for pod in pods if pod.template == 'compose'), None)
    
    return ModuleBuild(
        id=item['metadata']['name'],
        name=name,
        state=item['status'].get('phase'),
        started=item['status'].get('startedAt'),
        finished=item['status'].get('finishedAt'),
        pods=pods,
        srpms=srpms,
        phases=phases,
        compose=compose,
    )


def get_json(url):
    response = requests.get(
        url,
        headers={'Accept': 'application/json"'},
    )
    if response.status_code != 200:
        raise Exception(f"REST API failed with HTTP code {response.status_code}")
    return response.json()


class DAO:
    @property
    def builds(self):
        data = get_json(ARGO_API_URL)
        items = data.get('items') or []
        return [parse_module_build(item) for item in items]

    @property
    def versions(self):
        data = get_json(VERSIONS_URL)
        return data
