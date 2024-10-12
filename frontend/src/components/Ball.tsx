import React, { useEffect, useRef } from 'react';

declare global {
  interface Window { THREE: any; }
}

const Ball: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const scene = new window.THREE.Scene();
    const camera = new window.THREE.PerspectiveCamera(25, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new window.THREE.WebGLRenderer({ canvas: canvasRef.current, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    const geometry = new window.THREE.SphereGeometry(1, 22, 22);
    const material = new window.THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
    const sphere = new window.THREE.Mesh(geometry, material);
    scene.add(sphere);
    camera.position.z = 5;

    const animate = () => {
      requestAnimationFrame(animate);
      sphere.rotation.x += 0.0012;
      sphere.rotation.y -= 0.0012;
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;
      renderer.setSize(width, height);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return <canvas ref={canvasRef} className="background-canvas" />;
};

export default Ball;