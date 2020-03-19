import sys
class main(object):
    def solution(s1, s2):
        if len(s1) > len(s2):
            return False
        d = {}
        for i in range(len(s1)):
            if s1[i] not in d:
                d[s1[i]] =s2[i]
            if d[s1[i]] !=s2[i]:
                return False
        return True
    
    s1=str(str(sys.argv[1])) 
    s2=str(str(sys.argv[2])) 
    print(solution(s1,s2))