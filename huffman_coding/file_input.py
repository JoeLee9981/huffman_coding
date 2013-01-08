'''
Created on Nov 10, 2012

@author: god_laptop
'''
import fileinput
import decimal

class File_Input(object):
    '''
    classdocs
    '''

    def __init__(selfparams):
        '''
        Constructor
        '''
    def get_str(self):
        f = open('file.txt', 'r')
        str = f.read()
        f.close()
        return str
     
    def read(self):
        f = open('file.txt', 'r')
        str = f.read()
        
        dict = {}
        count = len(str)
        self.count_list(dict, str)
        b = self._convert_list(dict, count)
        
        f.close()
        return b
    
    def _convert_list(self, dict, count):
        list = []
        for x in dict:
            list.append((decimal.Decimal(dict[x] / count), x))
        return list
    
    def count_list(self, dict, content):
        for c in content:
            if c in dict.keys():
                dict[c] += 1
            else:
                dict[c] = 1
            
    def _count_list(self, a, content):
        count = len(content)
        for i in range(len(content)):
            try:
                index = a.index(content[i])
                a[index].increment(count)
            except:
                a.append(Key_Value(content[i], count))
        print(count, "characters in text file")