'''
to rebuild or upload to pip,
https://packaging.python.org/tutorials/packaging-projects/
https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56#a435



remove all files in dist/
python setup.py sdist
python -m twine upload dist/*

'''