- Authentication can be done mostly in 2 ways
    1. `Session Based`
    2. `Token Based`
- `Session Based` approached are not using in current applications.
That works when `php` application are trending.
- And, it have very cons. such as 
    - security threats
    - need to store session info on db.
    - and more...
- Current scenario mostly using `Token Based` authentication.

> [!NOTE]
> - `Authentication` : check who the user is, is a valid user. (in login)
> - `Authorization` : check what the user can access. (in resource access)



# JWT (Json Web Tokens)

[Resource](https://hw.glich.co/p/what-is-jwt-token)

- `Token` : Is a encode string that hold user identity.
and it send to server with the request header

> [!NOTE]
> Anyone can decoder `JWT` token.
> It `not encrypted`, it just encode with `BASE64URL`.
> So, never store sensitive info on it.

---

## JWT structure

| Section| its role |
|---------|-------|
| `Header` | Contain metadata|
| `Payload` | contain data to store |
| |On Payload section we only store non-sensitive data such as user_id.|
| `Signature` | generate a new key with encoded header and |
| |encoded payload to verify authenticity of the token.|

- e.g. `header_xxxx.payload_yyyy.signature_zzzz` = `JWT TOKEN`

---

### In Python

- use `python-jose` library for better overall.

```python
from jose import jwt

EXPIRE = timedelta(minutes=3)
ALGORITHM = "HS256"
SECRET_KEY = "kjclsfh3wiehvskjdzbvkllkjszxfoewi
data = {"sub": "john wick will come for you!", "exp": EXPIRE}

jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
```

> - The `ALGORITHM` we mention it only for `signature` section encrypting.
> - `header` & `payload` are encode with `BASE64URL` algorithm.
> - And `header` & `payload` anyone can decode.
> - But, server validation are happend using `signature`.
> - In order to decode `signature` section, we need the `SECRET_KEY`
> - And `signature` section encrypt  with the `ALGORITHM` that we mentioned.


> [!NOTE]
> ### **Workflow i understand after implement a jwt workflow**
> - `signup` create a new user account.
> - `login` check if the user is a valid one or not.
>  If yes it return a `access_token` and `refresh_token` that will store as Cookie
> - `access token` have limited time expire time.
> - `refresh token` have days duration to expire.
> - and when the user make another request to the api, 
> in requst body header have `access_token` added as 
> `Authorization : beared <access_token`
> - If it valid user can access the resource, 
>  if the access token expires, the client generate new 
> `access token` with `refresh token`
> - if the `refresh token` expires the user need to `logn` again.



