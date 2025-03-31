from setuptools import setup, find_packages

setup(
    name='Methylation Tools',  # Replace with your package name
    version='1.0.0',  # Initial version of your package
    author='Sweet Lake Analytics',  # Your name or your organization's name
    author_email='chris@sl-analytics.com',  # Your email address
    description='A set of tools to analyze methylation patterns.',  # Short description
    long_description=open('README.md').read(),  # Long description read from README file
    long_description_content_type='text/markdown',  # Specify the format of the long description
    url='https://github.com/Sweet-Lake-Analytics/MethylationTools',  # URL to your project's repository
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify the Python version
        'License :: OSI Approved :: MIT License',  # License type (replace with your license)
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        'required_package1',  # List your project's dependencies
        'required_package2',
    ],
    extras_require={
        'dev': ['check-manifest'],  # Optional dependencies for development
        'test': ['pytest'],  # Optional dependencies for testing
    },
    entry_points={
        'console_scripts': [
            'your_command=your_package.module:function',  # Command line interface (if applicable)
        ],
    },
)
