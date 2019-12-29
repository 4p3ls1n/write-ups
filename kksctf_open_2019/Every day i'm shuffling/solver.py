from random import *

def replace_keys_and_values_in_list(orig_list):
    ans = [-1 for i in range(len(orig_list))]
    for i in range(len(orig_list)):
        ans[orig_list[i]] = i
    return ans

def Shuffle(p, data):
    """
    symmetric function
    """
    buf = list(data)
    for i in range(len(data)):
        buf[i] = data[p[i]]
    return ''.join(buf)

def main():
    file_name = 'fsegovs_meaoerbma_'
    data = open(file_name + '.txt', 'r').read()
    seed(3)
    file_name = list(file_name)
    shuffle(file_name)
    p = list(range(len(data)))
    shuffle(p)
    p = replace_keys_and_values_in_list(p)
    data = Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,Shuffle(p,data)))))))))))))))))))))))))))))))))))))))) 
    out = open('original_text.txt', 'w')
    out.write(''.join(data))
    out.close()

main()