var intervalo;
// for popular
function scrollDireita1(){
  intervalo = setInterval(function(){ document.getElementById('scroller1').scrollLeft += 5 }  , 0);
};
function scrollEsquerda1(){
  intervalo = setInterval(function(){ document.getElementById('scroller1').scrollLeft -= 5 }  , 0);
};
function clearScroll1(){
  clearInterval(intervalo);
};
// for topRatedMovies
function scrollDireita2(){
  intervalo = setInterval(function(){ document.getElementById('scroller2').scrollLeft += 5 }  , 0);
};
function scrollEsquerda2(){
  intervalo = setInterval(function(){ document.getElementById('scroller2').scrollLeft -= 5 }  , 0);
};
function clearScroll2(){
  clearInterval(intervalo);
};
// for upcomingMovies
function scrollDireita3(){
  intervalo = setInterval(function(){ document.getElementById('scroller3').scrollLeft += 5 }  , 0);
};
function scrollEsquerda3(){
  intervalo = setInterval(function(){ document.getElementById('scroller3').scrollLeft -= 5 }  , 0);
};
function clearScroll3(){
  clearInterval(intervalo);
};
