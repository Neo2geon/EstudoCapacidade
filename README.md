# EstudoCapacidade
AINDA EM DESENVOLVIMENTO
<br><br>Cálculo de CP e CPK a partir de uma base de dados CSV
<br>A partir de um arquivo CSV contendo dados, é realizado um Estudo de Capacidade do Processo (CP e CPK).

## Premissas
1. Os dados devem estar em um arquivo CSV, tendo a seguinte estrutura:
<table border="1">
    <tr>
        <td>Peça nº</td>
        <td>Dimensão 1</td>
        <td>Dimensão 2</td>
        <td>Dimensão n</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1,147</td>
        <td>2,369</td>
        <td>5,589</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1,145</td>
        <td>2,365</td>
        <td>5,587</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1,156</td>
        <td>2,368</td>
        <td>5,569</td>
    </tr>
</table>

2. O arquivo CSV deve estar nomeado como "DadosCSV.csv" e deve estar na mesma pasta do módulo Python;

3. Os dados numéricos podem ter a parte inteira separada da decimal tanto com vírgula (3,14159) quanto com ponto (para
países anglófonos: 3.14159);

4. Tenha a biblioteca PANDAS instalada

5. Crie uma pasta chamada "Os relatórios gerados estao aqui" no mesmo diretório do código para receber os relatórios
 gerados  
 

## Fluxo de funcionamento
1. Substitui as vírgulas do arquivo CSV por pontos (ATENÇÃO: nesse processo os dados são sobrescritos, mas tenho certeza
 de que não preciso lembrar-lhe de manter uma cópia dos dados são e salva em outro lugar, certo?);
2. Importa os dados transformando-o em um dataframe com o PANDAS;
3. Solicita o Limite Superior de Especificação;
4. Solicita o Limite Inferior de Especificação;
5. Para cada coluna do arquivo CSV:
   1. Transforma os dados numa lista python (Por que não usar tudo como dataframe? Não sei, só sei que foi assim...);
   2. Calcula a média dos dados, o desvio padrão, o índice CP e o CPK;
   3. Grava os resultados num arquivo txt na pasta "Os relatórios gerados estao aqui";


## Saídas
Para cada coluna de dados do arquivo CSV (desprezando a primeira coluna que é o número da peça) será gerado um arquivo
TXT contendo os dados utilizados nos cálculos e os resultados dos cálculos efetuados.


## Observações que valem a pena serem lidas
1. O <b>desvio padrão</b> utilizado é o STDEV da biblioteca STATISTICS do python. Dependendo do tipo da sua amostra isso
fará diferença


## Próximos passos
1. incorporar o cálculo de desvio padrão através da média móvel
2. Gráfico de histograma dos dados do estudo