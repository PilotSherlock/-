import configparser
import os

class Config:
    def __init__(self):
        if not os.path.exists("config.ini"):
            config = configparser.ConfigParser()
            config['darksouls1']={"path":"","savename":"DRAKS0005.sl2"}
            config['darksouls2']={"path":"","savename":"DS2SOFS0000.sl2"}
            config['darksouls3']={"path":"","savename":"DS30000.sl2"}
            config['eldenring']={"path":"","savename":"ER0000.sl2"}

            config['default']={"game":"darksouls3"}
            with open("config.ini",'w') as configfile:
                config.write(configfile)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

        if not os.path.exists('saves'):
            os.makedirs("saves")
        if not os.path.exists("saves/darksouls1"):
            os.makedirs("saves/darksouls1")
        if not os.path.exists("saves/darksouls2"):
            os.makedirs("saves/darksouls2")
        if not os.path.exists("saves/darksouls3"):
            os.makedirs("saves/darksouls3")
        if not os.path.exists("saves/eldenring"):
            os.makedirs("saves/eldenring")

    def writeReplace(self):
        self.config.write(open("config.ini","w"))
