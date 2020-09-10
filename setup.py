import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neutronics_material_maker",
    version="0.1.3",
    summary="Package for making material cards for OpenMC",
    author="neutronics_material_maker development team",
    author_email="jonathan.shimwell@ukaea.uk",
    description="A tool for making neutronics material cards for use in OpenMC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ukaea/neutronics_material_maker",
    packages=setuptools.find_packages(),
    zip_safe=True,
    package_dir={"neutronics_material_maker": "neutronics_material_maker"},
    package_data={
        "neutronics_material_maker": [
            "requirements.txt",
            "README.md",
            "LICENSE",
            "data/*.json",
        ]
    },
    tests_require=["pytest-cov", "pytest-runner"],
    install_requires=[
        "CoolProp",
        # 'openmc' when pip install is available
    ],
)
