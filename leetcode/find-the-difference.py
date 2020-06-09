class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        t2 = t
        t = list(t)

        s = list(s)
        for i in range(len(t)) :

    
            guardo = t[i] 
    
            del(t[i])

           

            if s == t :

                pass
                #print(guardo)       

            else:
                t = list(t2) 
    
        return guardo 


#class Solution(object):
#    def findTheDifference(self, s, t):
#        """
#        :type s: str
#        :type t: str
#        :rtype: str
#        """
#        sc = collections.Counter(s)
#        tc = collections.Counter(t)
#        for ch in tc:
#            if sc[ch] != tc[ch]:
#                return ch