const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particlesArray = [];
        const maxParticles = 100;

        class Particle {
            constructor(x, y, size, color, speedX, speedY) {
                this.x = x;
                this.y = y;
                this.size = size;
                this.color = color;
                this.speedX = speedX;
                this.speedY = speedY;
            }

            update() {
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.size > 0.2) this.size -= 0.1;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.fill();
            }
        }

        function createParticles(event) {
            const x = event.x;
            const y = event.y;
            const size = Math.random() * 5 + 2;
            const color = `hsl(${Math.random() * 360}, 100%, 50%)`;
            const speedX = (Math.random() - 0.5) * 4;
            const speedY = (Math.random() - 0.5) * 4;

            particlesArray.push(new Particle(x, y, size, color, speedX, speedY));

            if (particlesArray.length > maxParticles) {
                particlesArray.shift(); // Remove old particles
            }
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < particlesArray.length; i++) {
                particlesArray[i].update();
                particlesArray[i].draw();
            }

            requestAnimationFrame(animate);
        }

        window.addEventListener('mousemove', createParticles);
        animate();

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });