print('got')
class State:
    def __init__(self):
        self._components = []
       
    def add_component(self, component):
        self._components.append(component)

    def get_components(self):
        return self._components

class Another:
    def __init__(self):
        print('nupe')        










