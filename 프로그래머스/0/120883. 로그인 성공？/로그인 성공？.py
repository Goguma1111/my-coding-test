def solution(id_pw, db):
    for data in db : 
        if data == id_pw :
            return 'login'
        elif data[0] == id_pw[0] :
            return 'wrong pw'
    return 'fail'