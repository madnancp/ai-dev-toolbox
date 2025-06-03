# Dependency Injection (DI)

- Its a best practice in backend development.
- That is instead of create object for class or call function from api route just use the object and function return value inside.


```python
from fastapi import FastAPI, Depends

app = FastAPI()

def get_token_header():
    return "Authorization : bearer "

@app.get("/home")
def home(token: Depends(get_token_header)):
    return {"token" : token}
```
