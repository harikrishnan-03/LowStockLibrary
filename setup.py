from setuptools import setup, find_packages

setup(
    name='InventoryLowStockLibrary', 
    version='0.1.0',  
    author='Harikrishnan Satheeshkumar',  
    author_email='harikrishnanq11@gmail.com',  
    description='A Python library to fetch low stock items from an RDS database.', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='',  
    packages=find_packages(), 
    install_requires=[
        'pymysql',  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent', 
    ],
    python_requires='>=3.6', 
)
