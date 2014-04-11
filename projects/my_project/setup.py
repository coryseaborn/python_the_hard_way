try:
    from setuptools import setup
except ImportError:
    from distribute.core import setup
    
config = {
    'description': 'my_project',
    'author': 'Cory',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['my_project'] # be sure to update this!
    'scripts': [],
    'name': 'projectname'
}

setup(**config)