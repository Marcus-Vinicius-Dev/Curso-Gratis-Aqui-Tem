let carregarImagens = false;

function carregarMaisPostagens() {
  console.log('Chamando carregarMaisPostagens');
  if (
    !carregarImagens &&
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 3
  ) {
    console.log('Condição de carregamento atendida');
    carregarImagens = true;

    document.getElementById('indicador-de-carregamento').style.display = 'block';

    setTimeout(function () {
      console.log('Timeout executado');
      const novoContainer = document.createElement('div');
      novoContainer.classList.add('postagens-container');

      let novoPost = '';
      const quantidadeDeImagens = 30; // Defina a quantidade de imagens a serem carregadas
      for (let i = 1; i <= quantidadeDeImagens; i++) {
        if (i % 2 === 0) { // Carregar apenas imagens com números pares
          console.log(`Criando imagem ${i}`);
          const novaImagem = document.createElement('img');
          novaImagem.classList.add('imagem-post');
          novaImagem.src = `/static/erp/img/imagem_postagem_${i}.jpg`;
          novaImagem.alt = `Imagem ${i}`;
          novoContainer.appendChild(novaImagem);
        }
      }

      document.body.appendChild(novoContainer);

      document.getElementById('indicador-de-carregamento').style.display = 'none';

      carregarImagens = false;
    }, 2000);
  }
}

function detectorDeRolagem() {
  window.addEventListener('scroll', function () {
    if (
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 3
    ) {
      console.log('Rolagem detectada');
      carregarMaisPostagens();
    }
  });
}
