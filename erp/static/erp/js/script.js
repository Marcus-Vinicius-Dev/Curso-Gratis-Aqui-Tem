let carregarImagens = false; // Variável de controle para evitar carregamento duplicado 

function carregarMaisPostagens() {
  if (
    !carregarImagens &&
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 3
  ) {
    carregarImagens = true; // Definir como true para indicar que está carregando

    document.getElementById('indicador-de-carregamento').style.display = 'block';

    setTimeout(function () {
      const novoContainer = document.createElement('div');
      novoContainer.classList.add('postagens-container');

      let novoPost = '';
      for (let i = 0; i < 4; i++) {
        novoPost += `
          <div class="postagem">
              <h2>Título da Postagem ${i}</h2>
              <p>Conteúdo da postagem...</p>
              <img src="{% static 'erp/img/imagem_postagem_${i}.jpg' %}" alt="Imagem da postagem ${i}">
              <a href="#" class="botao">Leia mais</a>
          </div>
        `;
      }

      novoContainer.innerHTML = novoPost;

      document.body.appendChild(novoContainer);

      // Agora, adicione o trecho de código para carregar as imagens
      const quantidadeDeImagens = 30; // Defina a quantidade de imagens a serem carregadas
      for (let i = 1; i <= quantidadeDeImagens; i++) {
        const novaImagem = document.createElement('img');
        novaImagem.classList.add('imagem-post');
        novaImagem.src = `/static/erp/img/artes.jpg`;
        novaImagem.alt = `Imagem ${i}`;
        document.getElementById('container-de-imagens').appendChild(novaImagem);
      }

      document.getElementById('indicador-de-carregamento').style.display = 'none';

      carregarImagens = false; // Correção: atribuir false à variável de controle
    }, 2000);
  }
}

function detectorDeRolagem() { //Nova função
  window.addEventListener('scroll', function () { //window.addEventListener a janela adiciona um ouvinte quando ocorrer um evento 'scroll' (rolagem da janela) acionará a function()
    if (
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 3 /* window.innerHeight é a altura da janela e window.scrollY é a rolagem vertical a soma de ambos resulta no final da página. document.body.offsetHeight calcula a altura da página inteira e - 3 representa menos 3 pixels, caso a rolagem de tela entre no intervalo entre o final da página e -3 pixels, o carregamento de tela terá inicio*/
    ) {
      carregarMaisPostagens(); // Corrigido para chamar a função correta
    }
  });
}