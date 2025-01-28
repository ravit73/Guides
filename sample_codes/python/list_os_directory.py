import os
from datetime import datetime
import polars as pl

 
def sizeFormat(size):
    newform = format(size/1024, ".2f")
    return newform + " KB"

def createFileRecords(somepath):
    #dictionary
    recordList = []
    

    for name in os.listdir(somepath): 
        
        filepath = os.path.join(somepath, name)
        #main library that holds stats
        stats = os.stat(filepath)
        attrs = {
            'file_name': name,
            'size_kb': str(round(stats.st_size/1024,2)),
            'created': str(datetime.fromtimestamp(stats.st_ctime)), # st_ctime from Python 3.12 will be replaced with st_birthtime 
            'modified': str(datetime.fromtimestamp(stats.st_mtime)),
            'last_accessed': str(datetime.fromtimestamp(stats.st_atime)),
           # 'user_id': str(stats.st_uid)
        }
        df = pl.from_dict(attrs)
        recordList.append(df)
    return recordList 
 
    


if __name__ == "__main__":
    path = 'C:/Users/radek.vitek/my_dev/ravit73/Guides/sample_codes/python'   
    print(pl.concat(createFileRecords(path)))
             