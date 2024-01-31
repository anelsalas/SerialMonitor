
### Usage:
- Usage: python3 serial_data_logger.py COM_PORT [slope] [intercept]
- Default calibration: `python3 serial_data_logger.py COM_PORT`
- Custom calibration: `python3 serial_data_logger.py COM_PORT 1.2961 0.1312`

This version of the script uses the corrected calibration formula in the `apply_calibration` function. You can specify the slope and intercept as optional command line arguments, or the script will use the default values if they are not provided.
