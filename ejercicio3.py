from hashlib import sha1
import RSA

if __name__ == "__main__":
    M = b"hello world"
    h = sha1()
    h.update(M)
    m = int(h.hexdigest(), 16)
    #print("h = ", h.hexdigest())
    (e, d, n) = RSA.gen_Key_RSA()
    print(e, d, n)
    #sigma 
    x = RSA.cifrar(m, d, n)
    
