import API

def main():
    API_KEY = ''
    with open("hidden.txt", "r") as f:
        lines = f.readlines()
        API_KEY = lines[0].strip()
    











if __name__ == "__main__":
    main()