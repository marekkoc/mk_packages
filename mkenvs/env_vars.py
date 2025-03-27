"""
This file contains gets the environment variables from the system.

Author: @marekkoc

Created: 2025-03-15
Modified: 2025-03-15
"""

import os

class EnvVars:
    """
    This class contains the environment variables for the project.
    """
    env_vars = os.environ

    @classmethod
    def get_env_var(cls, var_name):
        return cls.env_vars[var_name]
    
    @classmethod
    def get_python_projects(cls):
        if "PYTHON_PROJECTS" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa PYTHON_PROJECTS nie istnieje")
        return cls.get_env_var("PYTHON_PROJECTS")

    @classmethod
    def get_python_packages(cls):
        if "PYTHON_PACKAGES" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa PYTHON_PACKAGES nie istnieje")
        return cls.get_env_var("PYTHON_PACKAGES")
     
    @classmethod
    def get_python_quotes(cls):
        if "PYTHON_QUOTES" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa PYTHON_QUOTES nie istnieje")
        return cls.get_env_var("PYTHON_QUOTES")


if __name__ == "__main__":
    print()
    projects = EnvVars.get_python_projects() 
    packages = EnvVars.get_python_packages()
    quotes = EnvVars.get_python_quotes()
    print(projects, os.path.exists(projects))
    print(packages, os.path.exists(packages))
    print(quotes, os.path.exists(quotes))
    print()


