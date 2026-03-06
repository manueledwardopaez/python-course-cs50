import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'^<iframe[^>]*src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"[^>]*></iframe>$'
    
    match = re.fullmatch(pattern, s)
    
    if match:
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    
    return None


if __name__ == "__main__":
    main()