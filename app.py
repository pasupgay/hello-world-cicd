def generate_greeting():
    return "Hello, World!"

if __name__ == "__main__":
    print(generate_greeting())

def test_greeting():
    assert generate_greeting() == "Hello, World!"
    print("Test passed successfully!")
