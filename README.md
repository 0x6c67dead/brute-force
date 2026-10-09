# Brute Force

Projeto pessoal de estudo com o objetivo de entender, na mão, como funcionam a
comunicação via **sockets TCP**, o **handshake TLS** e a anatomia de uma
**requisição HTTP** — sem usar bibliotecas de alto nível como `requests`. Tudo
é construído com os módulos `socket` e `ssl` do Python.

> [!IMPORTANT]
> Este projeto é **educacional**, para uso em ambientes que você controla ou
> tem autorização explícita para testar (ex.: máquinas virtuais, CTFs,
> aplicações locais). Atacar sistemas de terceiros sem autorização é crime
> (no Brasil, art. 154-A do Código Penal).

## Estado atual

O projeto está em fase inicial de aprendizado. Neste momento ele:

1. Valida os argumentos de linha de comando (alvo, porta, endpoint, usuário,
   wordlist, nomes dos campos do formulário);
2. Resolve o nome do alvo para um IP com `socket.gethostbyname()`;
3. Abre uma conexão TCP e envolve-a com TLS usando
   `ssl.create_default_context()`;
4. Monta e envia **uma única** requisição `POST` com corpo JSON contendo uma
   senha fixa de teste (`teste_senha`);
5. Lê a resposta com `recv()` e procura por indicadores de sessão iniciada
   (`sair`/`logout` na resposta);
6. Percorre a wordlist apenas **imprimindo** as linhas na tela — elas ainda
   não são usadas para montar as requisições.

Ou seja: a wordlist ainda não alimenta o mecanismo de tentativas. Essa etapa
foi proposital, para validar isoladamente cada peça (conexão, requisição,
resposta, leitura de arquivo) antes de juntá-las no loop principal.

## Uso

```bash
python brute.py <target> -p <porta> -d <path> -u <usuário> -w <wordlist>
```

Exemplo:

```bash
python brute.py example.com -p 443 -d /login -u admin -w test.txt
```

### Argumentos

| Argumento         | Obrigatório | Padrão    | Descrição                                          |
| ----------------- | ----------- | --------- | -------------------------------------------------- |
| `target`          | sim         | —         | Host ou IP do alvo                                 |
| `-p, --port`      | sim         | —         | Porta TCP do alvo                                  |
| `-d, --path`      | sim         | —         | Endpoint que recebe as requisições (`/login` etc.) |
| `-u, --user`      | sim         | —         | Usuário usado nas tentativas                       |
| `-w, --word-list` | não*        | —         | Caminho da wordlist de senhas                      |
| `--user-field`    | não         | `username`| Nome do campo de usuário no formulário             |
| `--password-field`| não         | `password`| Nome do campo de senha no formulário               |

\* na prática é obrigatório: sem ele o programa quebra ao tentar abrir o
arquivo.

## Aprendizados até aqui

- Diferença entre abrir um socket TCP e estabelecer uma conexão;
- Como o TLS é "encaixado" por cima do socket com `ssl.SSLContext`;
- Anatomia de uma requisição HTTP manual: request line, headers (`Host`,
  `Content-Type`, `Content-Length`) e corpo;
- Por que o `Content-Length` deve ser calculado sobre os bytes (`.encode()`)
  e não sobre o tamanho da string;
- Leitura de arquivo linha a linha sem carregar tudo em memória.

## Roadmap

- [ ] Usar a wordlist de verdade: mover a montagem do corpo da requisição
      para dentro do loop, trocando a senha a cada iteração;
- [ ] Suportar outros formatos de corpo além de JSON:
  - [ ] `application/x-www-form-urlencoded` (`user=Joseph&password=12345`)
  - [ ] detectar/aceitar outros formatos conforme apareçam
- [ ] Ler a resposta HTTP completa (o `recv(4096)` atual pode truncar
      respostas maiores);
- [ ] Critério de sucesso mais robusto (status code / string configurável
      em vez de procurar `sair`/`logout`);
- [ ] Tratar time-outs e erros de conexão a cada tentativa;
- [ ] Nova conexão por tentativa (ou header `Connection: close`).

## Estrutura

```
brute-force/
├── brute.py    # todo o código (argumentos, socket, requisição, wordlist)
├── test.txt    # wordlist de teste
└── README.md
```
