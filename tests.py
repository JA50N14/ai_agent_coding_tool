import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# class TestGetFiles(unittest.TestCase):
#     def test_get_files_calculator1(self):
#         print("Results - Current directory:")
#         print(get_files_info("calculator", "."))
#         print("")

#     def test_get_files_calculator2(self):
#         print("Results - 'pkg' directory:")
#         print(get_files_info("calculator", "pkg"))
#         print("")

#     def test_get_files_calculator3(self):
#         print("Results - '/bin' directory:")
#         print(get_files_info("calculator", "/bin"))
#         print("")

#     def test_get_files_calculator4(self):
#         print("Results - '../' directory:")
#         print(get_files_info("calculator", "../"))

# class TestGetFileContent(unittest.TestCase):
    # def test_get_files_calculator1(self):
    #     print("Results - 'lorem.txt':")
    #     print(get_file_content("calculator", "lorem.txt"))
    #     print("")

    # def test_get_files_calculator2(self):
    #     print("Results - 'main.py':")
    #     print(get_file_content("calculator", "main.py"))
    #     print("")

    # def test_get_files_calculator3(self):
    #     print("Results - 'pkg/calculator.py':")
    #     print(get_file_content("calculator", "pkg/calculator.py"))
    #     print("")

    # def test_get_files_calculator4(self):
    #     print("Results - '/bin/cat':")
    #     print(get_file_content("calculator", "/bin/cat"))

# class TestWriteFile(unittest.TestCase):
#     def test_get_files_calculator1(self):
#         print("Results - 'lorem.txt':")
#         print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#         print("")

#     def test_get_files_calculator2(self):
#         print("Results - 'pkg/morelorem.txt':")
#         print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#         print("")

#     def test_get_files_calculator3(self):
#         print("Results - '/tmp/temp.txt':")
#         print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
#         print("")

# class TestRunPython(unittest.TestCase):
    # def test_get_files_calculator1(self):
    #     print("Results - 'main.py':")
    #     print(run_python_file("calculator", "main.py"))
    #     print("")

    # def test_get_files_calculator2(self):
    #     print("Results - 'tests.py':")
    #     print(run_python_file("calculator", "tests.py"))
    #     print("")

    # def test_get_files_calculator3(self):
    #     print("Results - '../main.py':")
    #     print(run_python_file("calculator", "../main.py"))
    #     print("")
    
    # def test_get_files_calculator4(self):
    #     print("Results - 'nonexistent.py':")
    #     print(run_python_file("calculator", "nonexistent.py"))
    #     print("")


if __name__ == "__main__":
    unittest.main()