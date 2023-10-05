#!/usr/bin/python3
import py_compile
import hidden_4

if __name__ == "__main__":
    compiled_module = py_compile.compile("hidden_4.pyc")
    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]

    for name in sorted(module_names):
        print(name)
