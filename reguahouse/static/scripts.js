document.addEventListener("DOMContentLoaded", function() {
    const clienteBtn = document.getElementById("cliente-btn");
    const barbeiroBtn = document.getElementById("barbeiro-btn");
    const formulario = document.getElementById("cadastro-form");
    const camposBarbeiro = document.getElementById("campos-barbeiro");
    const camposComuns = document.getElementById("campos-comuns");
    const mensagemCadastro = document.createElement('div'); // Criar o elemento da mensagem
    const opcoes = document.querySelector('.opcoes'); // Seleciona a div com os botões de cadastro
    const voltarHomeBtn = document.querySelector('.menu .btn'); // Seleciona o botão "Voltar para Home"
    const loginBtnContainer = document.getElementById("login-btn-container"); // Seleciona o contêiner do botão de login
    const loginBtn = document.getElementById("login-btn"); // Seleciona o botão de login
    const fraseCadastro = document.querySelector("main p"); // Seleciona a frase "Escolha uma das opções para continuar:"

    // Estilo para a mensagem de sucesso
    mensagemCadastro.style.padding = "10px";
    mensagemCadastro.style.marginTop = "20px";
    mensagemCadastro.style.backgroundColor = "#4CAF50";
    mensagemCadastro.style.color = "white";
    mensagemCadastro.style.textAlign = "center";
    mensagemCadastro.style.display = "none"; // Começa oculto

    // Adicionar a mensagem de sucesso ao corpo
    document.body.appendChild(mensagemCadastro);

    // Ao clicar em "Sou Cliente"
    clienteBtn.addEventListener("click", function() {
        formulario.style.display = "block";
        camposBarbeiro.style.display = "none";
        camposComuns.style.display = "block";
    });

    // Ao clicar em "Sou Barbeiro"
    barbeiroBtn.addEventListener("click", function() {
        formulario.style.display = "block";
        camposBarbeiro.style.display = "block";
        camposComuns.style.display = "block";
    });

    // Ao submeter o formulário
    formulario.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevenir o envio do formulário (evita recarregar a página)
        
        // Substituir a frase pela mensagem de sucesso
        fraseCadastro.textContent = "Cadastro realizado com sucesso!";
        fraseCadastro.style.color = "#4CAF50"; // Mudando a cor da frase para verde

        // Ocultar os botões de cadastro
        opcoes.style.display = "none";

        // Mostrar o botão "Login"
        loginBtnContainer.style.display = "block"; // Torna o botão de login visível

        // Mostrar o botão "Voltar para Home"
        voltarHomeBtn.style.display = "inline-block"; // Garante que o botão de voltar esteja visível

        // Limpar o formulário após o cadastro (opcional)
        formulario.reset();
        
        // Ocultar o formulário novamente, se desejar
        formulario.style.display = "none";
    });

    // Ao clicar no botão de Login
    loginBtn.addEventListener("click", function() {
        window.location.href = "login.html"; // Redireciona para a página de login
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

document.addEventListener('DOMContentLoaded', function () {
    // Seleciona os elementos
    const clienteBtn = document.getElementById('clienteBtn');
    const form = document.getElementById('form-agendamento');
    const camposBarbeiro = document.getElementById('camposBarbeiro');

     // Verifica se o botão e os campos existem antes de adicionar o evento
     if (clienteBtn && form && camposBarbeiro) {
        clienteBtn.addEventListener('click', () => {
            // Exibe o formulário e esconde os campos dos barbeiros
            form.style.display = 'block';
            camposBarbeiro.style.display = 'none';
        });
    } else {
        console.log('Erro: Não foi possível encontrar os elementos necessários.');
    }
});

document.addEventListener('DOMContentLoaded', function () {
    // Dados dos cortes agendados (em um cenário real, isso viria de um banco de dados)
    const cortesAgendados = [
        { cliente: 'João Silva', data: '12/12/2024', hora: '10:00', servico: 'Corte de Cabelo', estado: 'Agendado', observacao: 'Nenhuma' },
        { cliente: 'Maria Souza', data: '12/12/2024', hora: '14:00', servico: 'Corte de Cabelo e Barba', estado: 'Confirmado', observacao: 'Cliente preferiu um estilo diferente' },
        { cliente: 'Pedro Lima', data: '13/12/2024', hora: '09:00', servico: 'Corte de Cabelo', estado: 'Agendado', observacao: 'Nenhuma' }
    ];

    // Verifique se o 'agenda-lista' existe na página
    const tabelaBody = document.querySelector('.tabela-cortes tbody');
    if (!tabelaBody) {
        console.error('Elemento <tbody> da tabela não encontrado.');
        return;
    }

    // Preencher a tabela com os dados
    cortesAgendados.forEach(corte => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${corte.cliente}</td>
            <td>${corte.data}</td>
            <td>${corte.hora}</td>
            <td>${corte.servico}</td>
            <td>${corte.estado}</td>
            <td>${corte.observacao}</td>
            <td><button class="btn-editar" onclick="editarCorte('${corte.cliente}', '${corte.data}', '${corte.hora}', '${corte.servico}', '${corte.estado}', '${corte.observacao}')">Editar</button></td>
        `;
        tabelaBody.appendChild(tr);
    });
});

// Função de editar agendamento (abertura de modal ou página)
function editarCorte(cliente, data, hora, servico, estado, observacao) {
    alert(`Editando corte para ${cliente}:\nData: ${data}\nHora: ${hora}\nServiço: ${servico}\nEstado: ${estado}\nObservação: ${observacao}`);
    // Aqui você pode redirecionar para uma página de edição ou abrir um modal para editar os detalhes do agendamento.
}
