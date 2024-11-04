import sys
from loguru import logger


logger.remove()
logger.add(sink=sys.stdout, format="<white>@Powercodes[*]</white>"
                                   "<white>{time:HH:mm:ss}</white>"
                                   " | <level>{level: <8}</level>"
                                   " | <white><b>{line}</b></white>"
                                   " - <cyan><b>{message}</b></cyan>")
logger = logger.opt(colors=True)
