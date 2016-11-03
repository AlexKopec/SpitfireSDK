# swagger_client.IndustryresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_industry_using_post**](IndustryresourceApi.md#create_industry_using_post) | **POST** /api/industries | createIndustry
[**delete_industry_using_delete**](IndustryresourceApi.md#delete_industry_using_delete) | **DELETE** /api/industries/{id} | deleteIndustry
[**get_all_industries_using_get**](IndustryresourceApi.md#get_all_industries_using_get) | **GET** /api/industries | getAllIndustries
[**get_industry_using_get**](IndustryresourceApi.md#get_industry_using_get) | **GET** /api/industries/{id} | getIndustry
[**update_industry_using_put**](IndustryresourceApi.md#update_industry_using_put) | **PUT** /api/industries | updateIndustry


# **create_industry_using_post**
> IndustryDTO create_industry_using_post(industry_dto)

createIndustry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustryresourceApi()
industry_dto = swagger_client.IndustryDTO() # IndustryDTO | industryDTO

try: 
    # createIndustry
    api_response = api_instance.create_industry_using_post(industry_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryresourceApi->create_industry_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **industry_dto** | [**IndustryDTO**](IndustryDTO.md)| industryDTO | 

### Return type

[**IndustryDTO**](IndustryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_industry_using_delete**
> delete_industry_using_delete(id)

deleteIndustry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustryresourceApi()
id = 789 # int | id

try: 
    # deleteIndustry
    api_instance.delete_industry_using_delete(id)
except ApiException as e:
    print("Exception when calling IndustryresourceApi->delete_industry_using_delete: %s\n" % e)
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

# **get_all_industries_using_get**
> list[IndustryDTO] get_all_industries_using_get()

getAllIndustries

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustryresourceApi()

try: 
    # getAllIndustries
    api_response = api_instance.get_all_industries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryresourceApi->get_all_industries_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IndustryDTO]**](IndustryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industry_using_get**
> IndustryDTO get_industry_using_get(id)

getIndustry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustryresourceApi()
id = 789 # int | id

try: 
    # getIndustry
    api_response = api_instance.get_industry_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryresourceApi->get_industry_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**IndustryDTO**](IndustryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_industry_using_put**
> IndustryDTO update_industry_using_put(industry_dto)

updateIndustry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndustryresourceApi()
industry_dto = swagger_client.IndustryDTO() # IndustryDTO | industryDTO

try: 
    # updateIndustry
    api_response = api_instance.update_industry_using_put(industry_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndustryresourceApi->update_industry_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **industry_dto** | [**IndustryDTO**](IndustryDTO.md)| industryDTO | 

### Return type

[**IndustryDTO**](IndustryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

