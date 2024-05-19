#from dotenv import dotenv_values, load_dotenv
from Crawler import *
#from multiprocessing import Pool

key_word = ["a", "b"]

crawler = Crawler()

crawler.generator_result_columns(column_name=column_name)

for word in key_word:
    try:
        crawler.get_info_users(word)
    except Exception as error:
        print("Problem Raising: ", error )

try:
    df = pd.DataFrame(crawler.data)
    df.to_csv("./data/Soundcloud_User.csv")
    print("Crawling Success")
except Exception as err:
    print("Problem raise: ", err)









