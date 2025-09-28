#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 64
#define MAX_BLOCKS 256    


static int cache[MAX_BLOCKS][MAX_BLOCKS][MAX_N][MAX_N];
static char computed[MAX_BLOCKS][MAX_BLOCKS];

void addMatrix(int n, int A[n][n], int B[n][n], int C[n][n]) {
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            C[i][j] = A[i][j] + B[i][j];
}

void subMatrix(int n, int A[n][n], int B[n][n], int C[n][n]) {
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            C[i][j] = A[i][j] - B[i][j];
}

void strassen_memo(int n, int idA, int idB,
                   int A[n][n], int B[n][n], int C[n][n]) {
                       
                       
    //Verifica se existe na memória de possibilidades

    if (computed[idA][idB]) {
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                C[i][j] = cache[idA][idB][i][j];
        return;
    }

    if (n == 1) {
        C[0][0] = A[0][0] * B[0][0];
    } else {
        int k = n/2;

        int A11[k][k], A12[k][k], A21[k][k], A22[k][k];
        int B11[k][k], B12[k][k], B21[k][k], B22[k][k];

        for (int i=0;i<k;i++)
            for (int j=0;j<k;j++) {
                A11[i][j]=A[i][j];
                A12[i][j]=A[i][j+k];
                A21[i][j]=A[i+k][j];
                A22[i][j]=A[i+k][j+k];

                B11[i][j]=B[i][j];
                B12[i][j]=B[i][j+k];
                B21[i][j]=B[i+k][j];
                B22[i][j]=B[i+k][j+k];
            }

        int M1[k][k], M2[k][k], M3[k][k], M4[k][k], M5[k][k], M6[k][k], M7[k][k];
        int tempA[k][k], tempB[k][k];

        addMatrix(k, A11, A22, tempA);
        addMatrix(k, B11, B22, tempB);
        strassen_memo(k, idA*4+0, idB*4+0, tempA, tempB, M1);

        addMatrix(k, A21, A22, tempA);
        strassen_memo(k, idA*4+1, idB*4+0, tempA, B11, M2);

        subMatrix(k, B12, B22, tempB);
        strassen_memo(k, idA*4+2, idB*4+1, A11, tempB, M3);

        subMatrix(k, B21, B11, tempB);
        strassen_memo(k, idA*4+3, idB*4+0, A22, tempB, M4);

        addMatrix(k, A11, A12, tempA);
        strassen_memo(k, idA*4+0, idB*4+3, tempA, B22, M5);

        subMatrix(k, A21, A11, tempA);
        addMatrix(k, B11, B12, tempB);
        strassen_memo(k, idA*4+1, idB*4+1, tempA, tempB, M6);

        subMatrix(k, A12, A22, tempA);
        addMatrix(k, B21, B22, tempB);
        strassen_memo(k, idA*4+2, idB*4+2, tempA, tempB, M7);

        for (int i=0;i<k;i++)
            for (int j=0;j<k;j++) {
                C[i][j]       = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j]; 
                C[i][j+k]     = M3[i][j] + M5[i][j];                     
                C[i+k][j]     = M2[i][j] + M4[i][j];                     
                C[i+k][j+k]   = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j]; 
            }
    }
    
    
    //Salva na memória de possibilidades

    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            cache[idA][idB][i][j] = C[i][j];
    computed[idA][idB] = 1;
}

int main() {
    int n;
    printf("Digite n (potência de 2): ");
    scanf("%d", &n);

    int A[n][n], B[n][n], C[n][n];
    //Dar espaço antes de inserior o próximo elemento na matriz
    printf("Digite matriz A:\n");
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            scanf("%d", &A[i][j]);

    printf("Digite matriz B:\n");
    for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
            scanf("%d", &B[i][j]);

    memset(computed, 0, sizeof(computed));
    strassen_memo(n, 0, 0, A, B, C);

    printf("Resultado C = A*B:\n");
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    return 0;
}
