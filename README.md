
# Python System Performance Monitor

A lightweight, Python-based application that monitors CPU, RAM,
and disk usage on Windows computers.

Developed using Python and the psutil library, this project
collects system performance statistics, evaluates resource
utilization, and records timestamped measurements for analysis.

## Features

- Monitor CPU, RAM, and disk usage
- Classify resource usage as Normal, Moderate, or High
- Choose between a single check and multiple readings
- Collect up to 10 readings per monitoring session
- Automatically stop after completing the selected readings
- Calculate average CPU and RAM utilization
- Save timestamped measurements to a local text file
- Validate user input to prevent invalid monitoring requests

## Technologies Used

- Python
- psutil
- time (Python standard library)

## Installation

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Install the required library:

   ```bash
   python -m pip install psutil
   ```

## Usage

Run the application:

```bash
python system_monitor.py
```

The program offers two options:

**Option 1: Single Performance Check**
- Collects one set of CPU, RAM, and disk statistics.
- Displays performance classifications and averages.

**Option 2: Multiple Performance Readings**
- Allows the user to select between 1 and 10 readings.
- Collects measurements approximately every five seconds.
- Calculates average CPU and RAM utilization.
- Automatically terminates after the requested readings.

## Performance Classification

| Resource Usage | Status |
|----------------|--------|
| Below 50% | Normal |
| 50% to below 80% | Moderate |
| 80% or higher | High Usage |

These thresholds are illustrative and are not hardware safety limits.

## Performance Logging

Each measurement is automatically recorded in
`performance_log.txt` with a timestamp.

Example:

```text
2026-11-05 11:15:00 | CPU: 24.5% | RAM: 62.1% | Disk: 43.6%
2026-11-05 11:15:05 | CPU: 35.2% | RAM: 63.4% | Disk: 43.6%
```

The log file is excluded from GitHub using `.gitignore`.

## Example Output

```text
SYSTEM PERFORMANCE MONITOR
--------------------------
1. Check System Performance Once
2. Monitor System Performance
Select an option: 2
How many readings (1-10)? 2

Reading 1 of 2

SYSTEM PERFORMANCE MONITOR
--------------------------
CPU Usage: 24.5 %
RAM Usage: 62.1 %
Disk Usage: 43.6 %
--------------------------
CPU Status: Normal
RAM Status: Moderate
Disk Status: Normal

Reading 2 of 2

SYSTEM PERFORMANCE MONITOR
--------------------------
CPU Usage: 35.2 %
RAM Usage: 63.4 %
Disk Usage: 43.6 %
--------------------------
CPU Status: Normal
RAM Status: Moderate
Disk Status: Normal

--------------------------
PERFORMANCE SUMMARY
--------------------------
Average CPU Usage: 29.85 %
Average RAM Usage: 62.75 %

Performance data saved successfully!
```

## Limitations

- Currently designed for Windows systems using the C: drive
- Uses a command-line interface
- Monitors disk space usage rather than disk read/write activity
- Monitoring sessions are limited to 10 readings

## Future Improvements

- Graphical user interface
- Performance graphs and visualization
- Cross-platform compatibility
- Additional hardware statistics

## Author

Kyle Chan
