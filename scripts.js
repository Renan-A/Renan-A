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

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form-agendamento");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Impede o envio tradicional do formulário

        // Redireciona para a página 'revisar.html'
        window.location.href = "revisar.html"; // Página de revisão
    });
});

// Função para capturar parâmetros da URL
function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    return {
        endereco: params.get('endereço'),
        data: params.get('data'),
        horario: params.get('horario'),
        barbeiro: params.get('barbeiro')
    };
}

// Preenche os campos com os valores passados na URL
const params = getUrlParams();
document.getElementById('endereco').innerText = params.endereco;
document.getElementById('data').innerText = params.data;
document.getElementById('horario').innerText = params.horario;
document.getElementById('barbeiro').innerText = params.barbeiro;
