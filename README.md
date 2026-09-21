# API Sales Report Automation

## Description

This project retrieves product data from an API, processes the data using pandas, and generates a formatted Excel report using openpyxl.

## Features

- Retrieve product data from an API
- Process data using pandas
- Generate an Excel report
- Apply professional Excel formatting
- Format price values
- Automatically adjust column widths
- Freeze the header row
- Add AutoFilter to the report
- Log important program events
- Handle errors during API requests and file operations

## Technologies Used

- Python 3.12
- Requests
- Pandas
- OpenPyXL
- Git & GitHub

## Project Structure

```text
api-sales-report-automation/
│
├── api/
│   └── api_client.py
│
├── config/
│   └── config.py
│
├── excel/
│   └── excel_writer.py
│
├── processing/
│   └── data_processor.py
│
├── utils/
│   └── logger.py
│
├── main.py
├── requirements.txt
└── README.md
```

## How It Works

1. The application sends a request to the API to retrieve product data.
2. The API response is converted into a pandas DataFrame.
3. The data is processed and prepared for the report.
4. The processed data is exported to an Excel file.
5. OpenPyXL is used to apply formatting to the Excel report.
6. Logging records important events and errors during execution.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jefferson-rocha1412/api-sales-report-automation.git
```

2. Navigate to the project folder:

```bash
cd api-sales-report-automation
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```