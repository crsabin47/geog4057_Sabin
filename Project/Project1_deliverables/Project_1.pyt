

import arcpy

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Project1"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]  # Add the Tool class to the tools list

class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Project1tool"
        self.description = "Create a shape from JSON"

    def getParameterInfo(self):
        """Define the tool parameters."""
        
        # Define the input JSON parameter
        input_json = arcpy.Parameter(
            name='input_json',
            displayName='Input JSON file',  # Corrected 'displayName'
            direction='Input',
            datatype='DEFile',
            parameterType='Required',
        )

        # Define the output feature class parameter
        output_fc = arcpy.Parameter(
            name='output_fc',
            displayName='Output Feature Class',  # Corrected 'displayName'
            direction='Output',
            datatype='DEFile',
            parameterType='Required',
        )

        # Define the workspace parameter
        workspace = arcpy.Parameter(
            name='workspace',
            displayName='Workspace',  # Corrected 'displayName'
            direction='Input',
            datatype='DEWorkspace',
            parameterType='Required',
        )

        # Return all parameters as a list
        params = [input_json, output_fc, workspace]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        # Retrieve parameter values
        input_json = parameters[0].valueAsText
        output_fc = parameters[1].valueAsText
        workspace = parameters[2].valueAsText
        
        # Add your functionality to process the input JSON and output feature class here
        arcpy.AddMessage(f"Processing input JSON: {input_json}")
        arcpy.AddMessage(f"Output will be saved as: {output_fc}")
        arcpy.AddMessage(f"Workspace: {workspace}")
        
        # Example of reading a JSON file (assuming you're importing it)
        # If you want to use the 'input_json', consider the appropriate function to parse and use it
        # You can use arcpy functions to process the data here, like arcpy.JSONToFeatures for example
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and added to the display."""
        return
