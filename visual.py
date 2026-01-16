from bottle import route, run
@route('/')
def index():
    return """
    <html>
    <head>
        <title>EcoKernel AI - Scarlet</title>
        <style>
            @keyframes scanline { 0% { bottom: 100%; } 80% { bottom: 0%; } 100% { bottom: 0%; } }
            @keyframes pulse { 0% { box-shadow: 0 0 5px #00ff41; } 50% { box-shadow: 0 0 20px #00ff41; } 100% { box-shadow: 0 0 5px #00ff41; } }
            body { background-color: #0a0a0a; color: #00ff41; font-family: 'Courier New', Courier, monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
            .container { border: 2px solid #00ff41; padding: 30px; position: relative; background: rgba(0, 20, 0, 0.9); animation: pulse 3s infinite; width: 80%; max-width: 500px; border-radius: 10px; }
            .scan { position: absolute; width: 100%; height: 2px; background: rgba(0, 255, 65, 0.3); top: 0; left: 0; animation: scanline 4s linear infinite; }
            h1 { font-size: 1.5rem; text-transform: uppercase; letter-spacing: 5px; margin-bottom: 20px; }
            .stat { text-align: left; margin-bottom: 15px; }
            .bar-bg { width: 100%; background: #002200; height: 12px; border: 1px solid #00ff41; border-radius: 5px; overflow: hidden; }
            .bar-fill { height: 100%; background: #00ff41; width: 0%; transition: width 2s ease-in-out; }
            .btn { background: #00ff41; color: #000; border: none; padding: 15px; width: 100%; font-weight: bold; cursor: pointer; margin-top: 20px; border-radius: 5px; }
            .btn:hover { background: #008f11; color: #fff; }
        </style>
    </head>
    <body onload='document.getElementById("fill1").style.width="90%"; document.getElementById("fill2").style.width="65%"'>
        <div class='container'>
            <div class='scan'></div>
            <h1>📡 ECO-KERNEL</h1>
            <p style='font-size: 0.8rem;'>AUTH: SCARLET_FUENMAYOR_DIAZ</p>
            <div class='stat'>
                <small>NÚCLEO BIO-MÉTRICO</small>
                <div class='bar-bg'><div id='fill1' class='bar-fill'></div></div>
            </div>
            <div class='stat'>
                <small>SINCRONIZACIÓN ISLA NUEVA</small>
                <div class='bar-bg'><div id='fill2' class='bar-fill' style='background:#ffaa00;'></div></div>
            </div>
            <button class='btn' onclick='startSystem()'>INICIALIZAR PROTOCOLO</button>
        </div>
        <script>
            function startSystem() {
                var audio = new Audio('https://www.myinstants.com/media/sounds/sci-fi-shutter.mp3');
                audio.play();
                alert('EcoKernel: Protocolo Scarlet activado. Procesando datos de Isla Nueva...');
            }
        </script>
    </body>
    </html>
    """
run(host='0.0.0.0', port=8080)
