import logging


logging.Formatter(
    fmt='%(asctime)s.%(msecs)03d',
    datefmt='%Y-%m-%d,%H:%M:%S'
)


#Messages above and including this level will be logged.
logging.basicConfig(filename='root.log',encoding='utf-8',filemode='w',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.warning("Remain calm!")
logging.info("just for your info fyi")  
#exc_info=True will print the exception if any
logging.error("This is an error message",exc_info=True)
logging.critical("Critical error...")

### 
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("mylogger.log", mode="w", encoding="utf-8")
logger.addHandler(console_handler)
logger.addHandler(file_handler)
formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",    
    datefmt='%Y-%m-%d %H:%M:%S',
)


console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.warning("Look at my logger!")
