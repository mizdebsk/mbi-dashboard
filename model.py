class Pod:
    def __init__(self, id, name, template, host, started, finished, state, reason, params):
        self.id = id
        self.name = name
        self.template = template
        self.host = host
        self.started = started
        self.finished = finished
        self.state = state
        self.reason = reason
        self.params = params
        self.phase = params.get('phase')
        self.component = params.get('component')


class Phase:
    def __init__(self, name, rpms, repo):
        self.name = name
        self.rpms = rpms
        self.repo = repo


class ModuleBuild:
    def __init__(self, id, name, state, started, finished, pods, srpms, phases, compose):
        self.id = id
        self.name = name
        self.state = state
        self.started = started
        self.finished = finished
        self.pods = pods
        self.srpms = srpms
        self.phases = phases
        self.compose = compose
