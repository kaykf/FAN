const vlrSecreto = Math.floor(Math.random() * 100 + 1);
var vlrInicial = 1;
var vlrFinal = 100;
var vlrTentativas = 5;

function chutar(event){
    event.preventDefault();

    var vlrChute = parseInt(document.getElementById("chute").value);
    if(isNaN(vlrChute) || vlrChute < vlrInicial || vlrChute > vlrFinal){
        document.getElementById("avisos").textContent = "ERRO: Digite um valor válido entre "+ vlrInicial+ " e "+ vlrFinal;
        return;
    }

    vlrTentativas = vlrTentativas - 1;

    if(vlrChute === vlrSecreto){
        document.getElementById("avisos").textContent = "PARABÉNS!! Você acertou! Muito Bom!";
        return;
    }

    if(vlrChute < vlrSecreto){
        vlrInicial = vlrChute + 1;
        document.getElementById("tentativa").textContent = "Você tem " + vlrTentativas + "tentativas para acertar o número de " + vlrInicial +" a " + vlrFinal + ". ";
        document.getElementById("avisos").textContent = "O número é maior!";
    }else{
        vlrFinal = vlrChute - 1
        document.getElementById("tentativa").textContent ="Você tem " + vlrTentativas + "tentativas para acertar o número de " + vlrInicial +" a " + vlrFinal + ". ";
        document.getElementById("avisos").textContent = "O número é menor!";
    }

    if(vlrTentativas === 0){
        document.getElementById("aviso").textContent = "Acabou suas Tentivas seu trouxa";
        return;
    }
}