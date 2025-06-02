# JWT (Json Web Tokens)

[Resource](https://hw.glich.co/p/what-is-jwt-token)

- `Token` : Is a encode string that hold user identity.
and it send to server with the request header

> [!NOTE]
> Anyone can decoder `JWT` token.
> It `not encrypted`, it just encode with `BASE64`.
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

> - The `ALGORITHM` we mention it only for `signature` section encoding.
> - `header` & `payload` are strictly encode with `BASE64URL` algorithm.
> - And `header` & `payload` anyone can decode.
> - But, server validation are happend using `signature`.
> - In order to decode `signature` section, we need the `SECRET_KEY`
> - And `signature` section encode with the `ALGORITHM` that we mentioned.
