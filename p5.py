def return_lowest_multiple():
    prime=[]
    prime_count=[]
    lowest_multiple=1
    for i in range(2,21):
        print(i)
        # for j in range(0,len(prime)):
        #     print("he:",i)
        #     if(i==1):
        #         break
        #     elif i%prime[j]==0:
        #         i=i/prime[j]
        #         continue
        #     #elif prime[j]==prime[j-1]:
        #         # continue
        #     elif prime[j]>i:
        #         prime.insert(j,i)
        #         i=1
        j=0
        count=0
        while(j<len(prime)):
            if(i==1):
                if count>prime_count[j]:
                    prime_count[j]==count
                break
            elif i%prime[j]==0:
                i=i/prime[j]
                count+=1
                continue
            else:
                j+=1
        if(i!=1):
            prime.append(i)
            prime_count.append(1)
    for j in range(0,len(prime)):
        lowest_multiple=lowest_multiple*(prime[j]**prime_count[j])
    print(lowest_multiple)
            
if __name__=="__main__":
    return_lowest_multiple()
