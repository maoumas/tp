import React, { useState, useRef, useEffect } from 'react';
import templateImage from './assets/template.png';

function App() {
    const [title, setTitle] = useState("VIDEO TITLE GOES HERE");
    const [subtitle, setSubtitle] = useState("SUBTITLE TEXT");
    const [bgColor, setBgColor] = useState("#1a1a1a");
    const canvasRef = useRef<HTMLCanvasElement>(null);

    // Helper to draw the validation canvas
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const img = new Image();
        img.src = templateImage;
        img.crossOrigin = "anonymous";

        img.onload = () => {
            // Set canvas size to match transparency template (usually 1920x1080 for YT) or scale down
            // For now let's assume standard 1080p but verify aspect ratio
            canvas.width = 1280; // Standard YouTube thumb size often used
            canvas.height = 720;

            // 1. Draw Background
            ctx.fillStyle = bgColor;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // 2. Draw Template Overlay
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

            // 3. Draw Text
            // Configuration for text based on stripes (approximate positions, need tuning)
            // Black stripe (top)
            ctx.fillStyle = "white";
            ctx.font = "bold 60px Arial"; // Placeholder font
            ctx.textAlign = "right";
            ctx.fillText(title, canvas.width - 250, 450); // Adjust Y coordinate

            // Blue stripe (bottom)
            ctx.fillStyle = "white";
            ctx.font = "bold 80px Arial";
            ctx.fillText(subtitle, canvas.width - 50, 650); // Adjust Y
        };

    }, [title, subtitle, bgColor]);

    const handleDownload = () => {
        const canvas = canvasRef.current;
        if (canvas) {
            const link = document.createElement('a');
            link.download = 'thumbnail.png';
            link.href = canvas.toDataURL();
            link.click();
        }
    }

    return (
        <div className="min-h-screen bg-gray-900 text-white p-8 font-sans">
            <header className="mb-8 flex items-center justify-between">
                <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
                    Thumbnail Generator
                </h1>
            </header>

            <main className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Controls */}
                <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 space-y-6">
                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-gray-300">Title (Top Stripe)</label>
                        <input
                            type="text"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            className="w-full bg-gray-700 border border-gray-600 rounded-lg p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-gray-300">Subtitle (Bottom Stripe)</label>
                        <input
                            type="text"
                            value={subtitle}
                            onChange={(e) => setSubtitle(e.target.value)}
                            className="w-full bg-gray-700 border border-gray-600 rounded-lg p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-gray-300">Background Color</label>
                        <div className="flex gap-2">
                            {['#1a1a1a', '#ef4444', '#3b82f6', '#10b981', '#f59e0b'].map(c => (
                                <button
                                    key={c}
                                    onClick={() => setBgColor(c)}
                                    className={`w-8 h-8 rounded-full border-2 ${bgColor === c ? 'border-white' : 'border-transparent'}`}
                                    style={{ backgroundColor: c }}
                                />
                            ))}
                            <input type="color" value={bgColor} onChange={(e) => setBgColor(e.target.value)} className="bg-transparent h-8 w-8 ml-2" />
                        </div>
                    </div>

                    <button
                        onClick={handleDownload}
                        className="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-4 rounded-lg transition-colors flex items-center justify-center gap-2"
                    >
                        Download Thumbnail
                    </button>
                </div>

                {/* Preview */}
                <div className="lg:col-span-2 bg-gray-800 p-4 rounded-xl border border-gray-700 flex items-center justify-center">
                    <canvas
                        ref={canvasRef}
                        className="max-w-full h-auto shadow-2xl rounded-lg"
                        style={{ maxHeight: '70vh' }}
                    />
                </div>
            </main>
        </div>
    )
}

export default App
