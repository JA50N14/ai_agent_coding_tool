import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {e}'
    

schema_get_file_content = types.FunctionDeclaration (
        name="get_file_content",
        description="Reads a file specified by file_path and returns the first {MAX_CHARS} characters, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties = {
                "file_path": types.Schema(
                    type= types.Type.STRING,
                    description="The file path to read a file from, relative to the working directory.",
                ),
            },
        required=["file_path"],
        ),
    ) 

