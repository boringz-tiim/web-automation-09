"""本地登录测试站点服务器（只使用 Python 标准库）。"""

from argparse import ArgumentParser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys


SITE_DIR = Path(__file__).resolve().parent / "site"


class QuietHandler(SimpleHTTPRequestHandler):
    """提供静态页面，并把首页重定向到练习用登录页。"""

    def do_GET(self):
        if self.path in {"", "/"}:
            self.send_response(302)
            self.send_header("Location", "/Home/user/login.html")
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format, *args):
        print(f"[本地测试站] {self.address_string()} - {format % args}")


class LocalServer(ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):
        """忽略 Chrome 预连接主动断开产生的无关日志。"""
        error = sys.exc_info()[1]
        if isinstance(error, ConnectionResetError):
            return
        super().handle_error(request, client_address)


def main():
    parser = ArgumentParser(description="启动本地 TPshop 登录练习站点")
    parser.add_argument("--port", type=int, default=8000, help="监听端口，默认 8000")
    args = parser.parse_args()

    handler = partial(QuietHandler, directory=SITE_DIR)
    server = LocalServer(("127.0.0.1", args.port), handler)
    url = f"http://127.0.0.1:{args.port}/Home/user/login.html"

    print("本地登录测试环境已启动")
    print(f"访问地址：{url}")
    print("按 Ctrl+C 停止服务器")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n正在停止服务器……")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
