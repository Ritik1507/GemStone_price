import os
from pathlib import Path

package_name = "gemstone_price_prediction"

list_of_files = [
   
   
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "src/components/__init__.py",
   "src/exception/__init__.py",
   "src/exception/exception.py",
   "src/logger/__init__.py",
   "src/logger/logging.py",
   "src/pipeline/__init__.py",
   "src/utils/__init__.py",
   "src/__init__.py",
   "templates/index.html",
   "templates/form.html",
   "templates/result.html",
   "app.py",
   "init_setup.sh",
   "requirements.txt",
   "requirements_dev.txt",  
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
   "artifacts",
   "test.py",
  
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
