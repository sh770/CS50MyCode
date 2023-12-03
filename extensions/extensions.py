def main():
    file_name = input("File name: ").lower().strip()
    # print(file_name)

    match = False


    list_file = [".gif" ,".jpg", ".jpeg", ".png", ".pdf", ".txt" , ".zip"]

    for file in list_file:
        if file_name.endswith(file):
            if file == ".gif":
                print("image/gif")
            elif file == ".jpg" or file == ".jpeg":
                print("image/jpeg")
            elif file == ".png":
                print("image/png")
            elif file == ".pdf":
                print("application/pdf")
            elif file == ".txt":
                print("text/plain")
            elif file == ".zip":
                print("application/zip")
            match = True
    if match is False:
        print("application/octet-stream")
main()




