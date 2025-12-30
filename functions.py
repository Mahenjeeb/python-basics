def main():
    name = input("Enter Your Name ")
    hello(name)
# Passing default parameter to a function
def hello(to="World"):
    print(f"Hello, {to} 😊")
main()