from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from typing import List


class MsSqlServerWrapperManager(DatabaseWrapperManager):

    def __init__(self,dbConnection):
        super().__init__(dbConnection)
        #self.conection

    def getRows(self,queryString:str,params=None) -> List:
        print("get rows from ms sql server")
        
    def executeQuery(self,queryString:str,params=None) -> None :
        print("execuete from ms sql server")
        
    
    def closeConection(self) -> None:
        print("close conection from ms sql server")
        