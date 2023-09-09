let loadingCards = false;

window.addEventListener('scroll', function() {
  if (
    !loadingCards &&
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 3
  ) {
    loadingCards = true;

    document.getElementById('loading-indicator').style.display = 'block';

    setTimeout(function() {
      const newPostagensContainer = document.createElement('div');
      newPostagensContainer.classList.add('postagens-container');

      let newCards = '';
      for (let i = 0; i < 4; i++) {
        newCards += `
          <div class="post-card">
            <div class="post-conteudo">
              <img src="imagens/curso.png" alt="Cursos Grátis Aqui Tem">
              <p>Conteúdo da nova postagem...</p>
            </div>
            <div class="post-acoes">
              <button class="acoes-btn like-btn">Curtir</button>
              <button class="acoes-btn comentario-btn">Comentar</button>
              <button class="acoes-btn compartilhar-btn">Compartilhar</button>
            </div>
          </div>
        `;
      }

      newPostagensContainer.innerHTML = newCards;

      document.body.appendChild(newPostagensContainer);

      document.getElementById('loading-indicator').style.display = 'none';

      loadingCards = false;
    }, 2000);
  }
});
