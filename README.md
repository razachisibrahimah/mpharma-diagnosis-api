
## About mPharma Diagnosis REST API
mPharma Diagnosis REST API allows utilization of an internationally recognized set of diagnosis codes

## Programming language
Python 3.9.1

## Framework
Django REST framework

## Database 
PostgreSQL Server13


## Packages Used
1. Psycopg2-binary: PostgreSQL database adapter for the Python\

## Deployment
In order to deploy the application, it is required to have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

1. Verify the `.env` file in the root directory to ensure the specified host machine ports are free to bind. If not, simply modify the ports
2. Run the command `docker-compose up -d`. 4 containers will be built:
  - The Django application container with gunicorn as the http-server
  - nginx container as the reverse proxy
  - A postgres container
  - An Adminer container...A GUI application to manage the database.

  After the containers start up, the application should be accessible at `http://localhost:<APP_HOST_PORT>`.

  **Note:** On first startup, it may take a while for the application to become available as the database server needs to run it's initialization.

## API 
 BasePath: http://localhost:8000/api/
 Consumes: application/json
 Produces: application/json

## Categories

### Create
  Method: POST
  Endpoint: categories/
  Params:
  ```
  {
    "code":"A011",
    "title":"Paratyphoid fever ",
    "description":"Paratyphoid fever "
  }
  ```

Expected Results:
```
  {
    "id": 4,
    "code": "A011",
    "title": "Paratyphoid fever",
    "created_at": "2021-02-07T10:03:23.355778Z",
    "updated_at": "2021-02-07T10:03:23.355778Z"
}
```

### Read
  Method : GET
  Endpoint: categories

  Expected Results:
  ```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "code": "A01",
            "title": "Typhoid fever",
            "created_at": "2021-02-06T16:39:32.601547Z",
            "updated_at": "2021-02-06T16:39:32.601547Z"
        },
        {
            "id": 1,
            "code": "111111",
            "title": "Chole",
            "created_at": "2021-02-06T15:10:46.681837Z",
            "updated_at": "2021-02-06T15:10:46.680839Z"
        },
        {
            "id": 4,
            "code": "A011",
            "title": "Paratyphoid fever",
            "created_at": "2021-02-07T10:03:23.355778Z",
            "updated_at": "2021-02-07T10:03:23.355778Z"
        }
    ]
}
```

  ### Update
  Method: PUT
  Endpoint: categories/
  Params  : 
  ```
  {
    "code":"A04",
    "title":"Other bacterial intestinal infections"
  }
  ```

  Expected Results:
  ```
  {
    "id": 1,
    "code": "A04",
    "title": "Other bacterial intestinal infections",
    "created_at": "2021-02-06T15:10:46.681837Z",
    "updated_at": "2021-02-06T15:10:46.680839Z"
  }
  ```

  ### Delete
  Endpoint: categories/{id}/
  Expected Results: 1


## Dxcode

### Create
  Method: POST
  Endpoint: dxcodes/
   Params  :
   ```
   {
    "category":1,
    "diagnosis_code":"0",
    "full_code":"A0101",
    "abbreviated_descrition":"Typhoid fever, unspecified",
    "full_description":"Typhoid fever, unspecified",
     "category_title":"Typhoid fever"
  }
  ```

Expected Results:
```
  {
    "id": 2,
    "diagnosis_code": "0",
    "full_code": "A0101",
    "abbreviated_descrition": "Typhoid fever, unspecified",
    "full_description": "Typhoid fever, unspecified",
    "category_title": "Typhoid fever",
    "created_at": "2021-02-07T10:49:57.054193Z",
    "updated_at": "2021-02-07T10:49:57.053120Z",
    "category": 1
  }
  ```

### Read
  Method : GET
  Endpoint: categories

  Expected Results:
  ```
  {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "diagnosis_code": "0",
            "full_code": "A0101",
            "abbreviated_descrition": "Typhoid fever, unspecified",
            "full_description": "Typhoid fever, unspecified",
            "category_title": "Typhoid fever",
            "created_at": "2021-02-07T10:49:57.054193Z",
            "updated_at": "2021-02-07T10:49:57.053120Z",
            "category": 1
        },
        {
            "id": 1,
            "diagnosis_code": "2",
            "full_code": "A3493",
            "abbreviated_descrition": "Typhoid fever, unspecified",
            "full_description": "Typhoid fever, unspecified",
            "category_title": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "created_at": "2021-02-06T17:00:16.475298Z",
            "updated_at": "2021-02-06T17:00:16.475298Z",
            "category": 1
        }
    ]
}
```

  ### Update
  Method: PUT
  Endpoint: dxcodes/
  Params  : 
  ```
  {
    "category":1,
    "diagnosis_code":"2",
    "full_code":"A3493",
    "abbreviated_descrition":"Typhoid fever, unspecified",
    "full_description":"Typhoid fever, unspecified"
  }
  ```

  Expected Results:
  ```
  {
    "id": 1,
    "diagnosis_code": "2",
    "full_code": "A3493",
    "abbreviated_descrition": "Typhoid fever, unspecified",
    "full_description": "Typhoid fever, unspecified",
    "category_title": "Cholera due to Vibrio cholerae 01, biovar cholerae",
    "created_at": "2021-02-06T17:00:16.475298Z",
    "updated_at": "2021-02-06T17:00:16.475298Z",
    "category": 1
  }
  ```

  ### Delete
  Endpoint: dxcodes/{id}/
  Expected Results: 1


## Update 
1.  
2.




## new features to be added 
1. create user to access the resource
2. Add JWT to authenticate user to access resource 

