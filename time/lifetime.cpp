#include <stdio.h>
#include <time.h>

int main() {
    int dia_nascimento, mes_nascimento, ano_nascimento;
    struct tm data_nascimento;
    time_t tempo_atual, tempo_nascimento;
    double segundos_vida;

    // Solicita a data de nascimento
    printf("Digite a data de nascimento (DD MM AAAA): ");
    scanf("%d %d %d", &dia_nascimento, &mes_nascimento, &ano_nascimento);

    // Preenche a struct tm com a data de nascimento fornecida
    data_nascimento.tm_year = ano_nascimento - 1900; // ano - 1900
    data_nascimento.tm_mon = mes_nascimento - 1; // mês (0-11)
    data_nascimento.tm_mday = dia_nascimento; // dia do mês (1-31)
    data_nascimento.tm_hour = 0;
    data_nascimento.tm_min = 0;
    data_nascimento.tm_sec = 0;
    data_nascimento.tm_isdst = -1;

    // Converte a struct tm para time_t
    tempo_nascimento = mktime(&data_nascimento);

    // Obtém o tempo atual
    time(&tempo_atual);

    // Calcula a diferença de tempo em segundos
    segundos_vida = difftime(tempo_atual, tempo_nascimento);

    printf("Você viveu aproximadamente %.0f segundos.\n", segundos_vida);

    return 0;
}
