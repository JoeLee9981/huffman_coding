'''
Created on Nov 10, 2012

@author: Joe Lee
'''
import heapq
#Algorith Referenced from http://en.literateprograms.org/Huffman_coding_%28Python%29

class Huffman(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
    
    def to_huffman(self, a):
        tree = self._build_tree(a)
        complete = []
        self._get_binary(tree, complete)
#        complete = self._to_bin(complete)
        return complete
        
    def _build_tree(self, a):
        heapq.heapify(a)
        while len(a) > 1:
            left = heapq.heappop(a)
            right = heapq.heappop(a)
            heapq.heappush(a, (left[0] + right[0], left, right))
        return a[0]
    
    def _get_binary(self, tree, a, prefix = ''):
        if len(tree) == 2:
            return (tree[1], prefix)
        else:
            left = self._get_binary(tree[1], a, prefix + '1')
            right = self._get_binary(tree[2], a, prefix + '0')
            if left != None:
                a.append(left)
            if right != None:
                a.append(right)
                
    def get_binary(self, tree, prefix = ''):
        if len(tree) == 2:
            print(tree[1], prefix)
        else:
            self.get_binary(tree[1], prefix + '1')
            self.get_binary(tree[2], prefix + '0')

                
    def _to_bin(self, a):
        list = []
        for x in a:
            n = self._str_to_bin(x[1])
            list.append((x[0], n))
        return list
                
    def _str_to_bin(self, str):
        reverse = str[::-1]
        int = 0
        if reverse[0] == "1":
            int += 1
        for i in range(1, len(reverse)):
            if reverse[i] == "1":
                int += 2**i
        return bin(int)