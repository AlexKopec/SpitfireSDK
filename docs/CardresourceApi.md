# swagger_client.CardresourceApi

All URIs are relative to *https://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_card_using_post**](CardresourceApi.md#create_card_using_post) | **POST** /api/cards | createCard
[**delete_card_using_delete**](CardresourceApi.md#delete_card_using_delete) | **DELETE** /api/cards/{id} | deleteCard
[**get_all_cards_using_get**](CardresourceApi.md#get_all_cards_using_get) | **GET** /api/cards | getAllCards
[**get_card_using_get**](CardresourceApi.md#get_card_using_get) | **GET** /api/cards/{id} | getCard
[**update_card_using_put**](CardresourceApi.md#update_card_using_put) | **PUT** /api/cards | updateCard


# **create_card_using_post**
> CardDTO create_card_using_post(card_dto)

createCard

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CardresourceApi()
card_dto = swagger_client.CardDTO() # CardDTO | cardDTO

try: 
    # createCard
    api_response = api_instance.create_card_using_post(card_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardresourceApi->create_card_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_dto** | [**CardDTO**](CardDTO.md)| cardDTO | 

### Return type

[**CardDTO**](CardDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_card_using_delete**
> delete_card_using_delete(id)

deleteCard

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CardresourceApi()
id = 789 # int | id

try: 
    # deleteCard
    api_instance.delete_card_using_delete(id)
except ApiException as e:
    print("Exception when calling CardresourceApi->delete_card_using_delete: %s\n" % e)
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

# **get_all_cards_using_get**
> list[CardDTO] get_all_cards_using_get(email=email)

getAllCards

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CardresourceApi()
email = 'admin@localhost' # str | email (optional) (default to admin@localhost)

try: 
    # getAllCards
    api_response = api_instance.get_all_cards_using_get(email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardresourceApi->get_all_cards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | [optional] [default to admin@localhost]

### Return type

[**list[CardDTO]**](CardDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_using_get**
> CardDTO get_card_using_get(id)

getCard

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CardresourceApi()
id = 789 # int | id

try: 
    # getCard
    api_response = api_instance.get_card_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardresourceApi->get_card_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**CardDTO**](CardDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_card_using_put**
> CardDTO update_card_using_put(card_dto)

updateCard

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CardresourceApi()
card_dto = swagger_client.CardDTO() # CardDTO | cardDTO

try: 
    # updateCard
    api_response = api_instance.update_card_using_put(card_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardresourceApi->update_card_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_dto** | [**CardDTO**](CardDTO.md)| cardDTO | 

### Return type

[**CardDTO**](CardDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

