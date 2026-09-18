from api.api_client import get_products_data
from processing.data_processor import process_data
from excel.excel_writer import create_report

def main():
    products = get_products_data()

    if products is None:
        return
    
    data = process_data(products)

    create_report(data)

if __name__ == "__main__":
    main()