import os
import spwd
import crypt 

class SignIn :
    def __init__(self,Username : str,password : str) :
        self.Username = Username
        self.password = password

    def CheckUsername(self) -> bool :
        if self.Username in os.listdir("/home") :
            return True
        else :
           
            return False
    def CheckPassword(self,Username:str,password:str) -> bool :
        user=spwd.getspnam(Username)
        if(crypt.crypt(password, user.sp_pwdp)) == user.sp_pwdp:
            return True
        return False
           
        return False
    def authentificationtest(self)->bool :
        if (self.CheckUsername == True and self.CheckPassword ==True ) :
            return True
        else :
            print("Erreur d'authentification")
            return False

if __name__ == "__main__" :
     a = SignIn("user1","0000")
     print(a.CheckUsername())
     print(a.CheckPassword("user1","0000"))
     print(a.authentificationtest())