from setuptools import setup, find_packages

setup(
    name='patcherex',
    version='1.2',
    description='The patcherex',
    packages=find_packages(),
    scripts=["patcherex/patcherex"],
    install_requires=[
        'angr',
        'capstone',
        'keystone-engine',
        'psutil',
        'timeout-decorator',
        'subprocess32',
        'povsim @ git+https://github.com/mechaphish/povsim.git',
        'compilerex @ git+https://github.com/mechaphish/compilerex.git',
        'shellphish-qemu',
        'fidget @ git+https://github.com/angr/fidget.git',
        'python-resources',
        'pyyaml',
        'pyelftools',
        'python-magic',
        'termcolor',
        'tracer @ git+https://github.com/angr/tracer.git',
   ],
)
