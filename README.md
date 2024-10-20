# Homework Instructions for Peer Review

## User Inspection

You can inspect the list of your users by navigating to the following URL:

- [User List](http://127.0.0.1:8000/auth/users/)

## Obtain Authentication Token

To interact with the API, you will need to obtain an authentication token for your preferred user. You can use either Djoser's or Django Rest Framework's token authentication path:

- **Djoser Token Login**:  
  [Login Token Endpoint](http://127.0.0.1:8000/auth/token/login/)

- **DRF Token Endpoint**:  
  [Obtain Token](http://127.0.0.1:8000/obtain-auth-token/)

Send a `POST` request to the token endpoint with the following payload:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```
## Test API
With a valid token in your request's authentication parameters, test the following endpoints:

- **Booking endpoint**:
  [Book a table](http://127.0.0.1:8000/restaurant/booking/tables/)

- **Menu endpoint**:
  [Menu](http://127.0.0.1:8000/menu/)

POST and GET are available for both APIs. Payload examples:

```json
{
  "first_name": "John",
  "reservation_date": "2024-10-20",
  "reservation_slot": "13"
}
``` 

```json
{
  "title": "Greek Salad",
  "price": "11",
  "inventory": "100",
  "menu_item_description": "Summer special"
}
``` 

