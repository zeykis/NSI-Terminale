## Binomial n et m avec récurrence
## Complexité : O(n)
def binomial_rec(n,m):
    if m==0 or m==n:
        return 1
    else:
        return binomial_rec(n-1,m-1)+binomial_rec(n-1,m)

## Binomial_dyn n et m avec programmation dynamique
## Complexité : O(n*m)
def binomial_dyn(n,m):
    T=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,m)+1):
            if j==0 or j==i:
                T[i][j]=1
            else:
                T[i][j]=T[i-1][j-1]+T[i-1][j]
    return T[n][m]

## Fonction binomial(n,m) qui initialise un tableau K
## Cette fonction appelle la fonction récursive binomial_memoise(n,m,K)
## Binomial(n,m) avec une complexité de O(n*m)
def binomial(n,m):
    if m==0 or m==n:
        return 1
    K=[[0]*(m+1) for i in range(n+1)]
    K[0][0]=1
    K[1][0],K[1][1]=1,1
    return binomial_memoise(n,m,K)

## Fonction binomial_memoise(n,m,K) qui calcule le binomial(n,m) si m = 0 ou m = n sortie --> 0
def binomial_memoise(n,m,K):
    if K[n][m]!=0:
        return K[n][m]
    else:
        if m==0 or m==n:
            K[n][m]=1
        else:
            K[n][m]=binomial_memoise(n-1,m-1,K)+binomial_memoise(n-1,m,K)
        return K[n][m]

## Test des fonctions binomiales
def main():
    n=int(input("n = "))
    m=int(input("m = "))
    print("binomial(n,m) = ",binomial(n,m))
    print("binomial_rec(n,m) = ",binomial_rec(n,m))
    print("binomial_dyn(n,m) = ",binomial_dyn(n,m))

if __name__ == '__main__':
    main()
