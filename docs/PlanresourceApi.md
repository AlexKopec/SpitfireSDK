# swagger_client.PlanresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_using_post**](PlanresourceApi.md#create_plan_using_post) | **POST** /api/plans | createPlan
[**delete_plan_using_delete**](PlanresourceApi.md#delete_plan_using_delete) | **DELETE** /api/plans/{id} | deletePlan
[**get_all_plans_using_get**](PlanresourceApi.md#get_all_plans_using_get) | **GET** /api/plans | getAllPlans
[**get_plan_using_get**](PlanresourceApi.md#get_plan_using_get) | **GET** /api/plans/{id} | getPlan
[**update_plan_using_put**](PlanresourceApi.md#update_plan_using_put) | **PUT** /api/plans | updatePlan


# **create_plan_using_post**
> Plan create_plan_using_post(plan)

createPlan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanresourceApi()
plan = swagger_client.Plan() # Plan | plan

try: 
    # createPlan
    api_response = api_instance.create_plan_using_post(plan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanresourceApi->create_plan_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | [**Plan**](Plan.md)| plan | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plan_using_delete**
> delete_plan_using_delete(id)

deletePlan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanresourceApi()
id = 789 # int | id

try: 
    # deletePlan
    api_instance.delete_plan_using_delete(id)
except ApiException as e:
    print("Exception when calling PlanresourceApi->delete_plan_using_delete: %s\n" % e)
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

# **get_all_plans_using_get**
> list[Plan] get_all_plans_using_get()

getAllPlans

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanresourceApi()

try: 
    # getAllPlans
    api_response = api_instance.get_all_plans_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanresourceApi->get_all_plans_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Plan]**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_using_get**
> Plan get_plan_using_get(id)

getPlan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanresourceApi()
id = 789 # int | id

try: 
    # getPlan
    api_response = api_instance.get_plan_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanresourceApi->get_plan_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plan_using_put**
> Plan update_plan_using_put(plan)

updatePlan

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlanresourceApi()
plan = swagger_client.Plan() # Plan | plan

try: 
    # updatePlan
    api_response = api_instance.update_plan_using_put(plan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanresourceApi->update_plan_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | [**Plan**](Plan.md)| plan | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

