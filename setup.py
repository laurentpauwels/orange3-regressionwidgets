from setuptools import setup, find_packages

setup(
    name="orange3-regressionwidgets",
    version="0.1.2",
    description="Orange add-on with regression summary and backward elimination widgets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Laurent Pauwels",
    author_email="laurent.pauwels@nyu.edu",
    url="https://github.com/laurentpauwels/orange3-regressionwidgets",
    project_urls={
        "Source": "https://github.com/laurentpauwels/orange3-regressionwidgets",
        "Bug Tracker": "https://github.com/laurentpauwels/orange3-regressionwidgets/issues",
    },
    packages=find_packages(),
    package_data={
        "orangecontrib.regressionsummary.widgets": ["icons/*.svg", "widgets.json"]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "Orange3>=3.30.0",
        "statsmodels>=0.13.0",
        "pandas>=1.3.0"
    ],
    entry_points={
        "orange.widgets": (
            "Regression = orangecontrib.regressionsummary",
        ),
    },
    zip_safe=False,
)