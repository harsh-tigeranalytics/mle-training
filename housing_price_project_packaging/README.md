# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Installation:
### Prerequisites:
Prerequisite dependencies are stored in `enviornment_file/env.yml`. To setup the conda environment:

`$ conda env create --file enviornment_file/env.yml`

`$ conda activate test-mle-dev`

### Setup:
For editable install:
`$ pip install -e .`

For normal install:
`$ pip install .`

## Run code:
### To download and process data:
`$ python src/housing_price_harsh_raghuwanshi/ingest_data.py -ad data/actual_dataset/ -pd data/processed_dataset/`
### To train the models:
`$ python src/housing_price_harsh_raghuwanshi/train.py -td data/processed_dataset/housing_train.csv -sm models/`
### To score trained models:
`$ python src/housing_price_harsh_raghuwanshi/score.py -td data/processed_dataset/housing_test.csv -m models/ --rmse --mae`
### Note:
You can get information on command line arguments for each of the above scripts using `-h` or `--help`. For example:

`$ python src/housing_price_harsh_raghuwanshi/train.py --help`
## Steps performed:
 - We prepared and cleaned the data.
 - We checked and imputed missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.
