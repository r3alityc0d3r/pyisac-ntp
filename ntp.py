"""
pyisac-ntp class

Class to manage NTP on servers
"""
from Pyisac.core import Core, Database, Package

class Ntp(object):
    
    def __init__(self,node):
        os_type = "Ubuntu"
        if os_type == "Ubuntu":
            self.package_name = "ntp"
        ntp_package = Package("ntp", node, "install")                                                                                
        if not ntp_package.current():
            print "need to install " + self.package_name
