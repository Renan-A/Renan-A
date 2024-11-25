// Manipulação do formulário
const clienteBtn = document.getElementById('cliente-btn');
const barbeiroBtn = document.getElementById('barbeiro-btn');
const form = document.getElementById('cadastro-form');
const camposBarbeiro = document.getElementById('campos-barbeiro');

clienteBtn.addEventListener('click', () => {
    form.style.display = 'block';
    camposBarbeiro.style.display = 'none';
});

barbeiroBtn.addEventListener('click', () => {
    form.style.display = 'block';
    camposBarbeiro.style.display = 'block';
});
