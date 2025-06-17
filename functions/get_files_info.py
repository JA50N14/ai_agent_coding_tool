import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = working_dir_abs
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(working_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_data = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            str_line = f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
            dir_data.append(str_line)
        return_str = "\n".join(dir_data)
        return return_str
    except Exception as e:
        return f'Error: {e}'


schema_get_files_info = types.FunctionDeclaration (
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties = {
                "directory": types.Schema(
                    type= types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )  


