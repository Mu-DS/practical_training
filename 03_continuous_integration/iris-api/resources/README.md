# Resources	

Here you can find different resources which are existing as an HTTP API.

# API


## /iris_api

Detect iris class from the list.

Input: json file 

Example:
```bash
    curl -d '{"features":[1,2,3,4]}' \
        -H "Content-Type: application/json" \
        -X POST http://localhost:8000/iris_api
```
