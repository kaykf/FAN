const vlrSecreto = Math.floor(Math.random() * 100 + 1);
var vlrInicial = 1;
var vlrFinal = 100;
var vlrTentativa = 5;

function chutar(event){
    event.preventDefault();

    var vlrChute = parseInt(document.getElementById("chute").value);
    if(isNaN(vlrChute) || vlrChute < vlrInicial || vlrChute > vlrFinal){
        document.getElementById("avisos").textContent = "ERRO: Digite um valor válido entre "+ vlrInicial+ " e "+ vlrFinal;
    }
}