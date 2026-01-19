def main():
    str = convert(input("Write your string: "))
    print(str)
    

def convert(str):
    result = str.replace(":(","🙁").replace(":)", "🙂")
    return result
    
main()