# Categories

```python
categories_api = client.categories
```

## Class Name

`CategoriesApi`

## Methods

* [Get-Categories](../../doc/controllers/categories.md#get-categories)
* [Get-a-Category](../../doc/controllers/categories.md#get-a-category)


# Get-Categories

Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

```python
def get_categories(self,
                  locale=None,
                  limit=20,
                  offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locale` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `20`<br><br>**Constraints**: `>= 1`, `<= 50` |
| `offset` | `int` | Query, Optional | **Default**: `0` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PagedCategories`](../../doc/models/paged-categories.md).

## Example Usage

```python
locale = 'sv_SE'

limit = 10

offset = 5

result = categories_api.get_categories(
    locale=locale,
    limit=limit,
    offset=offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-a-Category

Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

```python
def get_a_category(self,
                  category_id,
                  locale=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_id` | `str` | Template, Required | - |
| `locale` | `str` | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CategoryObject`](../../doc/models/category-object.md).

## Example Usage

```python
category_id = 'dinner'

locale = 'sv_SE'

result = categories_api.get_a_category(
    category_id,
    locale=locale
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

