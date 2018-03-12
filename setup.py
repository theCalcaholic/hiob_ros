from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=[
        'hiob',
        'hiob.core',
        'hiob.core.app',
        'hiob.core.argparser',
        'hiob.core.ev',
        'hiob.core.extraction',
        'hiob.core.pursuing',
        'hiob.core.roi',
        'hiob.core.sample_provider',
        'hiob.core.selection',
        'hiob.config',
        'hiob.config.collections',
        'hiob.config.data_sets',
        'hiob.net'],
    package_dir={'': './'}
)

setup(**d)
