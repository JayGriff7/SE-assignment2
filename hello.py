try:
    name = input("Please enter your name: ").strip()
    if not name:
        name = "Jalen"  # sensible default if user just hits Enter
    print(f"Hello, {name}!")
    print(f"Hi! {name}")
except EOFError:
    # If stdin isn't available (e.g., some IDEs), fall back:
    name = "Jalen"
    print(f"Hello, {name}!")
    print(f"Hi! {name}")
