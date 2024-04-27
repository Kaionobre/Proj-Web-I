//BOTÕES DE FORMULÁRIO
const botao_enviar = document.querySelector(`#botao_enviar`);
const form_name = document.querySelector(`.name_box `);
const form_email = document.querySelector(`.email_box`);
//BOTÕES DE COMPRA
const botao_comprar = document.querySelector(`#comprar01`);
const botao_comprar02 = document.querySelector(`#comprar02`);
const botao_comprar03 = document.querySelector(`#comprar03`);
const botao_comprar04 = document.querySelector(`#comprar04`);

//BOTÕES DE ICONES
const iconesIG = document.querySelector(`.ig`);
const iconesYT = document.querySelector(`.yt`);
const iconesWPP = document.querySelector(`.wpp`);

//EVENTOS ATRELADOS AOS BOTÕES DE FORMULÁRIO
botao_enviar.addEventListener(`click`, function(){
    alert(`FORMULÁRIO ENVIADO`)
})
//EVENTOS ATRELADOS AOS BOTÕES DE COMPRA
botao_comprar.addEventListener(`click`, function(){
    alert(`CAMISA BRANCA CLICADA`);
})
botao_comprar02.addEventListener(`click`, function(){
    alert(`CAMISA PRETA CLICADA`);
})
botao_comprar03.addEventListener(`click`, function(){
    alert(`SHORT HIGH CLICADO`);
})
botao_comprar04.addEventListener(`click`, function(){
    alert(`SHOULDER BAG CLICADA`);
})

//EVENTOS ATRELADOS AOS BOTÕES DE REDES SOCIAIS
iconesIG.addEventListener(`click`, function(){
    confirm(`Tem certeza que quer sair dessa página e ir para o INSTAGRAM EMBER?`);
})
iconesYT.addEventListener(`click`, function(){
    confirm(`Tem certeza que quer sair dessa página e ir para o YOUTUBE EMBER?`);
})
iconesWPP.addEventListener(`click`, function(){
    confirm(`Tem certeza que quer sair dessa página e ir para o WHATSAPP EMBER?`);
})