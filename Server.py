import http.server
import socketserver

# Порт
PORT = 8000

# Обработчик
class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Разрешаем localStorage
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

# Запуск сервера
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ Сервер запущен: http://localhost:{PORT}")
    print("👉 Открой в браузере:")
    print("    http://localhost:8000/user.html")
    print("    http://localhost:8000/admin.html")
    print("❗ Чтобы остановить — нажми Ctrl+C")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Сервер остановлен.")
