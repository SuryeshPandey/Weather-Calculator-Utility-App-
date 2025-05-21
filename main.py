# main.py

def main():
    print("Welcome to the Python Utility App 🌤️➗")
    print("Choose Mode: ")
    print("1. Weather Info")
    print("2. Calculator")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        from weather_gui import launch_weather_gui
        launch_weather_gui()
    elif choice == '2':
        from calculator import calculator_cli
        calculator_cli()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
