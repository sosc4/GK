const scene = new THREE.Scene({color: 0xfff});
const camera = new THREE.PerspectiveCamera(100, window.innerWidth / window.innerHeight, 1, 1000);
const renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

const light = new THREE.PointLight(0xffffff, 1, 300);
light.position.set(-5, -1, 0.5);
camera.add(light);
scene.add(camera);

const material = new THREE.MeshPhongMaterial(
    {
        color: 0xffffff,
    }
);
const points = [
    {"x": 1.2, "y": 0},
    {"x": 1.2, "y": 0.3},
    {"x": 0.9, "y": 0.3},
    {"x": 0.9, "y": 0.4},
    {"x": 0.78, "y": 1},
    {"x": 0.66, "y": 2},
    {"x": 0.5, "y": 4},
    {"x": 1, "y": 4},
    {"x": 1, "y": 4.25},
    {"x": 0.15, "y": 4.25},
    {"x": 0.15, "y": 6},
];

const geometry = new THREE.LatheGeometry(points, 32);
const lathe = new THREE.Mesh(geometry, material);
lathe.position.set(0, -4, 0);
scene.add(lathe);

const struct = new THREE.SphereGeometry(-0.8, 32, 16);
const sphere = new THREE.Mesh(struct, material);
sphere.position.set(0,1,0)
scene.add(sphere);

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

camera.position.z = 7;

animate();