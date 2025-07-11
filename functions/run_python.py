import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(working_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)

        result = subprocess.run(commands, timeout=30, capture_output=True, text=True, cwd=working_dir_abs)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced"
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration (
        name="run_python_file",
        description="Run a python file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties = {
                "file_path": types.Schema(
                    type= types.Type.STRING,
                    description="The python file to run, relative to the working directory.",
                ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(
                        type=types.Type.STRING,
                        description="Optional arguments to pass to the Python file."
                    ),
                    description="The optional argument(s) to pass to the python file."
                ),
            },
            required=["file_path"],
        ),
    ) 