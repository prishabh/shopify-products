import os
import json
import requests

# Read from environment variables
SHOP_NAME = os.getenv("SHOPIFY_SHOP_NAME")
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
COLLECTION_IDS = os.getenv("SHOPIFY_COLLECTION_IDS")

if not SHOP_NAME or not ACCESS_TOKEN or not COLLECTION_IDS:
    raise Exception("Please set SHOPIFY_SHOP_NAME, SHOPIFY_ACCESS_TOKEN, and SHOPIFY_COLLECTION_IDS environment variables.")

# Parse collection IDs (expected as comma-separated string)
collection_ids = [int(cid.strip()) for cid in COLLECTION_IDS.split(",")]

HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": ACCESS_TOKEN
}

BASE_URL = f"https://{SHOP_NAME}.myshopify.com/admin/api/2024-04"

def get_products_in_collection(collection_id):
    products = []
    page_info = None
    limit = 250

    while True:
        params = {
            "collection_id": collection_id,
            "limit": limit
        }
        if page_info:
            params["page_info"] = page_info

        url = f"{BASE_URL}/products.json"
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json()

        if "products" not in data or not data["products"]:
            break

        products.extend(data["products"])

        link_header = response.headers.get("Link")
        if link_header and 'rel="next"' in link_header:
            import re
            match = re.search(r'page_info=([^&>]+)', link_header)
            page_info = match.group(1) if match else None
        else:
            break

    return products

def get_products_for_collection_ids(collection_ids):
    collection_products = []

    for collection_id in collection_ids:
        print(f"Fetching products from collection ID: {collection_id}")
        products = get_products_in_collection(collection_id)
        product_map = {product["id"]: product for product in products}
        collection_products.append(product_map)

    if not collection_products:
        return []

    common_ids = set(collection_products[0].keys())
    for product_dict in collection_products[1:]:
        common_ids &= set(product_dict.keys())

    final_products = [collection_products[0][pid] for pid in common_ids]
    return final_products

if __name__ == "__main__":
    products = get_products_for_collection_ids(collection_ids)

    print(f"\nTotal products in *all* specified collections: {len(products)}")
    for p in products:
        print(f"- {p['title']} (ID: {p['id']})")
