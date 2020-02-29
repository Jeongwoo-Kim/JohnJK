class ConfigFileSingleton(object):
    __instance = None
    
    @classmethod
    def __get_instance(cls):
        return cls.__instance
    
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__get_instance
        return cls.__instance
    
    def get_instance(self, input_properties_path):
        result = self.instance()
        if input_properties_path and len(input_properties_path) > 0:
            self.change_propertie(input_properties_path)
        return result
    
    properties_path = 'sendbird-takehome.conf'

    myprops = {}
    
    def change_propertie(self, input_properties_path):
        if input_properties_path:
            self.properties_path = input_properties_path
            self.load_properties()
            
    def load_properties(self):
        try:
            with open(self.properties_path, 'r') as f:
                for line in f:
                    line = line.rstrip() 
                    if "=" not in line: continue 
                    if line.startswith("#"): continue 
            
                    k, v = line.split("=", 1)
                    self.myprops[k] = v
        except IOError as e:
            print(e)
            print('no properties file.')
    
    def get_property(self, input_key):
        if input_key and len(input_key) > 0:
            if self.myprops is not None and len(self.myprops.items()) > 0:
                return self.myprops.get(input_key)
            else:
                self.load_properties()
                return self.myprops.get(input_key)
        else:
            return None
        
class ConfigFile(ConfigFileSingleton):
    pass

if __name__ == '__main__':
    a = ConfigFile.instance()
    print(a)
    print(a.get_property('test.1'))