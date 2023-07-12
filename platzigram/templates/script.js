

function tieneSoporteUserMedia(){
	return !!(navigator.getUserMedia || (navigator.mozGetUserMedia ||  navigator.mediaDevices.getUserMedia) || navigator.webkitGetUserMedia || navigator.msGetUserMedia)
}


function _getUserMedia(){
	return (navigator.getUserMedia || (navigator.mozGetUserMedia ||  navigator.mediaDevices.getUserMedia) || navigator.webkitGetUserMedia || navigator.msGetUserMedia).apply(navigator, arguments);
}


if (tieneSoporteUserMedia()) {
_getUserMedia(
    {video: true},
    function (stream) {
        console.log("Permiso concedido");
        $video.srcObject = stream;
        $video.play();
    }, function (error) {
        console.log("Permiso denegado o error: ", error);
    });
} else {
alert("Lo siento. Tu navegador no zsoporta esta característica");
}

var $video = document.getElementById("video"),
$canvas = document.getElementById("canvas"),
$boton = document.getElementById("boton"),
$estado = document.getElementById("estado");


$boton.addEventListener("click", function(){
 
    //Pausar reproducción
    $video.pause();
 
    //Obtener contexto del canvas y dibujar sobre él
    var contexto = $canvas.getContext("2d");
    $canvas.width = $video.videoWidth;
    $canvas.height = $video.videoHeight;
    contexto.drawImage($video, 0, 0, $canvas.width, $canvas.height);
 
    var foto = $canvas.toDataURL(); //Esta es la foto, en base 64
    $estado.innerHTML = "Enviando foto. Por favor, espera...";
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "./guardar_foto.php", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(encodeURIComponent(foto)); //Codificar y enviar
 
    xhr.onreadystatechange = function() {
        if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            console.log("La foto fue enviada correctamente");
            $estado.innerHTML = "Foto guardada con éxito. Puedes verla <a target='_blank' href='./" + xhr.responseText + "'> aquí</a>";
        }
    }
 
    //Reanudar reproducción
    $video.play();
});