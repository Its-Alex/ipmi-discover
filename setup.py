import setuptools

setuptools.setup(
    name="ipmi_finder",
    version="0.1.0",
    author="Alexandre MARRE",
    author_email="me@itsalex.fr",
    license='AGPL',
    python_requires='>=3',
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ipmi_finder=ipmi_finder:cli'
        ]
    }
)
