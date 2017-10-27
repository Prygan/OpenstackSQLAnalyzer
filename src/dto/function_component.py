from dto.component import Component

class FunctionComponent(Component):
    types = ['compute_api', 'neutron_api', 'nova_image', 'rpc', 'l3-agent', 'vif_driver'] # potentiellement l3-agent

    def __init__(self, name, project, duration, parent_id, trace_id, function_call):
        super(FunctionComponent, self).__init__(name, project, duration, parent_id, trace_id)
        self.function_call = function_call

    def __str__(self):
        result = 'FUNCTION_COMPONENT\n'

        result += super(FunctionComponent, self).__str__()

        result += "Function called : " + self.function_call + '\n'
        for child in self.children:
            result += child.__str__() + '\n'

        return result