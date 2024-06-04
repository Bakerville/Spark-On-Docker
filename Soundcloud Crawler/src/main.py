#from dotenv import dotenv_values, load_dotenv
from Crawler import *
from multiprocessing import Pool
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  SUCCESS %(message)s",

    handlers=[
        logging.FileHandler("./log/crawler.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
# Creating an object
logger = logging.getLogger(__name__)

key_word = ["a","b","c","d", "e"]

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
    logger.info("Crawling Sucessfully")
except Exception as err:
    print("Problem raise: ", err)











