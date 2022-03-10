import threading

from sqlalchemy import Column, String, Integer

from IkarosChatBot.bot.database import BASE, SESSION


class IkarosChatBot(BASE):
    __tablename__ = "IkarosChatBot"
    user_id = Column(Integer, primary_key=True)
    ses_id = Column(String(64))
    expires = Column(String(10))
    
    def __init__(self, user_id, ses_id, expires):
        self.user_id = user_id
        self.ses_id = ses_id
        self.expires = expires
        
IkarosChatBot.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()
USERS = set()


def is_user(user_id):
    try:
        user = SESSION.query(IkarosChatBot).get(int(user_id))
        return bool(user)
    finally:
        SESSION.close()
        
        
def set_ses(user_id, ses_id, expires):
    with INSERTION_LOCK:
        autochat = SESSION.query(IkarosChatBot).get(int(user_id))
        if not autochat:
            autochat = IkarosChatBot(int(user_id), str(ses_id), str(expires))
        else:
            autochat.ses_id = str(ses_id)
            autochat.expires = str(expires)
            
        SESSION.add(autochat)
        SESSION.commit()
        __load_userid_list()
            
            
def get_ses(user_id):
    autochat = SESSION.query(IkarosChatBot).get(int(user_id))
    sesh = ""
    exp = ""
    if autochat:
        sesh = str(autochat.ses_id)
        exp = str(autochat.expires)
        
    SESSION.close()
    return sesh, exp
    
    
def rem_user(user_id):
    with INSERTION_LOCK:
        if autochat := SESSION.query(IkarosChatBot).get(int(user_id)):
            SESSION.delete(autochat)

        SESSION.commit()
        __load_userid_list()
        
        
def __load_userid_list():
    global USERS
    try:
        USERS = {int(x.user_id) for x in SESSION.query(IkarosChatBot).all()}
    finally:
        SESSION.close()
        

__load_userid_list()
