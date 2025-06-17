import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(working_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        try:
            os.makedirs(target_file, exist_ok=True)
        except Exception as e:
            return f'Error: {e}'
        
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return print(f'Error: "{target_file}" is a directory, not a file')
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: could not write to file: {e}"


schema_write_file = types.FunctionDeclaration (
        name="write_file",
        description="Writes to file path, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties = {
                "file_path": types.Schema(
                    type= types.Type.STRING,
                    description="The file path to write to, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write to the file path."
                ),
            },
            required=["file_path", "content"],
        ),
    ) 