# atmospheric-sensor
A demonstration of reading data from a BME280 atmospheric sensor from a Raspberry Pi using python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Pinout](#pinout)

## Installation

Clone the repository and install the dependencies:

```bash
git clone git@github.com:bcr666/atmospheric-sensor.git
cd atmospheric-sensor
python3 -m venv {your environment name | def-env}
source {your environment name}/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
The read_bme280.py has a shebang, so it can be executed directly by

./read_bme280.py

The program will read the data from the sensor every 5 seconds.
```

## Pinout
This resource was helpful in determining where I should connect my BME280 leads. https://pinout.xyz/
For my wiring, I am using the I2C protocol, which only requires 4 wires.
  Red - Pin 1
  Blue - Pin 3
  Yellow - Pin 5
  Black - Pin 6
