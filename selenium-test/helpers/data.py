import random
import time

class data_login_by_userAdm:
    def __init__(self):
        self.user= "admin"
        self.password = "Alma2021"

class data_login_by_user1:
    def __init__(self):
        self.user= "felipe.bravo"
        self.password = "1234"

class data_login_by_user2:
    def __init__(self):
        self.user= "felipe.niño"
        self.password = "3432"

class data_tag:
    def __init__(self):
        n = random.randint(1, 1000)
        nameRandom=f"Tag0{n}"
        time.sleep(3)
        self.nTag = nameRandom

class data_tag_edit:
    def __init__(self):
        n = random.randint(1, 1000)
        nameRandom=f"Tag0{n}"
        time.sleep(3)
        self.nETag = nameRandom

class data_form_doc:
    def __init__(self):
        self.almaDoc = "ejemplo6"
        self.date = "2021-03-03"
        self.modifiedBy = "ignacio"
        self.ownerName = "nombre1"
        self.subject = "tema-ejemplo"
        self.fielType = "PNG"
        self.author = "TeamQA"
        self.system = "systema-ejemplo"
        self.secMode = "Modo seguro"
        self.releaseBy = "ejemplo Release"
        self.docId = "documento ID 233df1"
        self.forumId = "forum ID u28437"
        self.approvedBy = "aprobado por admin"
        self.revBy = "felipe"
        self.group = "grupo 12"
        self.docAbs = "send keys"

class data_load_doc_equals:
    def __init__(self):
        n = random.randint(1, 10)
        self.imageRepeat = f"C:\\Users\\pipe_\\Desktop\\QA\\DocRepetidos\\Firewall{n}.PNG"

class data_load_doc_new:
    def __init__(self):
        n = random.randint(1, 26)
        self.imageNew = f"C:\\Users\\pipe_\\Desktop\\QA\\qa{n}.PNG"
        self.validImageNew = f"qa{n}"

class data_name_save_search:
    def __init__(self):
        n = random.randint(1, 100)
        self.nameDate= f"Test Date QA{n}"

