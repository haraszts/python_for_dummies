from interpreter import interpret
def main():
    print("Type in this format: num1; operator; num2\nType 'exit' to end")
    while True:
        user_input = input(">> ")
        if user_input.lower() in ("exit", "quit"):
            break
        result = interpret(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()