# python_snake_game

python snake game code.

O código em python refere-se a um snake game. Foram utilizadas as bibliotecas random e tkinter para criar a interface gráfica.

As funções utilizadas no código são as seguintes: 
- Snake: Classe que representa a cobra no jogo. Possui atributos como tamanho do corpo, coordenadas e gráficos das partes da cobra.
- Food: Classe que representa a comida no jogo. Criada em uma posição aleatória.
- next_turn(snake, food): Atualiza a posição da cobra e da comida a cada turno do jogo. Verifica se a cobra colidiu com a comida para aumentar o score e movê-la para uma nova posição. Verifica também colisões com a borda do jogo e o próprio corpo da cobra para encerrar o jogo.
- change_direction(new_direction): Altera a direção da cobra com base na tecla pressionada, evitando mudanças para direções opostas.
- check_collisions(snake): Verifica colisões da cobra com a borda do jogo e com seu próprio corpo.
- game_over(): Encerra o jogo e exibe a mensagem "GAME OVER" na tela, juntamente com um botão para reiniciar o jogo.
- restart_game(): Reinicia o jogo, redefinindo as variáveis e elementos gráficos.
- initial_screen(): Exibe a tela inicial do jogo com o texto "SNAKE GAME" e um botão para iniciar o jogo.
- start_game(): Inicia o jogo, criando a cobra, a comida e chamando a função next_turn().

Essas funções são essenciais para o funcionamento do jogo da cobrinha, controlando o movimento da cobra, detectando colisões e atualizando a interface gráfica.




https://github.com/danyfragas/python_snake_game/assets/114834495/ff808d65-997e-42cd-91a7-3975afd30ff1

