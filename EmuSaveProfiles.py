import os
import sys

class EmuSaves:
    def getSavePaths(self, path):
        o = []
        if os.path.isfile(path):
            for i in file.readlines(file(path)):
                if i[0] != '#' and i != '\n' and i != None and i[0] != ' ':
                    x = i.split('\n')[0]
                    if os.path.exists(x):
                        o.append(x)
                        continue
                    sys.exit('%s is not a valid directory.' %(x))
            return o
        sys.exit("ERROR! The file (%s) does not exist!!" %(path))

    def __main__(self):
        for folder in self.folders:
            activeuser = None
            hasUser = False
            for file in os.listdir(folder):
                if file.endswith('.emusaves'):
                    hasUser = True
                    activeuser = file.split('.emusaves')[0]
                    print "Current user in %s: %s" %(folder, activeuser)

            userpath = '%s.%s'%(folder, self.user)
            userpathexists = False
            if os.path.exists(userpath):
                userpathexists = True

            if not hasUser:
                if userpathexists:
                    sys.exit("ERROR! %s does not contain a .emusaves file, but %s already exists." %(folder, userpath)) 
                print 'No .emusaves file found in %s. Creating %s.emusaves' %(folder, self.user)
                open('%s\%s.emusaves' %(folder, self.user), 'w+')
                continue
            
            if self.user == activeuser:
                print '%s is already active in: %s' %(self.user, folder)
                continue
            
            print "Changing %s to %s.%s" %(folder, folder, activeuser)
            os.rename(folder,'%s.%s'%(folder,activeuser))

            if userpathexists:
                print "Changing %s to %s" %(userpath, folder)
                os.rename(userpath, folder)
                continue
            
            print "New user detected. Creating new folder %s with file %s.emusaves" %(folder, self.user)
            os.mkdir('%s'%(folder))
            open('%s\%s.emusaves' %(folder, self.user), 'w+')

    def __init__(self, user='default'):
        self.user = user
        self.folders =self.getSavePaths('savepaths.cfg')
        self.__main__()


USER = 'default'
if len(sys.argv) > 1:
    USER = sys.argv[1]
    print 'USER %s WAS SPECIFIED' %(USER)
EmuSaves(user=USER)