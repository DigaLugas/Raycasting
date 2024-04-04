let lim;
let ray;
let player;
function setup() {
    createCanvas(400,400);
    lim = new Boundary(300,100,300,300);
    ray = new Ray(100,200)
    player = new Player()
}

function draw() {
    background(0);
   
    lim.show();
    player.show();
    player.showRay();
}

