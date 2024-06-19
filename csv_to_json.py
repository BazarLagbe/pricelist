import csv
import json
from datetime import datetime, timezone

# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    # Current timestamp for priceUpdatedAt field
    price_updated_at = datetime.now(timezone.utc).isoformat()

    # Initialize JSON structure
    data = {
        "priceUpdatedAt": price_updated_at,
        "products": []
    }

    # Read CSV file and convert to JSON
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = {
                "name": row['Product Name'].strip(),
                "category": row['Category'].strip(),
                "mrp": float(row['MRP']),
                "discounted_price": float(row['Discounted Price'])
            }
            data['products'].append(product)

    # Write JSON output
    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    csv_to_json('pricelist.csv', 'products.json')
