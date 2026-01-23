# Create Django Project Script

# This script sets up a new Django project with the specified name.

import os
import sys

if len(sys.argv) != 2:
    print("Usage: python create_django_project.py <project_name>")
    sys.exit(1)

project_name = sys.argv[1]

# Create the Django project
os.system(f'django-admin startproject {project_name}')
print(f'Django project {project_name} created successfully!')
