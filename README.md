# atmospheric-sensor
A demonstration of reading data from a BME280 atmospheric sensor using python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Clone the repository and install the dependencies:

```bash
git clone git@github.com:bcr666/atmospheric-sensor.git
cd atmospheric-sensor
python3 -m venv {your environment name | def-env}
source {your environment name}/bin/activate
pip install -r requirements.txt

## Usage

The read_bme280.py has a shebang, so it can be executed directly by

./read_bme280.py

The program will read the data from the sensor every 5 seconds.
