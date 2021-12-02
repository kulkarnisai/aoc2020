def FNAME1(arr):    
   return 0


def FNAME2(arr):    
   return 0

def preprocess(fname):
    with open(fname) as f:
        arr = f.readlines()

    return arr

if __name__ == "__main__":

    test_arr = preprocess("test_input")
    arr = preprocess("input")
    
    assert FNAME1(test_arr) == 0
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr) == 0
    print("P2:\t" + str(FNAME2(arr)))