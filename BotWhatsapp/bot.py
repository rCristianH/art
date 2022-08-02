import pywhatkit
import time
from datetime import date, datetime


seconds = time.time() + 60
date = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg("+57", "Hola", date.hour, date.minute)

""" time.sleep(5)
 """""" pywhatkit.sendwhats_image("","Image") """