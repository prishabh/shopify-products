# Shopify Product Collection Intersection

This Python script fetches products from multiple Shopify collections and returns only those that exist in **all** specified collections (i.e. the intersection).

It is fully Dockerized and configurable using environment variables or a `.env` file.

---

## 🚀 Features

- Uses Shopify Admin REST API (2024-04)
- Filters products that exist in **all given collections**
- Dockerized for easy, portable execution
- Environment-based config for security
- Simple Makefile for building and running

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/prishabh/shopify-products.git
cd shopify-products
```

### 2. Set environment variables
Create a .env file in the root:

```env
SHOPIFY_SHOP_NAME=your-store-name
SHOPIFY_ACCESS_TOKEN=your-private-access-token
SHOPIFY_COLLECTION_IDS=1234567890,9876543210
```
Replace values with:
```env
Your Shopify store name (e.g. ethics-press)
Your Admin API access token
A comma-separated list of collection IDs
```

---

## 🐳 Using Docker

Build the Docker image
```bash
make build
```
Run the script
```bash
make run
```
Rebuild and run
```bash
make rebuild
```

---

## 🧪 Example Output

```php
Fetching products from collection ID: 269471383605
Fetching products from collection ID: 264997601333

Total products in *all* specified collections: 5
- Ethics of AI (ID: 765432109876)
- Moral Futures (ID: 654321098765)
...
```

---

## 📁 File Structure
```bash
.
├── main.py             # Main Python script
├── Dockerfile          # Docker build file
├── Makefile            # Build/run helper
├── requirements.txt    # Python dependencies
└── .env                # Your environment config (not committed)
```
