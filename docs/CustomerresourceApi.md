# swagger_client.CustomerresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_using_post**](CustomerresourceApi.md#create_customer_using_post) | **POST** /api/customers | createCustomer
[**delete_customer_using_delete**](CustomerresourceApi.md#delete_customer_using_delete) | **DELETE** /api/customers/{id} | deleteCustomer
[**get_all_customers_using_get**](CustomerresourceApi.md#get_all_customers_using_get) | **GET** /api/customers | getAllCustomers
[**get_customer_using_get**](CustomerresourceApi.md#get_customer_using_get) | **GET** /api/customers/{id} | getCustomer
[**update_customer_using_put**](CustomerresourceApi.md#update_customer_using_put) | **PUT** /api/customers | updateCustomer


# **create_customer_using_post**
> Customer create_customer_using_post(customer)

createCustomer

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerresourceApi()
customer = swagger_client.Customer() # Customer | customer

try: 
    # createCustomer
    api_response = api_instance.create_customer_using_post(customer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerresourceApi->create_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| customer | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_using_delete**
> delete_customer_using_delete(id)

deleteCustomer

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerresourceApi()
id = 789 # int | id

try: 
    # deleteCustomer
    api_instance.delete_customer_using_delete(id)
except ApiException as e:
    print("Exception when calling CustomerresourceApi->delete_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_customers_using_get**
> list[Customer] get_all_customers_using_get(email=email)

getAllCustomers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerresourceApi()
email = 'admin@localhost' # str | email (optional) (default to admin@localhost)

try: 
    # getAllCustomers
    api_response = api_instance.get_all_customers_using_get(email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerresourceApi->get_all_customers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | [optional] [default to admin@localhost]

### Return type

[**list[Customer]**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_using_get**
> Customer get_customer_using_get(id)

getCustomer

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerresourceApi()
id = 789 # int | id

try: 
    # getCustomer
    api_response = api_instance.get_customer_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerresourceApi->get_customer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_using_put**
> Customer update_customer_using_put(customer)

updateCustomer

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerresourceApi()
customer = swagger_client.Customer() # Customer | customer

try: 
    # updateCustomer
    api_response = api_instance.update_customer_using_put(customer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerresourceApi->update_customer_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| customer | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

