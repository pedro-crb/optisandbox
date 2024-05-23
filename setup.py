from setuptools import setup, find_packages
from pathlib import Path

README_path = Path(__file__).parent / "README.md"
with open(README_path, encoding='utf-8') as f:
    long_description = f.read()

init_path = Path(__file__).parent / "optisandbox" / "__init__.py"

with open(init_path) as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name='OptiSandbox',
    version=version,
    description="Optisandbox is a standalone version of the numpy and optimization "
                "modules from Peter Sharpe's Aerosandbox",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.11',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.20.0, <2.0a0',
        'scipy >= 1.7.0',
        'casadi >= 3.6.4',
        'pandas >= 2',
        'matplotlib >= 3.7.0',
        'seaborn >= 0.11',
        'sortedcontainers >= 2',
    ],
)
