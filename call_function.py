from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from config import WORKING_DIR

available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_call_part.args['working_directory'] = WORKING_DIR

    function_name = {
        "get_files_info": lambda: get_files_info(**function_call_part.args),
        "get_file_content": lambda: get_file_content(**function_call_part.args),
        "run_python_file": lambda: run_python_file(**function_call_part.args),
        "write_file": lambda: write_file(**function_call_part.args),
    }

    if function_call_part.name in function_name:
        function_result = function_name[function_call_part.name]()
        # print('FUNCTION CALL PART HAS A NAME AND A FUNCTION IS BEING CALLED')
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    return types.Content(
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
            )
        ],
    )
    