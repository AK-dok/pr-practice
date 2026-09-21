def greet(name):
    """Return a friendly greeting for the given name."""
    if not name:
        name = "there"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
