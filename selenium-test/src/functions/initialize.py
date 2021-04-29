import os

class Inicializar():
    # DIRECTORIO BASE
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d-%m-%Y'
    HourFormat = '%Hh. %Mm. %Ss'

    # JsonData
    Json = basedir + u'\pages'
    JsonResponseData = basedir + u'\data\json'

    Environment = 'Dev'

    NAVEGADOR = u'CHROME'

    DB_DRIVER = "{PostgreSQL ODBC Driver(ANSI)}"
    DB_HOST = "10.200.33.17"
    DB_PORT = "5432"
    DB_DATABASE = "apiux_biblioteca"
    DB_USER = "apiux_biblioteca"
    DB_PASS = 'apiux_biblioteca'

    #BROWSER DE PRUEBAS
    Path_Evidencias = basedir + u'\data\capturas'

    #HOJA DE DATOS EXCEL
    Excel = basedir + u'\data\dataExcel\DataTest.xlsx'

    if Environment == 'Dev':
        URL = f'http://10.200.33.17/auth/signin'
        User = 'admin'
        Pass = 'Alma2021'

    if Environment == 'Test':
        URL = f'http://10.200.33.17/auth/signin'
        User = 'felipe.bravo'
        Pass = '1234'

    # LOGIN AUTOMATICO
    userAdm = "admin"
    passAdm = "Alma2021"

    userFel= "felipe.bravo"
    passFel= "1234"

    userIgn= "ignacio.otarola"
    passIgn= "1234"

    userJuan = "juan.suaza"
    passJuan = "Ju@n1234"

    # CARGAR DOCUMENTOS AUTOMATICOS
       # FORMULARIO
    almaDoc = "ejemplo6"
    modifiedBy = "ignacio"
    ownerName = "nombre1"
    subject = "tema-ejemplo"
    fielType = "PNG"
    author = "TeamQA"
    system = "systema-ejemplo"
    secMode = "Modo seguro"
    releaseBy = "ejemplo Release"
    docId = "documento ID 233df1"
    forumId = "forum ID u28437"
    approvedBy = "aprobado por admin"
    revBy = "felipe"
    group = "grupo 12"
    docAbs = "send keys"