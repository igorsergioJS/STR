#include <iostream>
#include <cstdlib>  // Para qsort, srand, rand
#include <ctime>    // Para clock()

using namespace std;

// Funções necessárias pelo programa
int compare_ints(const void* a, const void* b) {
    int* arg1 = (int*) a;
    int* arg2 = (int*) b;
    if (*arg1 < *arg2) return -1;
    else if (*arg1 == *arg2) return 0;
    else return 1;
}

void bubbleSort(int *vetor, int tamanho) {
    int aux;
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
}

void criarVetor(int *&vetor, int tamanhoVetor, int semente) {
    srand(semente);
    vetor = new int[tamanhoVetor];
    for (int i = 0; i < tamanhoVetor; i++) {
        vetor[i] = rand() % 100000;
    }
}

int main() {
    clock_t tempo_inicio, tempo_fim;
    int *vetor;
    // Testar para vários tamanhos de vetores
    int tamanhos[] = {100, 1000, 10000, 20000, 50000};

    for (int t = 0; t < sizeof(tamanhos)/sizeof(tamanhos[0]); t++) {
        int tamanho = tamanhos[t];
        cout << "Testando vetor de tamanho: " << tamanho << endl;

        // Cria vetor de inteiros
        criarVetor(vetor, tamanho, time(NULL));

        // Mede tempo do Quick Sort
        tempo_inicio = clock();
        qsort(vetor, tamanho, sizeof(int), compare_ints);
        tempo_fim = clock();
        cout << "Tempo de execução do Quick Sort: " << (double)(tempo_fim - tempo_inicio) / CLOCKS_PER_SEC * 1000 << " milissegundos\n";

        // Recria vetor de inteiros
        criarVetor(vetor, tamanho, time(NULL));

        // Mede tempo do Bubble Sort
        tempo_inicio = clock();
        bubbleSort(vetor, tamanho);
        tempo_fim = clock();
        cout << "Tempo de execução do Bubble Sort: " << (double)(tempo_fim - tempo_inicio) / CLOCKS_PER_SEC * 1000 << " milissegundos\n\n";

        delete[] vetor;
    }

    return 0;
}
