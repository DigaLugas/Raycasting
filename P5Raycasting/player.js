class Player {
    constructor() {
        this.pos = createVector(width / 2, height / 2);
        this.rays = [];
        for (let a = 0; a < 80; a += 1) { 
            this.rays.push(new Ray(this.pos, radians(a))); 
        }
    }
    showRay(){
        for (let ray of this.rays) {
            const pt = ray.castRay();
            if(pt){
                line(this.pos.x, this.pos.y, pt.x, pt.y);
            }

        }
    }
    show() {
        fill(255);
        ellipse(this.pos.x, this.pos.y, 6);
        for (let i = 0; i < this.rays.length; i++) {
            this.rays[i].show();
        }
    }
}
