let carregarPostagens = false; // Variável de controle para evitar carregamento duplicado 

function carregarMaisPostagens() {
  if (
    !carregarPostagens &&
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 3
  ) {
    carregarPostagens = true;
    var indicador = document.getElementById('indicador-de-carregamento'); // Seleciona o elemento indicador-de-carregamento

    if (indicador) { // Verifica se o indicador existe
      indicador.style.display = 'block'; // Exibe o indicador de carregamento
    }

    setTimeout(function () {
      const novoContainer = document.createElement('div');
      novoContainer.classList.add('postagens-container');
      let novoPost = '';
      for (let i = 0; i < 4; i++) {
        novoPost +=
          `
          <div class="post-card">
          <div class="post-conteudo">
              <img src="/static/erp/img/curso.png" alt="imagem do curso">
              <p>Conteúdo da postagem...</p>
          </div>
          <div class="post-acoes">
              <button class="acoes-btn like-btn"><img src="/static/erp/img/curtir.svg" alt="ícone de curtir">Curtir</button>
              <button class="acoes-btn comentario-btn"><img src="/static/erp/img/comentar.svg" alt="ícone de comentar">Comentar</button>
              <button class="acoes-btn compartilhar-btn"><img src="/static/erp/img/compartilhar.svg" alt="ícone de compartilhar">Compartilhar</button>
          </div>
      </div>
        `;
      }
    
      novoContainer.innerHTML = novoPost;
      document.body.appendChild(novoContainer);
      if (indicador) { // Verifica se o indicador existe
        indicador.style.display = 'none'; // Oculta o indicador de carregamento
      }
      carregarPostagens = false;
    }, 2000);
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

// Inicialize a detecção de rolagem
detectorDeRolagem();
