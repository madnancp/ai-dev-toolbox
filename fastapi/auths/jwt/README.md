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
