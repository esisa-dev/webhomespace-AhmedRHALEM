import os
import subprocess
import zipfile

class Filesanddirs :

    def __init__(self) -> None:
        self.searchFile = []
        
    def getPath(self,path):
        List = []
        for l in os.listdir(path) :
            if l[0] != '.':
                List.append({
                    'chemin':path+"/"+l,
                    'nom' : l
                })
        return List
    
    def getUserDir(self, path : str) :
        List : list[str] = []
        try: 
            for i in os.listdir(path) : 
                if os.path.isdir(path+"/"+i) :
                    List.append(i)
        except :
            return []
        return List

    def getUserFiles(self, path : str) :
        List : list[str] = []
        try :
            for i in os.listdir(path) : 
                if os.path.isfile(path+"/"+i) :
                    List.append(i)
        except :
            return []
        return List
          
    def NombreDeFichier(self, path : str) -> int :
        cmp : int = 0
        try:
            for l in os.listdir(path) : 
                if os.path.isfile(path+"/"+l) and l[0] != '.':
                    cmp += 1
        except :
            return 0
        return cmp

    def NombreDeDir(self, path : str) -> int : 
        cmp : int = 0
        try :
            for l in os.listdir(path) : 
                if os.path.isdir(path+"/"+l) :
                    cmp += 1
        except:
            return 0
        return cmp
          
    def getSize(self, path : str) -> None :
        cmd = ['du', '-s', path]
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.split()[0]
        except:
            return 0
        
    
    def Extentionfichier(self,path:str,NomFichier : str )  : 
        List = []
        try:
            for i in os.listdir(path) :
                if i[0] != '.':
                    if(i.count(NomFichier)): 
                        List.append({
                            'chemin':path+"/"+i,
                            'nom' : i
                        })
        except:
            return []
        return List
    
    def Download(self,username) -> None :
        home_dir = os.path.expanduser('/home/'+username)
        zip_filename = "/home/"+username+"/"+username+".zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(home_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, home_dir))
          
      
if __name__ == "__main__" :
    f= Filesanddirs()
    f.getPath("/home/a")
   