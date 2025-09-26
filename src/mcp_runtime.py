class Tool:
    def __init__(self, name, description, parameters, returns, function):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.returns = returns
        self.function = function

class Toolkit:
    def __init__(self):
        self.tools = {}

    def add_tool(self, name, description, parameters, returns, function):
        self.tools[name] = Tool(name, description, parameters, returns, function)

    def call_tool(self, name, parameters):
        if name not in self.tools:
            raise ValueError(f"Tool '{name}' not found.")
        return self.tools[name].function(**parameters)

    def chain_tools(self, tool_names, input_data):
        data = input_data.copy()
        for name in tool_names:
            result = self.call_tool(name, data)
            data.update(result)
        return data
