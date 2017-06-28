import os
import sys
from src.SystemVariable import VAR
import pickle

class diskToMemory():
    def __init__(self, db=None):
        self.db = db

    # Return the total size of self.db dictionary.
    def analysisTotalUsage(self):
        total_size = sys.getsizeof(self.db)
        total_size += sum(map(sys.getsizeof, self.db.values())) + sum(map(sys.getsizeof, self.db.keys()))
        # print(total_size)
        return total_size

    # Return the size of each file in FOLDER_PATH
    # filename: the name of file in DBFile folder.
    def analysisFileUsage(self,filename):
        try:
            full_filename = VAR.FOLDER_PATH+"\\"+filename
            fileobject = open(full_filename, 'rb')
            fileobject.seek(0, 2)  # move the cursor to the end of the file
            size = fileobject.tell()
            # print(size)
            return size
        except Exception as e:
            print(e)

    def do_extract(self):
        try:
            set_num = len(self.db.keys())
            total_size = self.analysisTotalUsage()
            with open(VAR.FOLDER_PATH+"\\file.db", 'wb') as f:
                pickle.dump([set_num, total_size, self.db], f)
            # with open(VAR.FOLDER_PATH+"\\file.db", 'rb') as f:
                # db2 = pickle.load(f)
            # print(db2)
            return True
        except Exception as e:
            print(e)

class memoryToDisk():
    def __init__(self):
        self.db = None

    def do_load(self):
        try:
            with open(VAR.FOLDER_PATH+"\\file.db", 'rb') as f:
                db_descriptor = pickle.load(f)
            if len(db_descriptor) != 3:
                raise ValueError("db_descriptor size is not 3")
            set_num = db_descriptor[0]
            total_size = db_descriptor[1]
            db2 = db_descriptor[2]
            return db2
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    dtm = diskToMemory()
    dtm.analysisFileUsage("f4.txt")
    dtm.analysisTotalUsage()
