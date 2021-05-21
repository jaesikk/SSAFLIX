var intervalo;

function scrollDireita(){
  intervalo = setInterval(function(){ document.getElementById('scroller').scrollLeft += 3 }  , 0);
};
function scrollEsquerda(){
  intervalo = setInterval(function(){ document.getElementById('scroller').scrollLeft -= 3 }  , 0);
};
function clearScroll(){
  clearInterval(intervalo);
};
