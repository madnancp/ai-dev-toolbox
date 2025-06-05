# **Websocket**

- It is a communication protocol used in applications were realtime data matters.
- Unlike protocol `http`, `websocket` is `full-duplex` (mean. both client and server can share data any time they want)
- `websocket` only make connection single time. and keep the connection alive untill detroy.
- This mainly used in realtime data needed applications such as `live dashboard`, `chat apps`, `stock price` and so on.
- yes, using normal `http` we can do the similar with `polling` (call the api in specific interval to update data realtime). but that not fully realtime. and it can affect performance.

