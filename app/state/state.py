#class State:
#    def __init__(self):
    #    alive = True
 #       self.__labelValue = "Some Words"

 #   def setLabelValue(self, labelText):
  #      self.__labelValue = labelText

#    def labelValue(self):
#        return self.__labelValue
class State:
    def __init__(self):
        self._components = []
       
    def add_component(self, component):
        self._components.append(component)

    def get_components(self):
        return self._components

    def render_components(self):
      for component in self._components:
        component.render()
        print('rendering')











