# API versioning

- When building production ready api-services, it must apply the versioning

e.g. instead of `xyz.com/api/user` => `xyz.com/api/v1/user`

- It can help to scale and add new feature on the service without losing/messing up the existing code base
- In order to do that add prefix in api creating. as `api/<version>`

```txt
project/
|---api/
|   |-- v1/
|   |   |- user.py
|   |-- v2/
|   |   |- user.py
```

*We also define route based on version (only if needed)*
