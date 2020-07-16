window.addEventListener("load",()=>{
  const canvas=document.querySelector("#canvas");
  const c=canvas.getContext("2d");

  c.strokeRect(1000,1000,1500,1500);

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
    c.strokeStyle='#0e89b3';
    c.lineCap='round';
    c.lineTo(e.offsetX,e.offsetY)
    c.stroke();
  }

  canvas.addEventListener('mousedown',startPosition);
  canvas.addEventListener('mouseup',finishedPainting);
  canvas.addEventListener('mousemove',draw);
});
