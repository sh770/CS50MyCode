import sys
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    match = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if match:
        link = "https://youtu.be/" + match.group(1)
        return link
    else:
        return None
        # sys.exit("None")
    
    # match = re.search('(?<=embed/).*?(?=")' ,s)
    # if match:
    #     url = "https://youtu.be/" + match.group(0)
    #     # print(url)
    #     return url
    # else:
    #     return None
    # try:
    #     # // Use re to extract
    #     url: re.Match[str] = re.search('(?<=embed\/).*?(?=")', s)
    #     # // Return the extracted embed
    #     return f"https://youtu.be/{url.group(0)}"
    # except Exception:
    #     return None




if __name__ == "__main__":
    main()