#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

//criando estrutura
struct node{
    int temp;
    int umid;
    struct node *next;
};

// definindo ponteiros de cabeça e atuais, usados para manusear a lista, seja adicionar, ler, editar, remover
struct node *headtemp;
struct node *currenttemp = NULL;

struct node *headumid;
struct node *currentumid = NULL;
//---------------------------------

void adicionarUmid(int info)
{
    struct node *newNode = (struct node*)malloc(sizeof(struct node)); // cria novo nó, de tamanho atual da estrutura
    newNode->umid = info;
    newNode->next = NULL;

    if(headumid == NULL) { //checa se a lista está vazia, se estiver os ponteiros indicam para o mesmo canto, a 1a posicao
        headumid = newNode;
        currentumid = newNode;
    }
    else { // caso a lista nao esteja vazia, o ponteiro atual aponta para o ponteiro proximo, encadeando a lista
        currentumid->next = newNode;
        currentumid = newNode;
    }
}

void adicionarTemp(int info)
{
    struct node *newNode = (struct node*)malloc(sizeof(struct node)); // cria novo nó, de tamanho atual da estrutura
    newNode->temp = info;
    newNode->next = NULL;

    if(headtemp == NULL) { //checa se a lista está vazia, se estiver os ponteiros indicam para o mesmo canto, a 1a posicao
        headtemp = newNode;
        currenttemp = newNode;
    }
    else { // caso a lista nao esteja vazia, o ponteiro atual aponta para o ponteiro proximo, encadeando a lista
        currenttemp->next = newNode;
        currenttemp = newNode;
    }
}

float mediaTemp()
{
    float i = 0;
    float soma = 0;
    float media = 0.0;

    struct node *currenttemp = headtemp; //criado um ponteiro que aponta para o começo da lista
    while(currenttemp != NULL) { //enquanto a lista nao chegar no fim (o fim aponta para NULL) será realizado os comandos dentro do while
        i++;
        soma += currenttemp->temp;
        currenttemp = currenttemp->next;
    }
    i = i;
    media = soma / i;
    //a media é tirada

    return media;
}

float mediaUmid()
{
    float i = 0;
    float soma = 0;
    float media = 0.0;

    struct node *currentumid = headumid; //criado um ponteiro que aponta para o começo da lista
    while(currentumid != NULL) { //enquanto a lista nao chegar no fim (o fim aponta para NULL) será realizado os comandos dentro do while
        i++;
        soma += currentumid->umid;
        currentumid = currentumid->next;
    }
    i = i;
    media = soma / i;
    //a media é tirada

    return media;
}

float lerTemp()
{
    FILE *ptr; //Temp //É criado um ponteiro do tipo file que vai armazenar os dados de um arquivo

    ptr = fopen("temperature.txt" , "r"); // o ponteiro armazena os dados do arquivo de texto

    int auxTemp;

    while (!feof(ptr)) { //enquanto nao for o EOF (end of file) do ponteiro (do arquivo) os comandos dentro do while serao executados
        fscanf(ptr,"%d", &auxTemp); //é lida a informacao do ponteiro na vez atual e armazenada em uma variavel auxiliar
        adicionarTemp(auxTemp); //a variavel auxiliar é adicionada na lista
    }

    float media = mediaTemp(); //é dado o retorno da funcao de tirar media para o valor da variavel

    return media; //o valor da variavel que contem a media é retornado
}

float lerUmid()
{
    FILE *ptr2; //Umid //É criado um ponteiro do tipo file que vai armazenar os dados de um arquivo

    ptr2 = fopen("humidity.txt", "r"); // o ponteiro armazena os dados do arquivo de texto

    int auxUmid;

    while (!feof(ptr2)) { //enquanto nao for o EOF (end of file) do ponteiro (do arquivo) os comandos dentro do while serao executados
        fscanf(ptr2,"%d", &auxUmid); //é lida a informacao do ponteiro na vez atual e armazenada em uma variavel auxiliar
        adicionarUmid(auxUmid); //a variavel auxiliar é adicionada na lista
    }

    float media = mediaUmid(); //é dado o retorno da funcao de tirar media para o valor da variavel

    return media; //o valor da variavel que contem a media é retornado
}

int main(void)
{
    float mediaT, mediaU;

    mediaT = lerTemp(); // sao dadas as variaveis o retorno da funcao (média)
    mediaU = lerUmid(); //

    FILE *ptrT, *ptrU;

    ptrT = fopen("med_temp.txt", "a"); //é criado um txt com funcao de escrever nele
    fprintf(ptrT, "%.2f", mediaT); //o valor da variavel é insirida no arquivo de texto
    fclose(ptrT); //o ponteiro é fechado para evitar um possivel lixo de memoria

    ptrU = fopen("med_umid.txt", "a");  //é criado um txt com funcao de escrever nele
    fprintf(ptrU, "%.2f", mediaU); //o valor da variavel é insirida no arquivo de texto
    fclose(ptrU); //o ponteiro é fechado para evitar um possivel lixo de memoria

    return 0;
}


