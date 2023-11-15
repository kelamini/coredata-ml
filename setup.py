import setuptools
import coredata_ml

print(coredata_ml.package_name, coredata_ml.__version__)

# Readme
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Module dependencies
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name=coredata_ml.package_name,
    version=coredata_ml.__version__,
    author='Heartex',
    author_email="hello@heartex.com",
    description='Core Data ML backend',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heartexlabs/label-studio-ml-backend',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'coredata-ml=coredata_ml.server:main'
        ],
    }
)
