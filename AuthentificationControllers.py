from Data import *
import hashlib

# test commit and push
def sign_in(id, nom, passwd):
    gest = get_gestionnaire(id)
    if gest is not None:
        if nom == gest.nom_complet:
            if hashlib.md5(passwd.encode()).hexdigest() == gest.password:
                if id == "0000":
                    pass  # admin part
                else:
                    pass  # normal gest part
            else:
                pass # wrong passwd
        else:
            pass # wrong name
    else:
        pass # wrong information
