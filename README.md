# PDFtoKindle

PDFtoKindle is a simple Python script that allows you to download PDF files from a specified URL and send them to your Kindle device via email for easy reading.

## Usage

1. Run the `open.py` script by executing the following command:
This will open the specified URL, and the PDF file will be downloaded automatically.

2. Ensure you have set up the "Send-to-Kindle" email address on your Kindle device. You can find this address in the "Settings" section of your Kindle device or Kindle app.

3. Run the `emailSender.py` script by executing the following command:
This script will send the downloaded PDF file to your Kindle device's "Send-to-Kindle" email address.

4. Open the Kindle app on your phone or Kindle device to find the sent PDF file and start reading!

## Requirements

- Python 3.x
- An active internet connection to download the PDF file.
- The Kindle app installed on your phone or a Kindle device registered to your Amazon account.

## Notes

- Make sure to configure your "Send-to-Kindle" email address on your Kindle device or app before running `emailSender.py`.
- The `open.py` script currently supports downloading one PDF file from the specified URL. If you want to download multiple PDF files, you can modify the script accordingly.
