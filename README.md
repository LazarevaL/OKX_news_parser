## Make a Python script that downloads news from the OKX crypto exchange OKX.
The successful solution should:
1. Accept three parameters: START_DATE, END_DATE, FOLDER;
2. Download data from the website from START_DATE to END_DATE;
3. Dump the data to the FOLDER, using the structure of the file of your choice

### How to install 
```
pip install git+https://github.com/LazarevaL/OKX_news_parser
```
### Example 
```
news_downloader = OKXNewsDownloader("2023-04-21", "2023-05-04", "news_folder")
news_downloader.download_news() 
```
