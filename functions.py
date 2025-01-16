import json

def exercicio1_soma():
    """Calcula soma de 1 até 13"""
    indice, soma, k = 13, 0, 0
    while k < indice:
        k += 1
        soma += k
    print(f"Exercício 1 - A soma é: {soma}")

def exercicio2_fibonacci(numero):
    
    """Verifica se um número pertence à sequência de Fibonacci"""
    if numero < 0:
        return f"{numero} não pertence à sequência (negativo)"
    if numero in {0, 1}:
        return f"{numero} pertence à sequência"

    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return f"{numero} {'pertence' if b == numero else 'não pertence'} à sequência"

def exercicio3_faturamento():
    """Analisa dados de faturamento de um arquivo JSON"""
    try:
        with open('dados.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        faturamentos_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]
        menor = min(faturamentos_validos)
        maior = max(faturamentos_validos)
        media = sum(faturamentos_validos) / len(faturamentos_validos)
        dias_acima_media = sum(1 for valor in faturamentos_validos if valor > media)

        print("\nExercício 3 - Análise de Faturamento:")
        print(f"Menor faturamento: R$ {menor:.2f}")
        print(f"Maior faturamento: R$ {maior:.2f}")
        print(f"Dias acima da média: {dias_acima_media}")
    except FileNotFoundError:
        print("Arquivo dados.json não encontrado")

def exercicio4_percentuais():
    """Calcula percentuais de faturamento por estado"""
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total = sum(faturamento.values())
    print("\nExercício 4 - Percentual por estado:")
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

def exercicio5_inverte_strings(palavras):
    """Inverte uma lista de strings"""
    print("\nExercício 5 - Strings invertidas:")
    for p in palavras:
        print(f"Original: {p} -> Invertida: {p[::-1]}")

def main():
    """Função principal que executa todos os exercícios"""
    print("=== Execução dos Exercícios ===\n")

    # Exercício 1
    exercicio1_soma()

    # Exercício 2
    print("\nExercício 2 - Fibonacci:")
    numero_teste = 34
    print(exercicio2_fibonacci(numero_teste))

    # Exercício 3
    exercicio3_faturamento()

    # Exercício 4
    exercicio4_percentuais()

    # Exercício 5
    palavras = ["Hello World", "Python", "JavaScript"]
    exercicio5_inverte_strings(palavras)

if __name__ == "__main__":
    main()
