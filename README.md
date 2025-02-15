# warehouse-svc

This service is for simple demoing purposes only. It is also still "under construction". With that being said, this service contains 3 models - Category, Product, and Inventory. The exposted endpoints currently support the following features:

1. Query for all categories (i.e. "electronics", "clothing", etc.).

2. Query for all products. Result is paginated, returning 10 records at a time. Furthermore, category_id query param can be used to return subset of products that belong to the requested category.

3. Query to retrieve a specific product by product id. 

## How to run

1. Clone this repo and cd in to dir.

2. Create conda env and activate.

3. Install project dependencies.
    ```bash
    pip install -r requirements.txt
    ```

4. Install PostgreSQL on your machine if not already installed.

5. Create a new database and define a user that has read/write access to it.

6. Define the following system env vars:
    ```
    WAREHOUSE_DB_NAME=your_db_name
    WAREHOUSE_DB_USER=your_db_user
    WAREHOUSE_DB_PASS=your_db_password
    ```

7. Run migrations.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Load initial data into db.
    ```bash
    python manage.py loaddata shop/fixtures/init_data.json
    ```

9. Run dev server.
    ```bash
    python manage.py runserver
    ```

Try heading over to `http://127.0.0.1:8000/shop/products/`. You should see products!