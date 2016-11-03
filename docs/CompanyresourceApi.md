# swagger_client.CompanyresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company_using_post**](CompanyresourceApi.md#create_company_using_post) | **POST** /api/companies | createCompany
[**delete_company_using_delete**](CompanyresourceApi.md#delete_company_using_delete) | **DELETE** /api/companies/{id} | deleteCompany
[**get_all_companies_using_get**](CompanyresourceApi.md#get_all_companies_using_get) | **GET** /api/companies | getAllCompanies
[**get_company_using_get**](CompanyresourceApi.md#get_company_using_get) | **GET** /api/companies/{id} | getCompany
[**search_companies_using_get**](CompanyresourceApi.md#search_companies_using_get) | **GET** /api/_search/companies | searchCompanies
[**update_company_using_put**](CompanyresourceApi.md#update_company_using_put) | **PUT** /api/companies | updateCompany


# **create_company_using_post**
> CompanyDTO create_company_using_post(company_dto)

createCompany

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()
company_dto = swagger_client.CompanyDTO() # CompanyDTO | companyDTO

try: 
    # createCompany
    api_response = api_instance.create_company_using_post(company_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->create_company_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_dto** | [**CompanyDTO**](CompanyDTO.md)| companyDTO | 

### Return type

[**CompanyDTO**](CompanyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_using_delete**
> delete_company_using_delete(id)

deleteCompany

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()
id = 789 # int | id

try: 
    # deleteCompany
    api_instance.delete_company_using_delete(id)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->delete_company_using_delete: %s\n" % e)
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

# **get_all_companies_using_get**
> list[CompanyDTO] get_all_companies_using_get()

getAllCompanies

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()

try: 
    # getAllCompanies
    api_response = api_instance.get_all_companies_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->get_all_companies_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompanyDTO]**](CompanyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_using_get**
> CompanyDTO get_company_using_get(id)

getCompany

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()
id = 789 # int | id

try: 
    # getCompany
    api_response = api_instance.get_company_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->get_company_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**CompanyDTO**](CompanyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_companies_using_get**
> list[CompanyDTO] search_companies_using_get(query)

searchCompanies

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()
query = 'query_example' # str | query

try: 
    # searchCompanies
    api_response = api_instance.search_companies_using_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->search_companies_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query | 

### Return type

[**list[CompanyDTO]**](CompanyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_using_put**
> CompanyDTO update_company_using_put(company_dto)

updateCompany

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyresourceApi()
company_dto = swagger_client.CompanyDTO() # CompanyDTO | companyDTO

try: 
    # updateCompany
    api_response = api_instance.update_company_using_put(company_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyresourceApi->update_company_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_dto** | [**CompanyDTO**](CompanyDTO.md)| companyDTO | 

### Return type

[**CompanyDTO**](CompanyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

