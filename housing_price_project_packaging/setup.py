import setuptools

with open("README.md", "r" , encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="housing_price_harsh_raghuwanshi",
    version="0.3",
    author="Harsh Raghuwanshi",
    author_email="harsh.raghuwansh@tigeranalytics.com",
    description="Package made for assignment 4.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harsh-tigeranalytics/mle-training",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
