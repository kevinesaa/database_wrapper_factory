
import pymssql # replace this line with your specific database engine, example: import pyodbc 

import json

from databaseConectionManager.core.DatabaseWrapperManager import DatabaseWrapperManager
from databaseConectionManager.factory.SimpleFactory import DatabaseSimpleFactory
from databaseConectionManager.core.SupportedDatabasesEnum import DatabaseType



def _getSecretManagerString(awsRegion:str, secretManagerArn:str) -> str :
    
    # here make your logic to get the secret str with boto3
    # a trip could be add the dbType value to the secret manager
    secret : str ='''
        {
            "db_type": "MS_SQL_SERVER",
            "db_host":"localhost",
            "db_name":"example",
            "db_user":"admin",
            "db_pass":"12345678"
        }
        '''
    secret = " ".join([ line.strip() for line in secret.splitlines()])
    secret = secret.strip()
    return secret



def _cretateDbConection(secretManagerJsonObject:dict[str,object]) -> object:
    
    # here add the logic to create a specific database connection
    # https://learn.microsoft.com/es-es/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql?view=sql-server-ver16
    
    return pymssql.connect(
        server = secretManagerJsonObject["db_host"],
        user = secretManagerJsonObject["db_user"],
        password = secretManagerJsonObject["db_pass"],
        database = secretManagerJsonObject["db_name"],
        as_dict=True
    )  
    


def createDatabseManager(dbType: DatabaseType, awsRegion:str, secretManagerArn:str) -> DatabaseWrapperManager :
    
    # a trip could be add the dbType value to the secret manager
    databaseSecretString = _getSecretManagerString(awsRegion, secretManagerArn)
    databaseSecretJson = json.loads(databaseSecretString)
    dbConection = _cretateDbConection(databaseSecretJson)
    
    # with the trip the return looks something like
    # dbTypeName = databaseSecretJson['db_type']
    # dbType = DatabaseType[dbTypeName]
    # return DatabaseSimpleFactory.createDatabaseManager(dbType,dbConection)
    
    return DatabaseSimpleFactory.createDatabaseManager(dbType,dbConection)
