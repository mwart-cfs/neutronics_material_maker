
pip3 install bump
pip3 install setuptools
pip3 install twine

bump
python3 setup.py sdist
twine upload dist/* --verbose