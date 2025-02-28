
-----------------------------------------------------------------------------------------------------------------------
# Pattern_create

Este script gera uma string cíclica única, útil para encontrar offsets em vulnerabilidades de buffer overflow. A string pode ser usada para identificar onde um registrador (como EIP ou RIP) foi sobrescrito, auxiliando na criação de exploits precisos.

Funcionalidades:
- Geração de padrões cíclicos com tamanho personalizado
- Útil para identificação de deslocamento em ataques de buffer overflow

-----------------------------------------------------------------------------------------------------------------------

# Pattern_off

Este script ajuda a encontrar o deslocamento exato (offset) de um valor dentro de uma string cíclica gerada por um Pattern Create. Ele é essencial para determinar onde ocorre a sobreposição de registradores (como EIP ou RIP) em explorações de buffer overflow, permitindo um controle preciso da execução do código.

Funcionalidades:
- Encontra a posição exata de um valor dentro de uma string padrão
- Auxilia na criação de exploits ajustando o controle do fluxo de execução