
J = "z"
S = "ZZ"

class Solution(object):
    def numJewelsInStones(self, J, S):
            """
            :type J: str
            :type S: str
            :rtype: int
             """
            J = list(J)
            S = list(S)
            cont = 0
            for i in range(len(J)):
                for j in range(len(S)):

                    if J[i] == S[j] :
                        cont = cont +1
                        #print(cont)
            return cont 



 