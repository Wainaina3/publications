import yaml
import os

class Appconfig(object):

    #return config data given a name
    #if its running in a container, the config_data arg will have to be shared as the secret key/value and config name will be secret name
    def read_configs(config_name,config_data="data"):
       
        current_dir = os.getcwd()
        config_file = "govtconf.yaml"
        #return local configfiles dir
        app_secrets_dir = "".join([current_dir,"/mainapp/configs/confs/"])
        with open(os.path.join(app_secrets_dir, config_file)) as configs_file:
            loaded_config = yaml.safe_load(configs_file)
            config = loaded_config[config_name]
        return config
