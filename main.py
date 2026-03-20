from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello_world(
        q: str,
        sort: bool = False
) -> dict[str, str | bool]:
    return {"q": q, "sort": sort}

@app.get("/{username}")
def username_webpage(username: str):
    return f"This is the webpage of user {username}."


@app.get("/{username}/orders/{order_id}")
def repository_webpage(
        username: str,
        order_id: int,
        sort: bool = False
):
    return f"Order {order_id} for user {username}. Sorted: {sort}."
