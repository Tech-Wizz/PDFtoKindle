import webbrowser

def openUrl(url):
    # Use the webbrowser module to open the URL in the default web browser (Chrome if set as default).
    webbrowser.open(url)
    print("Opened URL (" + url + ")"

# loop:
for issue_number in range(1, 131):
    firstHalf = "https://magpi.raspberrypi.com/issues/"
    secondHalf = "/pdf/download"
    urlToOpen = firstHalf + str(issue_number) + secondHalf
    openUrl(urlToOpen)
    #print(urlToOpen)
