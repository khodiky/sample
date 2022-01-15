## https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string,markers):

    string = string.replace('\n','12')

    lines = string.split('1')

    for a in markers:

        for b in range(len(lines)):

            lines[b] = lines[b].split(a)[0].strip()

            

    return ''.join(lines).strip().replace('2','\n')
