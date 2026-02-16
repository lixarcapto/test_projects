


import os, subprocess

def execute(script_path:str)->None:
    """
    Executes the given Python script.
    """
    try:
        # Check if the script file exists
        if not os.path.exists(script_path):
            raise FileNotFoundError(
                f"Script file not found: {script_path}")
        # Execute the script using 
        # subprocess.run()
        subprocess.run(['python', 
            script_path])
    except Exception as e:
        # Handle any exceptions that 
        # occur during execution
        print(f"Error executing script: {e}")