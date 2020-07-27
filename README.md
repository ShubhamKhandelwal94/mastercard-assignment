# mastercard-assignment

Steps to start backend services:
1) cd ecommerce-backend
2) virtualenv ecommerceenv
3) source ecommerceenv/bin/activate
4) pip3 install requirements.txt
5) python3 manage.py runserver (server should start at http://127.0.0.1:8000/)

open Admin panel (http://127.0.0.1:8000/admin)
1) python manage.py createsuperuser (can skip email address).
2) login through username and password as set in above step.
3) Add Category and Subcategory through Admin panel

#4 - API to get all categories 
   - http://127.0.0.1:8000/categories

#5 - API to get subcategories for a category 
   * Get All subcategories
      - http://127.0.0.1:8000/subcategories
   
   * Get All subcategories by category name
      - http://127.0.0.1:8000/subcategories?category=sports
      
   * Get All subcategories by category id
      - http://127.0.0.1:8000/subcategories?category=7
      
#6 - API to get all products for a category
   * Get All products by category name
      - http://127.0.0.1:8000/getProductsByCategory?category=sports
      
   * Get All products by category id
      - http://127.0.0.1:8000/getProductsByCategory?category=7
      
#7 - API to get all products for a subcategory
   * Get All products by subcategory name
      - http://127.0.0.1:8000/getProductsBySubcategory?subcategory=cricket
    
   * Get All products by subcategory id
      - http://127.0.0.1:8000/getProductsBySubcategory?subcategory=2
      
#8 - API to post new product under existing subcategory and category
      - http://127.0.0.1:8000/products/ 
        body : {
                  "name": "iphone X",
                  "subcategory": 4
               }
 
#9 - 
Steps to start frontend services:
1) cd ecommerce-frontend
2) npm install or npm i
3) npm start 
(http://localhost:4200/home)
