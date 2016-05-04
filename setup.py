from setuptools import setup, find_packages
import opmd_viewer  # In order to extract the version number

# Get the long description
# If possible, use pypandoc to convert the README from Markdown
# to reStructuredText, as this is the only supported format on PyPI
try:
    import pypandoc
    long_description = pypandoc.convert( './README.md', 'rst')
except (ImportError, RunTimeError):
    long_description = open('./README.md').read()
# Get the package requirements from the requirements.txt file
with open('./requirements.txt') as f:
    install_requires = [line.strip('\n') for line in f.readlines()]
# Since wget cannot be installed with conda, it is added separately here
install_requires.append('wget')

# Main setup command
setup(name='openPMD-viewer',
      version=opmd_viewer.__version__,
      description='Visualization tools for openPMD files',
      long_description=long_description,
      maintainer='Remi Lehe',
      maintainer_email='remi.lehe@lbl.gov',
      license='BSD 3-Clause License',
      url='https://github.com/openPMD/openPMD-viewer.git',
      packages=find_packages('./'),
      package_data={'opmd_viewer': ['notebook_starter/*.ipynb']},
      scripts=['opmd_viewer/notebook_starter/openPMD_notebook'],
      install_requires=install_requires,
      tests_require=['pytest', 'jupyter'],
      setup_requires=['pytest-runner'],
      classifiers=[
          'Programming Language :: Python',
          'Development Status :: 4 - Beta',
          'Natural Language :: English',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Scientific/Engineering :: Visualization',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'],
      )
