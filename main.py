import re


def main():
    with open('D:\PythonLabs\lab11\con228.bugs.799464655', 'r') as file:
        lines = file.readlines()
        count = 0
        regex = ".edu\/icons"
        for line in lines:
            if re.search(regex, line):
                count = count + 1
                print(f"Query: {line.strip()}")
        print("Number of all queries:", count)



if __name__ == "__main__":
    main()
