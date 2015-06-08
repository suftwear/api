Vlakbijles API
===================

Requirements:
    - flask
    - flask-restful
    - sqlalchemy

# API Protocol

The following requests require content type json, following format, data only on post/put/delete

```
{
    "api_user": api_user,
    "data" = {
               ..
             },
    "hash": hash,
    "timestamp": timestamp
}
```

Creating users:
|METHOD   |`/user`|RESPONSES|
|---------|-------|---------|
|`GET`    |-|-|
|`POST`   |data:userdata|Success: `201` Failure: `400`|
|`PUT`    |-|-|
|`DELETE` |-|-|

Retrieving/updating user data, removing users:
|METHOD   |`/user/user_id`|RESPONSES|
|---------|---------------|---------|
|`GET`    |data:-|Success: `200` Failure: `404`|
|`POST`   |-|-|
|`PUT`    |data:token,iets|Success: `200` Failure: `400`, `401`, `404`|
|`DELETE` |data:token,password|Success: `200` Failure: `400`, `401`, `404`|

Retrieving/creating user offers:
|METHOD   |`/user/user_id/offer`|RESPONSES|
|---------|---------------------|---------|
|`GET`    |data:-|Success: `200` Failure: `404`|
|`POST`   |data:token,iets|Success: `201` Failure: `400`, `401`|
|`PUT`    |-|-|
|`DELETE` |-|-|

Retrieving list of reviews of user:
|METHOD   |`/user/user_id/review`|RESPONSES|
|---------|----------------------|---------|
|`GET`    |data:-|Success: `200` Failure: `404`|
|`POST`   |-|-|
|`PUT`    |-|-|
|`DELETE` |-|-|

Retrieving/creating/updating/removing user reviews:
|METHOD   |`/review/offer_id`|RESPONSES|
|---------|------------------|---------|
|`GET`    |data:-|Success: `200` Failure: `404`|
|`POST`   |data:token,reviewdata|Success: `201` Failure: `400`, `401`|
|`PUT`    |data:token,reviewdata|Success: `200` Failure: `400`, `401`, `404`|
|`DELETE` |data:token|Success: `200` Failure: `401`, `404`|

Retrieving offers:
|METHOD   |`/offer?loc=X&range=X&subject_id=X&level=X&p=&sortby=X`|RESPONSES|
|---------|-------------------------------------------------------|---------|
|`GET`    |loc:, range:, subject_id:, level:, sortby:|Success: `200` Failure: `204`, `400`|
|`POST`   |-|-|
|`PUT`    |-|-|
|`DELETE` |-|-|

Example:
```
asd
```
