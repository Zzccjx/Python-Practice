# Global variable
x = 10

def outer():
    # Enclosing variable
    y = 20

    def inner():
        # Local variable
        z = 30

        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)

    inner()

outer()
