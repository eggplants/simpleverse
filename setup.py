from setuptools import find_packages, setup  # type: ignore

"""Update:
(change version,)
sudo rm -rf build dist *.egg-info
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
"""

setup(
    name='simpleverse',
    version='0.3',
    description='API wrapper for versatileapi in Python',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/simpleverse',
    author='eggplants',
    packages=find_packages(),
    python_requires='>=3.0',
    include_package_data=True,
    license='MIT',
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'simv=simpleverse.main:main'
        ]
    }
)
