window.addEventListener("load",()=>{
  const canvas=document.querySelector("#canvas");
  const c=canvas.getContext("2d");
  //let classifier;
  //console.log(c);

  //ctx.globalCompositeOperation = 'destination-over';
  //c.fillStyle='white';
  //c.fillRect(1000,1000,1500,1500);


  let painting=false;
  function startPosition(e){
    painting=true;
    draw(e);
  }

  function finishedPainting() {
    painting=false;
    c.beginPath();
  }

  function draw(e){
    if(!painting) return;
    c.lineWidth=5;
    c.strokeStyle='#fff';
    c.lineCap='round';
    c.lineTo(e.offsetX,e.offsetY)
    c.stroke();
  }

  canvas.addEventListener('mousedown',startPosition);
  canvas.addEventListener('mouseup',finishedPainting);
  canvas.addEventListener('mousemove',draw);
  //getting content of canvas

  const display=document.querySelector("#Display");
  const image_view=document.querySelector("#user_image");
    display.addEventListener("click",()=>{
    const dataURI=canvas.toDataURL();
    //console.log(dataURI);
    image_view.src= dataURI;
    c.clearRect(0,0,canvas.width,canvas.height)
  });
  $("#Recognise").click(function(){
       let message = {
           image: base64Image
       }
       console.log(message);
       $.post("http://127.0.0.1:5000/send", JSON.stringify(message), function(response){
           //$("#dog-prediction").text(response.prediction.dog.toFixed(6));
           //$("#cat-prediction").text(response.prediction.cat.toFixed(6));
           console.log(response);
       });
     });
});
