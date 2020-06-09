//ja.prototype.

function ejecuta(){


    // for (var i=0 ;i<3) ;i++){
    //     document.getElementsByTagName("p")[i].onclick=saludo;

    // }
    
    // document.getElementById('importante').onclick=saludo;

//    var r = document.getElementsByClassName('pocoimportante')[0].onclick = saludo;

    // document.querySelector('#principal p:last-child').onclick=saludo;

    var r = document.querySelectorAll('#principal p')
    

    r[0].onclick=saludo;



}

function saludo(){
       
    alert('hola que hay de nuevo');
}



window.onload=ejecuta;