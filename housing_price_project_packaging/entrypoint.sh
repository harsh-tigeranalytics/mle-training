#!/usr/bin/env bash

conda run -n test-mle-dev python -m housing_price_harsh_raghuwanshi.ingest_data -ad data/actual_dataset/ -pd data/processed_dataset/ --log-path logs/log.txt
conda run -n test-mle-dev python -m housing_price_harsh_raghuwanshi.train -td data/processed_dataset/housing_train.csv -sm models/ --log-path logs/log.txt
conda run -n test-mle-dev python -m housing_price_harsh_raghuwanshi.score -td data/processed_dataset/housing_test.csv -m models/ --log-path logs/log.txt --rmse --mae
conda run -n test-mle-dev python -m pytest /home/housing_price_harsh_raghuwanshi-0.3/test/unit_tests