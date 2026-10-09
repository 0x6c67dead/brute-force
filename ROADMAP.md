# Roadmap

Progressão planejada do projeto: do estado atual (peças validadas de forma
isolada) até um brute forcer funcional, flexível e organizado.

## Concluído

- [x] Argumentos de linha de comando (alvo, porta, endpoint, usuário,
      wordlist, nomes dos campos do formulário);
- [x] Validação do caminho da wordlist e leitura linha a linha;
- [x] Conexão TCP com o alvo envolvida em TLS (`socket` + `ssl`);
- [x] Montagem e envio manual de uma requisição `POST` com corpo JSON;
- [x] Leitura e inspeção básica da resposta com `recv()`.

## Fase 1 — Loop de tentativas (próximo passo)

- [ ] Mover a montagem do corpo da requisição para dentro do loop, trocando
      a senha a cada iteração (a wordlist deixa de ser só impressa);
- [ ] Usar `json.dumps()` para montar o corpo com segurança (senhas com
      `"` ou `\` quebram o f-string);
- [ ] Uma conexão nova por tentativa, ou header `Connection: close`.

## Fase 2 — Formatos de corpo

- [ ] Argumento `--body-format {json, form}` selecionando o builder do corpo;
- [ ] Suporte a `application/x-www-form-urlencoded` com
      `urllib.parse.urlencode()` (escape de `&`, `=`, `%` nas senhas);
- [ ] Estudar suporte a **Basic Auth** (credenciais no header `Authorization`,
      sem body) para os endpoints que usam esse esquema.

## Fase 3 — Resposta e critério de sucesso

- [ ] Ler a resposta HTTP completa (loop de `recv` até fechar ou respeitar o
      `Content-Length`) — hoje o `recv(4096)` pode truncar;
- [ ] Interpretar o status line (`302` = sucesso típico, `401`/`403` = falha)
      em vez de procurar strings na resposta inteira;
- [ ] Argumento `--success-string` para critérios customizados.

## Fase 4 — Robustez e qualidade

- [ ] `try/except` para `socket.timeout` e erros de conexão em cada tentativa;
- [ ] Correções pontuais: tornar `-w` obrigatório no argparse, corrigir exit
      codes (0 = sucesso, 1 = falha), suportar HTTP puro (TLS apenas quando
      necessário), shebang `#!/usr/bin/env python3`, remover prints de debug;
- [ ] Refatorar em funções (`load_wordlist()`, `build_body()`,
      `send_attempt()`, `main()`);
- [ ] Argumento `--delay` para espaçar as tentativas.

## Ideias futuras (opcional)

- [ ] Detecção automática de TLS pela porta (443 → TLS);
- [ ] Suporte a múltiplos usuários;
- [ ] Progresso e estatísticas (tentativas por segundo, tempo decorrido).
