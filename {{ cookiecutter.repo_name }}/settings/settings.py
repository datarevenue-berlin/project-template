import os
import pandas as pd

DEBUG = True

DATA_DIR = os.path.abspath("../data")
LOG_DIR = os.path.join(DATA_DIR, "log/")

# ---------------------- DEFAULT COLS --------------------

ID_COL = "id"
DATE_COL = "date"
TARGET_COL = "target"

# ====== FEATURES =======

DEFAULT_TRAIN_DATES = pd.date_range("2016-10-01", "2016-10-31").date
DEFAULT_N_TEST_DAYS = 6

# Slicing
DATA_DELAY = {{ cookiecutter.data_delay }}
DEFAULT_N_AGG_DAYS = {{ cookiecutter.aggregation_window }}
N_LEAD_WINDOW_DAYS = {{ cookiecutter.lead_window }}

DEFAULT_TRAIN_SAMPLE = 10
DEFAULT_TEST_SAMPLE = 1

TIME_BINS = [
    (0, DEFAULT_N_AGG_DAYS)
]