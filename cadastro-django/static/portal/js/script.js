let carregarPostagens = false; // Variável de controle para evitar carregamento duplicado 

function carregarMaisPostagens() { /* Função que carrega novas postagens */
  if (
    !carregarPostagens && // Verifica se não está carregando cartões atualmente (! verifica se é falsa)
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 3 /* window.innerHeight é a altura da janela e window.scrollY é a rolagem vertical a soma de ambos resulta no final da página. document.body.offsetHeight calcula a altura da página inteira e - 3 representa menos 3 pixels, caso a rolagem de tela entre no intervalo entre o final da página e -3 pixels, o carregamento de tela terá inicio*/
  ) {
    carregarPostagens = true; // Define que está ocorrendo o carregamento 

    document.getElementById('indicador-de-carregamento').style.display = 'block'; // Exibe o indicador de carregamento 

    setTimeout(function () {  /* Temporiza o código abaixo conforme o valor ao final da função definida inicialmente em 2000 milisegundos */
      const novoContainer = document.createElement('div'); /* const novoContainer cria uma nova <div> html napágina que será usada para mostrar novas postagens*/
      novoContainer.classList.add('postagens-container'); //  adicionando a classe 'postagens-container' do index.html à <div> criada 
    
      let novoPost = ''; // string vaziz = '' serve para acumular o HTML das novas postagens 
      for (let i = 0; i < 4; i++) { // for gera um loop que se repetirá de i = '' até i < '' sendo acresentado de um em um i++ 
        novoPost += /* novoPost se refere ao trecho abaixo copiado de index.html em que += acrescenta o conteúdo abaixo conforme a quantidade de loop */
          `
          <div class="post-card">
            <div class="post-conteudo">
              <img src="imagens/curso.png" alt="Cursos Grátis Aqui Tem">
              <p>Conteúdo da nova postagem...</p>
            </div>
            <div class="post-acoes">
              <button class="acoes-btn like-btn"><img src="imagens/curtir.svg" alt="curtir">Curtir</button>
              <button class="acoes-btn comentario-btn"><img src="imagens/comentar.svg" alt="comentar">Comentar</button>
              <button class="acoes-btn compartilhar-btn"><img src="imagens/compartilhar.svg" alt="compartilhar">Compartilhar</button>
            </div>
          </div>
        `;
      }
    
      novoContainer.innerHTML = novoPost; // cria os contâineres para que o novoPost seja acrescentado 
    
      document.body.appendChild(novoContainer); // adiciona novoContainer à página 

      // Atualizado: agora ocultamos o indicador de carregamento depois de adicionar os novos cards
      document.getElementById('indicador-de-carregamento').style.display = 'none'; /* após o carregamento ser concluído, a mensagem de carregamento na tela some (display = 'none') */
    
      carregarPostagens = false; // Define que o carregamento terminou
    }, 2000); // Tempo de carregamento de 2000 milisegundos e finaliza a função timeOut ();
  }
}

function detectorDeRolagem() { //Nova função
  window.addEventListener('scroll', function () { //window.addEventListener a janela adiciona um ouvinte quando ocorrer um evento 'scroll' (rolagem da janela) acionará a function()
    if (
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 3 /* window.innerHeight é a altura da janela e window.scrollY é a rolagem vertical a soma de ambos resulta no final da página. document.body.offsetHeight calcula a altura da página inteira e - 3 representa menos 3 pixels, caso a rolagem de tela entre no intervalo entre o final da página e -3 pixels, o carregamento de tela terá inicio*/
    ) {
      carregarMaisPostagens();
    }
  });
}
//*************** Início da Função Modal de Registro ***************

// Função para exibir o modal
function abrirModal() {
  document.getElementById('registroModal').style.display = 'block';
}

// Função para fechar o modal
function fecharModal() {
  document.getElementById('registroModal').style.display = 'none';
}

// Evento para abrir o modal quando o ícone de conta é clicado
document.querySelector('.menu-icon-dir').addEventListener('click', abrirModal);

// Evento para fechar o modal quando o botão "Fechar" é clicado
document.getElementById('fecharModal').addEventListener('click', fecharModal);

// Evento para fechar o modal quando a área escura fora do modal é clicada
window.addEventListener('click', function (event) {
  if (event.target === document.getElementById('registroModal')) {
    fecharModal();
  }
});

//*************** Fim da Função Modal de Registro ***************

// Inicialize a detecção de rolagem
detectorDeRolagem();
