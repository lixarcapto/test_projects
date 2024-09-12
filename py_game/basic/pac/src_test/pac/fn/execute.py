


from ..out_deps import os, subprocess

"""Executes the given Python script.
    Args:
        script_path (str): 
        The path to the Python script file.
    @ by gemini
"""
def execute(script_path:str)->None:
    try:
        # Check if the script file exists
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script file not found: {script_path}")

        # Execute the script using subprocess.run()
        subprocess.run(['python', script_path])

    except Exception as e:
        # Handle any exceptions that occur during execution
        print(f"Error executing script: {e}")